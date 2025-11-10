---

schema: "[https://schema.org/CreativeWork](https://schema.org/CreativeWork)"
"@type": "CreativeWork"
identifier: "G0110-STD-DOC1-AuthoringGuideline"
name: "Documentation Authoring Guideline (v1.1.0 / Authoring & Style Edition)"
version: "v1.1.0"
datePublished: "2025-11-11"
status: "Approved"
inLanguage: ["ja"]
creator:
"@type": "Person"
name: "Documentation Team"
description: "Defines writing and stylistic principles for all DocFoundary standard documents. Focuses on authoring methodology, content design, and stylistic consistency rather than structural format."
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 目次（Table of Contents）

* [1. 目的と適用範囲（Purpose and Scope）](#1-目的と適用範囲purpose-and-scope)

  * [1.1 目的](#11-目的)
  * [1.2 適用範囲](#12-適用範囲)
* [2. 記述設計の原則（Authoring Principles）](#2-記述設計の原則authoring-principles)

  * [2.1 構造的整合性（Structural Consistency）](#21-構造的整合性structural-consistency)
  * [2.2 内容設計（Content Design）](#22-内容設計content-design)
  * [2.3 品質基準（Quality Principles）](#23-品質基準quality-principles)
* [3. 表現・スタイルガイド（Stylistic Rules）](#3-表現スタイルガイドstylistic-rules)

  * [3.1 言語・文体ルール（Language and Tone）](#31-言語文体ルールlanguage-and-tone)
  * [3.2 構文と書式（Syntax and Formatting）](#32-構文と書式syntax-and-formatting)
  * [3.3 図表とコード記法（Figures and Code Notation）](#33-図表とコード記法figures-and-code-notation)
* [4. 管理・運用上の留意点（Management Notes）](#4-管理運用上の留意点management-notes)
* [5. 総括（Summary Directive）](#5-総括summary-directive)
* [附録A. 参考文書（Referenced Standards）](#附録a-参考文書referenced-standards)
* [Revision History（改訂履歴）](#revision-history改訂履歴)

# [STD-DOC1] 文書設計指針（Documentation Authoring Guideline / v1.1.0）

## 1. 目的と適用範囲（Purpose and Scope）

本指針は、DocFoundary 標準群における文書作成・記述・表現の統一を目的とする。
G0100-STD-DOCF（書式標準）が定義する構造・形式に対し、本書は**内容と文体の品質指針**を提供する。

### 1.1 目的

* 文書記述の一貫性・可読性・検証性を確保する。
* 曖昧さのない表現・文体・語彙使用を統一する。
* 文書構造に従いながらも、自然で再現性の高い著述を支援する。

### 1.2 適用範囲

* 対象：すべての DocFoundary 標準文書（OVR, REQ, ARC, OPS, SEC, RPT, REF 系）。
* 非対象：運用工程や自動検証手順など、構成外の技術的実装（G0101に委譲）。

---

## 2. 記述設計の原則（Authoring Principles）

### 2.1 構造的整合性（Structural Consistency）

* 文書は「目的 → 構造 → 表現 → 管理」の順で論理的に構成する（MUST）。
* 章番号体系（1〜6 + 附録）はG0100と一致させ、欠番を許可しない（MUST）。
* H1はタイトルのみ、H2は章、H3は節とする。H4以降の多段見出しは禁止（SHOULD NOT）。
* 各章は独立して理解できるよう構成し、他文書への過度な依存を避ける（SHOULD）。

### 2.2 内容設計（Content Design）

* 各章には明確な目的と完結した内容を持たせる（MUST）。
* 記述は具体的かつ検証可能であること。推測的・感想的な表現は禁止（MUST NOT）。
* 「例」「補足」「備考」は本文から分離し、適切に注記または附録に移す（SHOULD）。
* 図表・コード・用語の定義は G0100 の規定形式に従う（MUST）。

### 2.3 品質基準（Quality Principles）

* 曖昧な語（例：「すべき」「望ましい」）は使用せず、RFC2119用語（MUST / SHOULD / MAY）を用いる（MUST）。
* 各段落は100文字以内、1文は50文字以内を目安とし、簡潔な文を心がける（SHOULD）。
* 内容は検証可能（Verifiable）かつ再現可能（Reproducible）でなければならない（MUST）。
* 意味的重複・冗長表現を避け、最短で正確な文体を採用する（SHOULD）。

---

## 3. 表現・スタイルガイド（Stylistic Rules）

### 3.1 言語・文体ルール（Language and Tone）

* 日本語文体は「〜である」調に統一し、「〜です／ます」体は禁止（MUST）。
* 技術用語・英語表現はカタカナ語を避け、原語表記（英語）を優先する（SHOULD）。
* 英語副題は `(English Subtitle)` として全章に併記する（MUST）。
* 専門語・略語には初出時に括弧付き説明を付す（MUST）。

### 3.2 構文と書式（Syntax and Formatting）

* リスト記号は `-` に統一し、番号付きリストは手順説明に限る（SHOULD）。
* 引用は `>` 1段階まで許可、多段引用は禁止（MUST）。
* コードブロックは三重バッククォートで囲み、言語名を明示する（MUST）。
* 表はMarkdown標準構文を使用し、セル内改行や罫線の装飾は禁止（MUST）。
* 行末改行は「半角スペース2個＋LF」とする（MUST）。

### 3.3 図表とコード記法（Figures and Code Notation）

* Mermaid図表を使用する場合、G0100 5.2節（Mermaid記法）に準拠する（MUST）。
* 図表にはタイトル行（例：`%% 図3-1：構造概要`）を必ず記載する（MUST）。
* 図表番号・表番号は「図n-m」「表n-m」とし、章番号に連動（SHOULD）。
* コード例には動作保証を伴わない説明目的の注記を付す（SHOULD）。

---

## 4. 管理・運用上の留意点（Management Notes）

| 項目         | 内容                                           |
| ---------- | -------------------------------------------- |
| **改訂履歴**   | 改訂内容は文末の表に必ず記載し、降順に整理。                       |
| **レビュー工程** | 公開前に自己検証（DOCF-CHK）を実施。文体・構文の一貫性を確認。          |
| **参照更新**   | 附録Aの参照文書リストを改訂時に見直す。                         |
| **文体監査**   | 書式・表現の揺らぎを検出する自動Lintツール（例: markdownlint）を推奨。 |

---

## 5. 総括（Summary Directive）

> 本指針（G0110）は、G0100が定義する「構造と書式」の上に、
> **内容の明確性・表現の一貫性・記述品質の再現性** を保証するための著述基準を定義する。
> DocFoundary 標準文書は、**形式と内容の両輪**によって完全な統一性を保つ。

---

## 附録A. 参考文書（Referenced Standards）

| 文書ID                            | 名称        | 関係           |
| ------------------------------- | --------- | ------------ |
| G0100-STD-DOCF-FormatPolicy     | 書式標準      | 形式層基準        |
| G0101-STD-DOCL-LintPolicy       | 検証標準      | 予定文書（Lint仕様） |
| G0120-REF-DOCR-ReferenceSamples | 書式例・用語集   | 補助層          |
| G0410-STD-YML1-LayerModel       | YAML階層モデル | 構造層参照        |
| G0300-ARC-COD0-CodingStandard   | コーディング標準  | 設計層参照        |

---

## Revision History（改訂履歴）

| 版      | 日付           | 内容                                    |
| ------ | ------------ | ------------------------------------- |
| v1.1.0 | "2025-11-11" | 文書構成要素節をG0100へ委譲。記述原則とスタイルガイドを中心に再構成。 |
| v1.0.0 | "2025-11-11" | 初版作成。文書構成・内容・表現・品質管理の原則を定義。           |
