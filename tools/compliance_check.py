#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DocFoundry G0100/G0101 compliance checker
-----------------------------------------
- Scans Markdown files and validates presence of DCMM front-matter.
- Writes a JSONL report (one line per file).
- Exits non-zero based on --fail-on policy.

Usage:
  python3 tools/compliance_check.py     --ruleset 0-standards/rules/G0101-STD-DOC1_ruleset.json     --output compliance_report.jsonl     --fail-on error     --include-glob "0-standards/**/*.md"     --include-glob "1-project-template/docs/**/*.md"     --exclude-glob "README.md"     --exclude-glob "0-standards/README.md"

Notes:
  - By G0100 policy, root-level and /0-standards/ README.md are informational and excluded by default.
  - Required keys default to: ["doc_id","title","version","date","status"].
"""

import argparse
import json
import os
import re
import sys
import glob
from typing import List, Dict

try:
    import yaml
except Exception as e:
    print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

FRONT_MATTER_RX = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)

DEFAULT_REQUIRED = ["doc_id", "title", "version", "date", "status"]

DEFAULT_EXCLUDES = [
    "README.md",
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
                import yaml as _yaml
                return _yaml.safe_load(f)
            return json.load(f)
        except Exception as e:
            print(f"WARN: failed to parse ruleset {path}: {e} (continuing with defaults)", file=sys.stderr)
            return {}

def match_globs(path: str, patterns: List[str]) -> bool:
    norm = path.replace("\\", "/")
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
        return {"file": md_path, "status": "❌ No front matter", "detail": "Missing YAML front matter block"}

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
    ap.add_argument("--ruleset", default=None, help="Path to ruleset (json/yaml). Optional")
    ap.add_argument("--output", default="compliance_report.jsonl", help="Output JSONL path")
    ap.add_argument("--fail-on", default="error", choices=["ok","warning","error","any"],
                    help="Failure policy: ok=never fail, warning=fail on warnings/errors, error=fail only on errors, any=fail on any non-OK")
    ap.add_argument("--include-glob", action="append", default=[], help="Glob for files to include (repeatable)")
    ap.add_argument("--exclude-glob", action="append", default=[], help="Glob for files to exclude (repeatable)")
    args = ap.parse_args()

    ruleset = load_ruleset(args.ruleset)
    required = ruleset.get("required_keys", DEFAULT_REQUIRED)

    excludes = DEFAULT_EXCLUDES + args.exclude_glob
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

    # Write JSONL
    with open(args.output, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"Compliance check finished. files={len(results)} errors={error_count} warnings={warn_count}")
    # Determine exit code
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
