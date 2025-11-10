---

schema: "[https://schema.org/CreativeWork](https://schema.org/CreativeWork)"
@type: "CreativeWork"
identifier: "G0420-STD-YML2-SyntaxStyleGuide"
name: "YAML記述スタイル標準（YML2: Syntax Style Guide）"
version: "v1.2.1"
datePublished: "2025-11-09"
status: "Star5 Edition (Refined)"
inLanguage: ["ja"]
creator: "Documentation Team"
confidentiality: "Public"
glossary_ref: "G0100-STD-DOC0-Glossary"
description: "DocFoundary プロジェクトにおける YAML 記述スタイルの完全標準。コメント規則を統合し、Lint対応・Annex参照導線を追加。Glossary参照を明記し、章構成の明瞭性と保守性を向上。"
--------------------------------------------------------------------------------------------------------------------

# [STD-YML2] YAML記述スタイル標準（Syntax Style Guide） v1.2.1 / Star5 Edition (Refined)

> 本書は YAML 文書の書式統一を目的とする。G0400（構造仕様）および G0410（理念層）との整合を保ち、DocFoundary 全体での表記揺らぎを排除する。

---

## 1. 目的と適用範囲

* **目的**: YAML 文書の可読性・差分安定性・解析一貫性を最大化し、教育・CI検証にも適合させる。
* **適用範囲**: DocFoundary におけるすべての YAML 形式文書。
* **非対象**: 運用・CIルールは G0110 に委譲。

### 関連文書一覧

| 文書ID                             | 名称       | 関係 |
| -------------------------------- | -------- | -- |
| G0400-STD-YML0-ContentStructure  | YAML構造仕様 | 上位 |
| G0410-STD-YML1-LayerModel        | 三層モデル理念  | 上位 |
| G0110-STD-DOCO-OperationalPolicy | 運用規約     | 補助 |
| G0100-STD-DOC0-Glossary          | 共通用語集    | 参照 |

---

## 2. 基本原則（Principles）

* **P1 一貫性**: 同一リポジトリ内で常に同一ルールを適用する（MUST）。
* **P2 可読性**: 人間が素早く理解できる表記を優先する（SHOULD）。
* **P3 差分安定**: 小さな変更で最小の差分となる書き方を選ぶ（SHOULD）。
* **P4 シンプル**: 機能が重複する表現は一つに絞る（MUST）。

### 用語定義（MUST/SHOULD/MAY）

| 用語     | 意味                    |
| ------ | --------------------- |
| MUST   | 絶対に守らなければならない規則       |
| SHOULD | 強く推奨されるが、例外が許される場合がある |
| MAY    | 任意であり、状況に応じて判断できる     |

---

## 3. 文字・レイアウト

| 項目       | 規則                            | 根拠                                   |
| -------- | ----------------------------- | ------------------------------------ |
| 文字コード/改行 | UTF-8 / LF（MUST）              | クロスプラットフォーム互換（Annex B: line-length）  |
| インデント    | 半角スペース2（MUST）・タブ禁止            | 差分安定・可読性（Annex B: indentation）       |
| 行長       | 120列以内（MUST）                  | Lint対応、レビュー性向上（Annex B: line-length） |
| 末尾空白     | 禁止（MUST）                      | 差分安定（Annex B: trailing-spaces）       |
| 空行       | セクション間1行（MUST）、連続空行禁止（MUST）   | 表示統一・Lint適合（Annex B: empty-lines）    |
| コメント     | `#` の後に半角スペース（MUST）。詳細は第7章参照。 | 差分安定・可読性                             |

---

## 4. キー・命名・順序

| 項目     | 規則                                                                   | 例                               |
| ------ | -------------------------------------------------------------------- | ------------------------------- |
| キー命名   | `snake_case`（MUST）                                                   | `date_published`, `in_language` |
| ブール/ヌル | `true`/`false`（MUST）、`null` は原則禁止（MUST NOT）※テンプレート等でのみ許可（MAY、コメント必須） | `enabled: true`                 |
| 数値     | 先頭0禁止（MUST）、桁区切り禁止（MUST）                                             | `count: 1200`                   |
| 日付     | `YYYY-MM-DD`（MUST）                                                   | `date_published: "2025-11-09"`  |
| キー順    | 論理順を固定（SHOULD）: メタ → 本文 → 付録                                         | 構造理解の一貫性                        |

---

## 5. スカラー（文字列）の書き方

* **プレーンスカラー（無引用）**を優先（SHOULD）。
* スペースや記号、先頭/末尾空白、コロン `:` を含む場合は **ダブルクォート**（MUST）。
* 複数行テキストは **フォールドブロック `>`** を使用（SHOULD）。**リテラル `|` は詩・コードなど改行保持が必要な場合のみ使用（MAY）**。

---

## 6. 配列・マップの表現

| 項目       | 規則                   | 例                                          |
| -------- | -------------------- | ------------------------------------------ |
| 配列       | ブロック形式（MUST）         | `items:\n  - a\n  - b`                     |
| インライン配列  | 短いリストのみ許容（MAY、3要素以内） | `in_language: ["ja", "en"]`                |
| マップ      | キーは1行1項目（MUST）       | `creator:\n  @type: Person\n  name: Alice` |
| 空配列/空マップ | 原則禁止（SHOULD NOT）     | `items: []` は避ける                           |

---

## 7. コメント・ドキュメント性（統合版）

### 7.1 用途

* 行頭 `#` コメントは**説明**や**TODO**に使用（SHOULD）。
* 長文の注釈や出典はFront Matterまたは本文に記述（SHOULD）。

### 7.2 形式

* `#` の後には必ず半角スペース（MUST）。
* コメントは1行40文字以内（SHOULD）。
* キー末尾コメントは短文のみ（MUST）。

### 7.3 例

```yaml
# YAML文書の概要
name: Example
# TODO: 章3の参照を更新
version: "v1.2.1"  # コメントは40文字以内
```

---

## 8. セクション構成（DocFoundary既定）

> 論理順序は G0410 に従う。

* `objectives` → `requirements` → `constraints`（MUST）
* 各セクションは配列（MUST）。
* 要素IDの重複を避ける（MUST）。

---

## 9. 語彙の統一（最小セット）

* 作成者は `creator`（MUST）。
* 説明は `description`（MUST）。
* 発行日は **意味層**では `datePublished`、**データ/スキーマ層**では `date_published`（SHOULD）。

---

## 10. 例（OK/NG コレクション）

| 分類     | OK例                         | NG例                |
| ------ | --------------------------- | ------------------ |
| 引用記号   | `name: "YAML構造標準"`          | `name: 'YAML構造標準'` |
| 配列形式   | `- item1`                   | `[item1, item2]`   |
| 空行     | （セクション間1行）                  | （連続空行）             |
| コメント   | `# この行は40文字以内`              | `#コメント間にスペースなし`    |
| null扱い | （使用しない）                     | `value: null`      |
| 言語配列   | `in_language: ["ja", "en"]` | `in_language: ja`  |

> 詳細例および教育用テンプレートは Annex A を参照。

---

## 11. 互換性と拡張

* 本ガイドは DocFoundary の YAML 書式の完全標準（Star5 Edition）である。
* G0400/G0410 に矛盾する場合はそれらを優先（MUST）。
* 用語定義は G0100-STD-DOC0-Glossary を参照（MUST）。

---

## Annex A: 教育・実践例

### A-1 Front Matter完全構造例

```yaml
identifier: G0400-STD-YML0-ContentStructure
name: "YAML文書内容構造標準"
version: "v1.2.1"
date_published: "2025-11-09"
in_language: ["ja", "en"]
creator:
  @type: Organization
  name: Documentation Team
objectives:
  - id: OBJ-001
    text: YAML書式の完全統一
requirements:
  - id: REQ-001
    text: 末尾空白禁止
constraints:
  - id: CST-001
    text: null値の使用禁止
```

### A-2 多言語対応例

```yaml
in_language: ["ja", "en-US"]
name: "YAML Style Standard / YAML記述スタイル標準"
description: >
  This document defines YAML writing rules.\n  本書は YAML 記述ルールを定義する。
```

---

## Annex B: Lint設定例（推奨）

```yaml
extends: default
rules:
  line-length:
    max: 120
    level: warning
  trailing-spaces:
    level: error
  indentation:
    spaces: 2
    indent-sequences: consistent
  empty-lines:
    max: 1
    level: error
  comments:
    require-starting-space: true
```

---

## 付録C（参考）: 最小テンプレート

```yaml
identifier: <DOC_ID>
name: "<DOC_NAME>"
version: "vX.Y.Z"
date_published: "YYYY-MM-DD"
in_language: ["ja"]
creator:
  @type: Person
  name: "<Author Name>"
objectives: []
requirements: []
constraints: []
```
