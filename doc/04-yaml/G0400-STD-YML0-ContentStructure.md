---

schema: "https://schema.org/CreativeWork"
@type: "CreativeWork"       # ← G0100/G0110と統一
identifier: "G0400-STD-YML0-ContentStructure"
name: "YAML文書内容構造標準（YML0: YAML Content Structure Standard）"
version: "v2.1.0"
datePublished: "2025-11-06"
status: "Publication Approved"
creator: "Documentation Team"
reviewers: ["Documentation Review Committee"]
confidentiality: "Public"
lifecycle: "Canonical"
inLanguage: ["ja"]
description: "本標準は、文書内容をYAML形式で構造化するための体系的指針を定義する。JSON Schemaによる形式保証とSchema.orgによる意味付けを中核とし、運用層をProfileとして分離する構成を採用する。5部構成に再整理し、付録に最小Schema・テンプレート・CI例を含む正式発行版。"
----------------------------------------------------------------------------------------------------------------------------------------------------------------

# G0400-STD-YAMLContentStructure（v2.1.0 / Publication Approved）

---

# Part I. 原則編（Philosophy）

## 1. 目的

文書内容を**YAML形式で構造化**し、AI・CI・人間が共通に理解・検証可能な形式で保持するための標準を示す。本標準は内容（Content）層を中核とし、**運用層（Profile）や生成ルールは別途管理する**ことを前提とする。

## 2. YAML三層モデル

文書内容は次の三層で構成する。

| 層                  | 目的             | 技術要素                |
| ------------------ | -------------- | ------------------- |
| **データ層（Content）**  | 文書の実体情報を構造化    | YAML                |
| **形式層（Structure）** | 型・必須項目・パターンを定義 | JSON Schema 2020-12 |
| **意味層（Semantic）**  | 文書の意味・語彙を定義    | Schema.org          |

> 運用層（Profile）は本標準の対象外とし、別文書に定義する。

## 3. 適用範囲と関係

* 本標準は、G0100（FormatPolicy）と整合し、G0401（YAML使用規約）は不採用とする。
* G0400は、構造・意味・検証を統一的に扱う単独標準として運用可能である。

---

# Part II. 内容編（Specification）

## 4. YAML構造仕様

```yaml
$schema: "/specs/schema/spec-core.schema.yaml"
@context: "https://schema.org"
@type: "CreativeWork"
profile_ref: "/profiles/P0001-YAML-Docs.yaml"

identifier: "G0501-STD-SPEC"
name: "System Specification"
version: "v1.0.0"
date_published: "2025-11-06"
in_language: ["ja"]  # BCP47形式の言語タグ（例：ja, en-US）
schema_version: "1.0"

sections:
  objectives:
    - id: "OBJ-001"
      text: "本システムの目的を定義する。"
  requirements:
    - id: "REQ-001"
      type: "functional"
      text: "ユーザはデータを登録できる。"
      priority: "must"
  constraints:
    - id: "CsST-001"
      text: "登録データの容量は100MB以内とする。"

creator:
  @type: "Organization"
  name: "Documentation Team"
status: "Publication Approved"   # ← status位置をFront Matter上部へ移動

```

## 5. 用語定義

| 用語              | 定義                                                            | 補足               |
| --------------- | ------------------------------------------------------------- | ---------------- |
| **Objective**   | ビジネス目的または利用者価値の到達点。                                           | 例：サービスの達成目的。     |
| **Requirement** | システムが満たすべき観測可能な振る舞い・品質。                                       | typeで分類する。       |
| **Constraint**  | 運用・法規・性能上の制約または禁止事項。                                          | 数値・条件などで明示。      |
| **Type**        | 要件分類：`functional` / `nonfunctional`。                          | Schemaで列挙値として強制。 |
| **Priority**    | 実現重要度：`must` / `should` / `may`。`should`は「原則必須だが合理的理由により例外可」。 | RFC2119準拠。       |

## 6. 構文ルール

| 項目             | 規定                                                       |
| -------------- | -------------------------------------------------------- |
| **キー命名**       | `snake_case` を使用。例：`date_published`, `in_language`       |
| **日付形式**       | ISO8601形式（例：`2025-11-06`）                                |
| **真偽値**        | `true` / `false` 固定                                      |
| **数値**         | 小数点形式（不要な0を付けない）                                         |
| **文字列**        | UTF-8、ダブルクォート推奨                                          |
| **IDパターン**     | `^OBJ-[0-9]+$`, `^REQ-[0-9]+$`, `^CST-[0-9]+$`           |
| **列挙値**        | `must` / `should` / `may`                                |
| **sections順序** | `objectives` → `requirements` → `constraints` の順は**必須**。 |

---

# Part III. 管理編（Governance）

## 7. 互換性ポリシー

* `schema_version` を設け、**メジャー更新は互換非保証、マイナー更新は後方互換維持**とする。
* **破壊的変更の定義**：①必須キー追加・削除、②列挙値変更、③型変更、④ID正規表現変更。
* 破壊的変更時はSchema版番号を更新し、CI警告を義務化。

## 8. Profile参照と連携

* YAMLヘッダに`profile_ref`キーを設け、外部ProfileのパスまたはURIを指定可。
* `profile_ref`は任意であり、CIにおける生成・検証ルールを外部参照する。
* Profile文書例：`/profiles/P0001-YAML-Docs.yaml`

## 9. Schema.org選定ガイド

| 文書種別        | 推奨`@type`             | 説明                                  |
| ----------- | --------------------- | ----------------------------------- |
| 仕様書 / 方針書   | `CreativeWork`        | 汎用文書。すべての標準・規約文書に使用可。迷う場合はこれを既定とする。 |
| 設計書 / 解説書   | `TechArticle`         | 技術設計や設計思想を記述する文書。                   |
| 製品仕様 / 実装構成 | `SoftwareApplication` | 実装対象のシステム・アプリケーションを表す。              |

---

# Part IV. 検証編（Validation）

## 10. 検証基準

* **構文検証**：`yamllint` によるフォーマット検証。
* **型検証**：`jsonschema` による必須キー・列挙・形式確認。
* **意味整合**：Schema.orgの`@type`が有効語彙に一致することを確認。

## 11. CI実行例

```yaml
- run: pip install yamllint jsonschema
- run: yamllint specs/doc.yaml
- run: python tools/validate-yaml.py specs/doc.yaml specs/schema/spec-core.schema.yaml
```

## 12. 例外処理指針

* CIでProfile未参照・非対応要素を検出した場合は**警告止まり**とし、標準に違反しない。
* Schema検証で破壊的変更を検出した場合は**エラーとして停止**する。

---

# Part V. 付録（Annexes）

## Annex A. 最小Schema例（spec-core.schema.yaml）

```yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
title: "Spec Core Schema (Minimal Example)"
type: object
required: [identifier, name, version, date_published, sections]
properties:
  identifier:
    type: string
    pattern: "^G[0-9]{4}-[A-Z]{3,}-[A-Za-z0-9\\-]+$"
  name:
    type: string
  version:
    type: string
    pattern: "^v[0-9]+\\.[0-9]+\\.[0-9]+$"
  date_published:
    type: string
    format: date
  sections:
    type: object
    required: [objectives, requirements, constraints]
    properties:
      objectives:
        type: array
        items:
          type: object
          required: [id, text]
          properties:
            id: { type: string, pattern: "^OBJ-[0-9]+$" }
            text: { type: string }
      requirements:
        type: array
        items:
          type: object
          required: [id, type, text, priority]
          properties:
            id: { type: string, pattern: "^REQ-[0-9]+$" }
            type: { enum: ["functional", "nonfunctional"] }
            text: { type: string }
            priority: { enum: ["must", "should", "may"] }
      constraints:
        type: array
        items:
          type: object
          required: [id, text]
          properties:
            id: { type: string, pattern: "^CST-[0-9]+$" }
            text: { type: string }
```

## Annex B. テンプレート例（doc-template.yaml）

```yaml
$schema: "/specs/schema/spec-core.schema.yaml"
@context: "https://schema.org"
@type: "CreativeWork"
identifier: "<文書ID>"
name: "<文書名>"
version: "v0.1.0"
date_published: "<YYYY-MM-DD>"
in_language: ["ja"]
schema_version: "1.0"
sections:
  objectives: []
  requirements: []
  constraints: []
creator:
  @type: "Organization"
  name: "Documentation Team"
```

## Annex C. CIワークフロー例

```yaml
name: YAML Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Install tools
        run: pip install yamllint jsonschema
      - name: Validate YAML
        run: |
          yamllint specs/doc.yaml
          python tools/validate-yaml.py specs/doc.yaml specs/schema/spec-core.schema.yaml
```

---

## 結論

YAML文書構造を規定する正式標準として、G0400は以下の三層を中核とする：

1. **YAML（データ層）** – 構造を明示し、人間・AIが扱える形式。
2. **JSON Schema（形式層）** – 型と必須項目を保証。
3. **Schema.org（意味層）** – 文書の意味を明確化。

> 本標準は、Profileや運用層と独立して利用可能な**正式発行標準**であり、構造化・意味付け・検証を統合的に保証する。
