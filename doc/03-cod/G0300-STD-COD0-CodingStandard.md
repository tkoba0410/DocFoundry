---

schema: "[https://schema.org/CreativeWork](https://schema.org/CreativeWork)"
@type: "CreativeWork"
identifier: "G0300-STD-COD0-CodingStandard"
name: "Coding Standard – Core (Language-Agnostic)"
version: "v1.2.0"
datePublished: "2025-11-09"
status: "Draft (Reorganized Structure)"
creator:
@type: "Organization"
name: "Documentation Team"
inLanguage: ["ja", "en"]
description: >
言語非依存のコーディング原則を定義する標準文書。v1.2.0では章構成を再編し、
原則・適用・適合性・測定・検証の五層構造に整理した。
related_docs:

* "G0100-STD-DOCF-FormatPolicy"
* "G0110-STD-DOCO-OperationalPolicy"
* "G0400-STD-YML0-ContentStructure"
* "G0410-STD-YML1-LayerModel"
* "G0420-STD-YML2-SyntaxStyleGuide"

---

# [STD-COD0] Coding Standard – Core (Language-Agnostic)

---

## 1. 目的

プログラミング言語に依存しない**コーディング行為の原則**を定義し、
品質・再利用性・検証可能性を高めることを目的とする。

## 2. 適用範囲・非対象（Non-Goals）

適用対象：アプリケーション、ライブラリ、ツールのコード記述そのもの。
非対象：設計仕様（ARC系）、要求仕様（REQ系）、運用設定（OPS系）など、構造・運用定義に関する内容。

## 3. 規範レベル

RFC 2119 に準拠し、**MUST / SHOULD / MAY / MUST NOT / SHOULD NOT** を用いる。
逸脱は「#15 逸脱管理」に従い、T4-Deviation 形式で管理する。

---

# Part I. 原則（Principles）

## 4. 記法・可読性

* 可読性優先 (MUST)
* 自己記述性 (MUST)
* 一貫性 (MUST)
* 最小公開 (MUST)
* 副作用の局所化 (MUST)
* 早期失敗 (MUST)
* コメントは理由説明 (SHOULD)

## 5. 依存とモジュール境界

循環依存 (MUST NOT)。
依存方向の単調性 (SHOULD)。
暫定的跨ぎ参照は T4-Deviation で管理。

## 6. エラー処理 / 例外

空 catch 禁止 (MUST NOT)。
契約違反区別 (MUST)。
再スロー時に文脈付与 (MUST)。
冪等操作のみ再試行 (SHOULD)。

## 7. 並行性 / リソース管理

共有可変状態最小化 (MUST)。
キャンセル伝播 (MUST)。
決定的解放 (MUST)。

## 8. 設定・シークレット

設定外在化 (MUST)。
秘密情報保護 (MUST)。
既定値検証 (SHOULD)。

## 9. ログ / 計測

PII禁止 (MUST)。
構造化ログ (SHOULD)。
キー構成はOPS標準に委譲。

## 10. テスト規約

層別化 (MUST)。
カバレッジ閾値 0.80 / 0.90 (MUST)。
決定的テスト (MUST)。
プロパティベース (SHOULD)。

## 11. セキュリティと依存

最小権限 (MUST)。
依存性衛生 (MUST)。
入力検証 (MUST)。

## 12. ドキュメント / コメント

公開APIのDoc必須 (MUST)。
理由説明コメント (SHOULD)。
ADRはARC文書で管理。

## 13. 禁止 / 非推奨パターン

* グローバル可変状態・シングルトン乱用 (MUST NOT)
* 循環依存・層逆参照 (MUST NOT)
* 空 catch ・戻り値無視 (MUST NOT)
* マジックナンバー・資格情報ハードコード (MUST NOT)
* PII ログ出力 (MUST NOT)

---

# Part II. 適用と運用

## 14. プロファイル運用指針

* Core / Strict / Lite の3階層を定義。

  * **Core**: 本標準のMUST要件を完全に満たす。
  * **Strict**: Coreより厳格な社内運用プロファイル。
  * **Lite**: 研究・試作・教育用の緩和版（Annex D）。
* `profile_ref` による適用優先度：Strict > Core > Lite。
* CI／検証ツールは `profile_ref` で自動切替可能とする。

## 15. 適合性（Conformance）

**適合レベル**：

* Core：本標準#4〜#13のMUST遵守＋#16メトリクス閾値達成。
* Strict：Core＋追加Profile要件を満たす。
* Lite：Annex D の閾値に基づくR&D向け。

**判定方法**：

* メトリクス検証（#16）＋逸脱台帳（Annex A）を参照。
* CI自動検証およびレビューで評価。

**逸脱時対応**：

* `T4-Deviation` テンプレートに基づき是正計画・期限を設定。
* CIで期限超過を警告またはFailとする。

## 16. 測定（Metrics YAML）

```yaml
version: 1
rules:
  cod.core:
    func_max_lines: 50
    cyclomatic_max: 10
    magic_numbers_forbid: true
    logging_pii_forbid: true
    test_coverage_min: 0.80
    test_coverage_critical_min: 0.90
  cod.security:
    input_validation_required: true
    dispose_required: true
    dependency_sca_required: true
  cod.quality:
    naming_abbrev_allowlist: []
    flaky_tests_forbid: true
valid_until: "2026-11-30"
```

## 17. 検証（Verification / CI Integration）

* 静的解析・カバレッジゲート・依存衛生・シークレットスキャン・逸脱期限検査を自動化。
* CI設定例は Annex B を参照。
* 測定・適合結果は CIレポートとして保存・レビュー対象とする。

## 18. 逸脱管理

逸脱は `T4-Deviation` 形式で管理（Annex A参照）。
是正計画・期限を設定し、CIで自動検証可能とする。

---

# Part III. 管理情報

## 19. 用語集

PII = Personally Identifiable Information
ADR = Architectural Decision Record
SCD = 開発ライフサイクル定義モデル

## 20. 改版履歴

| 版      | 日付           | 内容                              |
| ------ | ------------ | ------------------------------- |
| v1.2.0 | "2025-11-09" | 章構成を再編（案B適用）。適用・適合・測定・検証を明確化。   |
| v1.1.0 | "2025-11-09" | Front Matter統一、Annex追加、メトリクス分割。 |
| v1.0.0 | "2025-10-27" | 初版（正式採用）。                       |

---

# Annex A. Deviation Template (Reference from G0110)

```yaml
t4_deviation:
  id: DEV-2025-001
  target_rule: "error.empty_catch.forbid"
  description: "一時的にサードパーティSDKの例外仕様を吸収"
  mitigation_plan: "SDK更新後に除去予定"
  deadline: "2026-03-31"
  approver: "QA Lead"
```

---

# Annex B. CI Workflow Example

```yaml
name: Code Quality Validation
on: [push, pull_request]
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
      - name: Install tools
        run: pip install pylint coverage safety
      - name: Static Analysis
        run: pylint src/ --exit-zero
      - name: Coverage Gate
        run: pytest --cov=. --cov-fail-under=80
      - name: Secret Scan
        run: gitleaks detect --no-banner --redact
      - name: Deviation Expiry Check
        run: python tools/check_deviation.py deviations/
```

---

# Annex C. 用語整合（G0410 8.4 準拠）

| 意味  | 採用キー                               | 非推奨キー                 |
| --- | ---------------------------------- | --------------------- |
| 発行日 | `datePublished` / `date_published` | `date`                |
| 作成者 | `creator`                          | `author`, `editor`    |
| 説明  | `description`                      | `summary`, `abstract` |

---

# Annex D. R&D向け軽量プロファイル（COD0-Lite）

```yaml
$schema: "/schemas/cod0-profile.schema.yaml"
profile_id: "COD0-Lite"
profile_name: "Coding Standard Profile (Lite)"
purpose: "R&D and prototype development relaxed coding standard"
inherits_from: "G0300-STD-COD0"
rules:
  cod.core:
    func_max_lines: 200
    cyclomatic_max: 30
    test_coverage_min: 0.50
    test_coverage_critical_min: 0.60
  cod.security:
    input_validation_required: true
    dispose_required: false
    dependency_sca_required: false
  cod.quality:
    naming_abbrev_allowlist: ["id", "url", "tmp"]
    flaky_tests_forbid: false
    logging_pii_forbid: true
valid_until: "2026-11-30"
level: "Experimental"
ci_behavior:
  deviation_expiry: "warn"
  coverage_gate: "warn"
```
