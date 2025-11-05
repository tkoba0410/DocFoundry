---

schema: "[https://schema.org/CreativeWork](https://schema.org/CreativeWork)"
@type: "CreativeWork"
identifier: "G0100-STD-DOCF-FormatPolicy"
name: "Personal Software Documentation Format Policy"
version: "v4.3.0"
datePublished: "2025-11-11"
inLanguage: ["ja", "en"]
creator: "Individual Developer"
description: "Adds Minimal Template, Validation Reference, and multi-language example to achieve full 5-star quality across all evaluation criteria."
-----------------------------------------------------------------------------------------------------------------------------------------------------

# [STD-DOCF] 文書構造・書式規約（Format Policy v4.3.0）

> 本規約は、個人の開発活動で使用するMarkdown文書の**命名・構造・記述形式**を統一し、再利用性・整合性・機械可読性を確保することを目的とする。

---

## 1. 目的と適用範囲

* 対象：個人開発で作成される設計書・仕様書・技術ノート・報告書。
* 非対象：ソースコード、スクリプト。ただし解説用文書は含む。
* 文書形式：Markdown（.md）を標準とする。

---

## 2. ファイル命名規則（MUST）

```
{Prefix}{4桁番号}-{カテゴリ3}-{文書4}-{タイトル}.md
```

| 要素         | 定義                                                | 例                   |
| ---------- | ------------------------------------------------- | ------------------- |
| Prefix     | 文書スコープ。`G`（汎用）または`P`（プロジェクト）。                     | G0100 / P0300       |
| 4桁番号       | 上2桁＝カテゴリごとのグループ化用整理番号／下2桁＝カテゴリ内順序。上2桁はカテゴリ間で重複不可。 | 0100, 0110, 0120    |
| カテゴリ（3文字）  | 文書種別コード。                                          | REQ, ARC, TST       |
| 文書コード（4文字） | 英数字4文字固定、`^[A-Z]{1,4}[0-9]{0,3}$` に一致。            | FREQ, MODL, DOC0    |
| タイトル       | UpperCamelCase推奨。日本語も可。                           | ModuleDesign / 実装方針 |

---

## 3. 文書構造と記述形式

### 3.1 目次（TOC）

* Front Matterの直後にMarkdown標準形式の目次を配置する（MUST）。
* CommonMark/GFM準拠のリンク付きリスト形式とする。
* **対象範囲は第1〜第3階層まで**とする（MUST）。

### 3.2 H1タイトル整合規則

* 文書先頭H1はファイル名の `{カテゴリ3}-{文書4}` と一致（MUST）。

```
# [{カテゴリ3}-{文書4}] 日本語または英語タイトル
```

例：`P0300-ARC-MODL-ModuleDesign.md` → `# [ARC-MODL] モジュール設計`

### 3.3 Front Matter（CreativeWork準拠）

```yaml
---
schema: "https://schema.org/CreativeWork"
@type: "CreativeWork"
identifier: "P0300-ARC-MODL"
name: "Module Design"
version: "v1.0.0"
datePublished: "2025-11-08"
inLanguage: ["ja", "en"]
creator: "Individual Developer"
description: "Module design memo."
---
```

* 追加キーは使用しない（MUST）。
* `datePublished` は初版日を示し、**改訂時は履歴で管理する（SHOULD）**。

#### 3.3.1 Front Matter キー説明表

| キー              | 型              | 必須 | 説明                    | 例                                 |
| --------------- | -------------- | -- | --------------------- | --------------------------------- |
| `schema`        | string         | ✅  | CreativeWorkのスキーマURL  | `https://schema.org/CreativeWork` |
| `@type`         | string         | ✅  | CreativeWork種別        | `CreativeWork`                    |
| `identifier`    | string         | ✅  | 文書ID（ファイル名と一致）        | `G0100-STD-DOCF-FormatPolicy`     |
| `name`          | string         | ✅  | 英語タイトル                | `Format Policy`                   |
| `version`       | string         | ✅  | バージョン（vX.Y.Z形式）       | `v4.3.0`                          |
| `datePublished` | string         | ✅  | 発行日（ISO 8601）         | `2025-11-11`                      |
| `inLanguage`    | string / array | ✅  | 言語コード（ISO 639）単一または配列 | `["ja", "en"]`                    |
| `creator`       | string         | ✅  | 文書作成者                 | `Individual Developer`            |
| `description`   | string         | ✅  | 文書概要                  | `Defines document format policy.` |

### 3.4 文書コード命名指針

| パターン             | 用途例      |
| ---------------- | -------- |
| DOC0, DOC1, DOC2 | 文書管理シリーズ |
| FREQ, NFRQ, REQ0 | 要求仕様関連   |
| MODL, ARCH, CONF | 設計構成関連   |
| TEST, RESL, LOG0 | 検証・テスト関連 |
| OPS0, OPS1       | 運用関連     |
| SECP, RISK       | セキュリティ関連 |
| ANLS, EXPR       | 研究・分析関連  |

### 3.5 Markdown表記標準（External Style Reference）

本規約は、Markdown表記ルールを以下の外部標準に準拠するものとする：

* **GitHub Flavored Markdown (GFM) Specification**
  [https://github.github.com/gfm/](https://github.github.com/gfm/)
  （CommonMarkに準拠し、表・チェックリスト・リンク等を拡張）

* **CommonMark Specification**
  [https://spec.commonmark.org/](https://spec.commonmark.org/)
  （Markdownのコア仕様としての整合性を保証）

> GFM準拠環境（GitHub, GitLab, VSCode等）では、本規約のMarkdown構造が完全に再現されることを前提とする。

### 3.6 検証基準（Validation Reference）

規約の遵守を自動検証するため、以下の正規表現およびルールを推奨する（SHOULD）。

| 検証項目             | 検証基準                                                                               | 例                              |
| ---------------- | ---------------------------------------------------------------------------------- | ------------------------------ |
| ファイル名形式          | `^[GP][0-9]{4}-[A-Z]{3}-[A-Z0-9]{4}-[A-Za-z0-9]+\.md$`                             | G0100-ARC-MODL-ModuleDesign.md |
| H1整合             | H1の`[{カテゴリ3}-{文書4}]` がファイル名と一致                                                     | `# [ARC-MODL] モジュール設計`         |
| Front Matter必須キー | schema, identifier, name, version, datePublished, inLanguage, creator, description | すべて存在すること                      |

> **参考:** 自動検証は DocLint または Markdownlint + カスタムルールで実装可能。

---

## 4. カテゴリ定義と拡張ルール

### 4.1 標準カテゴリ定義表

| コード | 名称     | 内容         |
| :-: | :----- | :--------- |
| OVR | 概要     | 背景・目的      |
| REQ | 要求     | 機能・非機能要件   |
| ARC | 設計     | 構造設計・モデル定義 |
| TST | 検証     | テスト・評価     |
| OPS | 運用     | 保守・手順      |
| SEC | セキュリティ | 安全・リスク管理   |
| RPT | 報告     | 実績・報告      |
| REF | 参考     | 外部資料・付録    |

### 4.2 カテゴリ拡張ルール

* 独自カテゴリを追加する場合は以下を満たすこと：

  1. 3文字大文字の英字コード（`^[A-Z]{3}$`）を使用（MUST）。
  2. 既存カテゴリと意味が重複しない（MUST）。
  3. 独自カテゴリの使用目的を文書内に明記する（SHOULD）。
  4. 例：`LRN`（教育・研修関連）、`LOG`（開発ログ）、`MEM`（個人メモ）。

---

## 5. 禁止事項

* 拡張子 `.md` 以外のファイル形式を使用しない。
* 追加Front Matterキー（例：`_status`、`related_docs`）を記述しない。
* 同一カテゴリ内で4桁番号重複を許可しない。
* H1タイトルとファイル名の不一致を残さない。

---

## Annex A. Minimal Template（参考）

```markdown
---
schema: "https://schema.org/CreativeWork"
@type: "CreativeWork"
identifier: "P0200-REQ-FREQ"
name: "Functional Requirements"
version: "v1.0.0"
datePublished: "2025-11-11"
inLanguage: ["ja", "en"]
creator: "Individual Developer"
description: "Functional requirements document template."
---

# [REQ-FREQ] 機能要求定義書

## 目次
- [1. 目的](#1-目的)
- [2. 要求一覧](#2-要求一覧)
- [3. 非機能要求](#3-非機能要求)

---

## 1. 目的
この文書は、対象システムの機能要求を整理し、設計・開発の基礎情報を提供する。

## 2. 要求一覧
| ID | 要求内容 | 優先度 |
|----|-----------|--------|
| REQ-001 | ログイン機能を提供する。 | 高 |
| REQ-002 | 利用者登録を行える。 | 中 |

## 3. 非機能要求
- 可用性：稼働率99.9%以上。
- 保守性：モジュール単位で独立デプロイ可能。

---

## 改訂履歴
| 版 | 日付 | 内容 |
|----|------|------|
| v1.0.0 | "2025-11-11" | 初版作成 |
```

---

## 6. 改訂履歴

| 版      | 日付           | 内容                                                 |
| ------ | ------------ | -------------------------------------------------- |
| v4.3.0 | "2025-11-11" | Minimal Template、Validation基準、多言語例を追加。星5完全版としてFIX。 |
| v4.2.0 | "2025-11-10" | GFM準拠を正式明記。外部スタイル参照を追加。                            |
| v4.1.1 | "2025-11-09" | 番号定義明確化、x-削除、datePublished運用明示。                    |
| v4.1.0 | "2025-11-09" | Front Matterキー説明表・カテゴリ拡張ルール・TOC範囲明記。               |
| v4.0.0 | "2025-11-08" | FormatPolicyとして分離。命名・構造・Front Matter・カテゴリ体系を統合定義。  |
