#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DocFoundry G0100/G0101 compliance checker (v1.1)
- More robust front-matter detection (handles BOM/leading blank lines).
- Better default excludes for generic OSS docs (README/CHANGELOG/etc. anywhere).
- Optional console summary.

Exit policy (--fail-on): ok|warning|error|any (default: error)
"""
import argparse, json, os, re, sys, glob
from typing import List, Dict
try:
    import yaml
except Exception:
    print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

# Allow BOM and leading whitespace before '---'
FRONT_MATTER_RX = re.compile(r"^(?:\ufeff)?\s*---\n(.*?)\n---\n?", re.DOTALL)

DEFAULT_REQUIRED = ["doc_id", "title", "version", "date", "status"]

DEFAULT_EXCLUDES = [
    "**/README.md",
    "README.md",
    "**/CHANGELOG.md",
    "**/CONTRIBUTING.md",
    "**/SECURITY.md",
    "**/CODE_OF_CONDUCT.md",
    "**/LICENSE.md",
    "0-standards/README.md",
    "**/.git/**",
    "**/.github/**",
    "**/node_modules/**",
    "**/venv/**",
    "**/.venv/**",
]

def load_ruleset(path: str) -> Dict:
    if not path:
        return {}
    if not os.path.exists(path):
        print(f"WARN: ruleset not found: {path} (continuing with defaults)", file=sys.stderr)
        return {}
    with open(path, encoding="utf-8") as f:
        try:
            if path.endswith(('.yaml', '.yml')):
                return yaml.safe_load(f)
            return json.load(f)
        except Exception as e:
            print(f"WARN: failed to parse ruleset {path}: {e} (continuing with defaults)", file=sys.stderr)
            return {}

def match_globs(path: str, patterns: List[str]) -> bool:
    norm = path.replace('\\', '/')
    for pat in patterns:
        if glob.fnmatch.fnmatch(norm, pat):
            return True
    return False

def discover_files(includes: List[str], excludes: List[str]) -> List[str]:
    files = set()
    if not includes:
        includes = ["**/*.md"]
    for pat in includes:
        for p in glob.glob(pat, recursive=True):
            if os.path.isdir(p):
                continue
            files.add(p)
    keep = []
    for p in sorted(files):
        if match_globs(p, excludes):
            continue
        keep.append(p)
    return keep

def check_front_matter(md_path: str, required: List[str]) -> Dict:
    try:
        with open(md_path, encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        return {"file": md_path, "status": "❌ IO error", "detail": str(e)}
    m = FRONT_MATTER_RX.match(text)
    if not m:
        return {"file": md_path, "status": "❌ No front matter", "detail": "Missing YAML front matter block at top"}
    yaml_block = m.group(1)
    try:
        meta = yaml.safe_load(yaml_block) or {}
    except Exception as e:
        return {"file": md_path, "status": "❌ YAML error", "detail": str(e)}
    missing = [k for k in required if k not in meta]
    if missing:
        return {"file": md_path, "status": "⚠ Missing keys", "detail": ", ".join(missing)}
    return {"file": md_path, "status": "✅ OK"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ruleset", default=None)
    ap.add_argument("--output", default="compliance_report.jsonl")
    ap.add_argument("--fail-on", default="error", choices=["ok","warning","error","any"])
    ap.add_argument("--include-glob", action="append", default=[])
    ap.add_argument("--exclude-glob", action="append", default=[])
    ap.add_argument("--summary", action="store_true", help="Print human-readable summary to console")
    args = ap.parse_args()

    ruleset = load_ruleset(args.ruleset)
    required = ruleset.get("required_keys", DEFAULT_REQUIRED)

    excludes = list(dict.fromkeys(DEFAULT_EXCLUDES + args.exclude_glob))  # de-dup
    includes = args.include_glob

    files = discover_files(includes, excludes)
    if not files:
        print("WARN: No files matched include patterns.")
    results = []

    error_count = 0
    warn_count = 0

    for p in files:
        r = check_front_matter(p, required)
        results.append(r)
        if r["status"].startswith("❌"):
            error_count += 1
        elif r["status"].startswith("⚠"):
            warn_count += 1

    with open(args.output, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    if args.summary:
        # compact console output of offenders
        offs = [r for r in results if r["status"] != "✅ OK"]
        if offs:
            print("\n== Offenders ==")
            for r in offs:
                print(f"- {r['status']}: {r['file']}  ({r.get('detail','')})")
        else:
            print("\nAll checked files are compliant.")

    print(f"Compliance check finished. files={len(results)} errors={error_count} warnings={warn_count}")
    if args.fail_on == "ok":
        sys.exit(0)
    if args.fail_on == "warning" and (warn_count > 0 or error_count > 0):
        sys.exit(1)
    if args.fail_on == "error" and error_count > 0:
        sys.exit(2)
    if args.fail_on == "any" and (error_count > 0 or warn_count > 0):
        sys.exit(3)
    sys.exit(0)

if __name__ == "__main__":
    main()
