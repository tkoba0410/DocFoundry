---

schema: "[https://schema.org/CreativeWork](https://schema.org/CreativeWork)"
"@type": "CreativeWork"
identifier: "G0100-STD-DOC0-FormatPolicy"
name: "Documentation Format Standard (v5.6.0 / Final Logical Edition)"
version: "v5.6.0"
datePublished: "2025-11-11"
status: "Approved"
inLanguage: ["ja"]
creator: "Person"
description: >
  Final logical edition of the DocFoundary Format Standard.
  Defines structure, taxonomy, naming, metadata, and Markdown formatting rules in coherent logical order.
-------------------------------------------------------------------------------------------------------

# [STD-DOC0] ドキュメント書式標準（Documentation Format Standard / v5.6.0）

## 目次（Table of Contents）

* [1. 定義と適用範囲](#1-定義と適用範囲definition-and-scope)
* [2. 文書体系とカテゴリ構造](#2-文書体系とカテゴリ構造document-taxonomy-and-category-model)
* [3. ファイル命名規則](#3-ファイル命名規則naming-convention)
* [4. 文書構造とメタデータ](#4-文書構造とメタデータstructure--metadata)

  * [4.1 目次](#41-目次table-of-contents)
  * [4.2 Front Matter構造](#42-front-matter構造creativework-schema)
  * [4.3 Front Matter固定仕様](#43-front-matter固定仕様error-free-form)
  * [4.4 バージョンと改訂履歴](#44-バージョンと改訂履歴versioning--revision-history)
* [5. Markdown書式標準](#5-markdown書式標準markdown-formatting-standard)

  * [5.1 表記詳細ルール](#51-表記詳細ルールformatting-details)
* [6. 禁止事項](#6-禁止事項prohibited-items)
* [附録A. 参照文書](#附録a-参照文書referenced-standards)
* [Revision History](#revision-historyrevision-history)

---

## 1. 定義と適用範囲（definition-and-scope）

本標準は、DocFoundary 標準群における **Markdown 文書の形式層仕様** を定義する。
文書の意味や運用手順ではなく、その **構造・命名・書式** を統一し、再現性と整合性を保証することを目的とする。

### 1.1 目的（purpose）

DocFoundary 全体で共通利用される Markdown 文書の形式を標準化し、GFM / CommonMark 準拠の書式に統一する。
また、本標準は全標準群に共通する **形式層（Format Layer）** の基盤仕様として位置づけられる。

### 1.2 適用範囲（scope-of-application）

* **対象**：設計書、仕様書、報告書など Markdown で作成される開発文書。
* **非対象**：ソースコードやスクリプト。ただし解説用文書は含む。
* **位置付け**：本標準は G0000-STD-OVRV（理念層）と G0400-STD-YML0（構造層）の間に位置し、両層を接続する **形式層（Format Layer）** に属する。

---

## 2. 文書体系とカテゴリ構造（document-taxonomy-and-category-model）

本章では、DocFoundary 標準群で使用されるカテゴリ、ステータス、および言語コードを定義する。
これらは文書構造の基本分類として本文内で正式に定義され、別レジストリ文書（G0121）への参照は不要である。

### 2.1 Categories（カテゴリ定義）

| コード | 名称                         | 用途概要                 | 代表文書例                                 |
| :-: | :------------------------- | :------------------- | :------------------------------------ |
| OVR | 概要（Overview）               | 背景・目的・原則・上位方針を定義する文書 | G0000-STD-OVRV-Overview               |
| REQ | 要求仕様（Requirements）         | 機能・非機能要求を定義する文書      | G0200-REQ-REQF-FunctionalRequirements |
| ARC | 設計書（Architecture / Design） | システム構成・モジュール・API定義   | G0300-ARC-COD0-CodingStandard         |
| TST | 試験仕様（Test / Validation）    | テスト方針・手順・結果を記述する文書   | G0500-TST-TSTP-TestPlan               |
| OPS | 運用（Operations）             | 手順・運用方針・保守を規定する文書    | G0110-OPS-DOCO-OperationalPolicy      |
| SEC | セキュリティ（Security）           | リスク・対策・権限管理を扱う文書     | G0600-SEC-SECP-SecurityPolicy         |
| RPT | 報告書（Report）                | 実施結果・評価・総括をまとめる文書    | G0700-RPT-RPTA-AnalysisReport         |
| REF | 参考資料（Reference）            | 用語集・例示・補足資料を提供する文書   | G0120-REF-DOCR-ReferenceSamples       |

### 2.2 Status（文書状態）

DocFoundary 標準群では、文書状態（status）は **Draft** と **Approved** のみを公式値（MUST）とする。
他の状態（Reviewing, Deprecated など）は運用層（OPS）で扱う。

| 値        | 意味          | 用途例               |
| -------- | ----------- | ----------------- |
| Draft    | 作成中・承認待ちの文書 | 新規作成時、改訂中の文書      |
| Approved | 承認済み・安定版    | 公開および他文書からの参照可能状態 |

### 2.3 Language Codes（言語コード）

DocFoundary 標準群では、**日本語（`ja`）を唯一の公式言語コード（MUST）** とする。
他言語（例：`en`, `ko`, `zh`）は補助翻訳用として扱い、文書の正本としては認めない。

| コード | 言語名 | 用途概要                |
| :-: | :-- | :------------------ |
|  ja | 日本語 | すべての標準文書の基準言語（MUST） |

> **注:** `inLanguage` は `["ja"]` を必須とし、翻訳版を作成する場合のみ補助的に追加できる（例：`["ja", "en"]`）。
> 翻訳文書は「参考（Reference）」カテゴリ扱いとする。

---

## 3. ファイル命名規則（naming-convention）

```
{Prefix}{4桁番号}-{カテゴリ3}-{文書4}-{タイトル}.md
```

| 要素             | 定義                                            | 例                   |
| -------------- | --------------------------------------------- | ------------------- |
| **Prefix**     | 文書スコープ。`G`（汎用）または`P`（プロジェクト）。                 | G0100 / P0300       |
| **4桁番号**       | 上2桁＝カテゴリ群番号／下2桁＝カテゴリ内順序。                      | 0100, 0110          |
| **カテゴリ（3文字）**  | 文書種別コード（例：REQ, ARC, OPS）。                     | REQ                 |
| **文書コード（4文字）** | 英大文字＋数字4桁以内（例示正規表現 `^[A-Z]{1,4}[0-9]{0,3}$`）。 | DOC0, MODL          |
| **タイトル**       | UpperCamelCase推奨。日本語も可。                       | FormatPolicy / 実装方針 |

---

## 4. 文書構造とメタデータ（structure--metadata）

### 4.1 目次（table-of-contents）

目次（TOC: Table of Contents）は、文書全体の構造を示すために設ける。
DocFoundary標準文書では、以下の要件を満たさなければならない（MUST）。

#### (1) 配置位置

* **Front Matter の直後、タイトル行（H1）の直後に配置する（MUST）**。
* 目次より前に他の要素（段落・注記・画像など）を置いてはならない（MUST NOT）。
* 目次は「章構成の一覧」であり、本文の一部ではなく**構造要素（format element）**として扱う。

#### (2) 構文形式

* **Markdown標準（CommonMark / GFM）準拠のリンク付きリスト形式（MUST）**とする。
* リスト階層は**第1〜第3階層まで**に限定する（MUST）。
* 各項目は `[章タイトル](#アンカー名)` の形式で記述する。

#### (3) アンカー命名

* 章タイトルの日本語と英語副題を**小文字＋ハイフン連結**で組み合わせる（MUST）。
  例：`#3-文書構造と-front-matterdocument-structure-and-metadata`
* 半角英数字とハイフン以外の文字を含めてはならない（MUST NOT）。
* タイトル変更時は対応するアンカーも更新する（SHOULD）。

#### (4) 対象範囲

* 目次は**第1章から附録および改訂履歴まで**を対象とする（MUST）。
* 自動生成を行う場合でも、記述順序・階層は本文構造と一致していなければならない（MUST）。

> **要旨:**
> 目次は、文書の章構成を正確に反映する**固定構文ブロック**であり、
> 生成方法やツールに依存しない最小限の書式で定義する。

### 4.2 Front Matter構造（creativework-schema）

| キー              | 型      | 必須 | 説明                                          |
| --------------- | ------ | -- | ------------------------------------------- |
| `schema`        | string | ✅  | スキーマURL (`https://schema.org/CreativeWork`) |
| `@type`         | string | ✅  | CreativeWork種別                              |
| `identifier`    | string | ✅  | 文書ID（ファイル名と一致）                              |
| `name`          | string | ✅  | 英語タイトル                                      |
| `version`       | string | ✅  | バージョン (`vX.Y.Z`)                            |
| `datePublished` | string | ✅  | 発行日 (ISO 8601)                              |
| `status`        | string | ✅  | 文書状態 (例: Draft / Approved)                  |
| `inLanguage`    | array  | ✅  | 言語コード (ISO 639)                             |
| `creator`       | object | ✅  | JSON-LD形式（Person または Organization）          |
| `description`   | string | ✅  | 文書概要                                        |

### 4.3 Front Matter固定仕様（error-free-form）

Front Matter は **唯一の固定構文**に従う。
この形式以外はサポート対象外とし、CI・Lint すべてで同一結果を保証する。

```yaml
---
schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0100-STD-DOC0-FormatPolicy"
name: "Documentation Format Standard"
version: "v5.6.0"
datePublished: "2025-11-11"
status: "Approved"
inLanguage: ["ja"]
creator:
  "@type": "Person"
  name: "Individual Developer"
description: "Core format specification with error-free YAML header."
---
```

### 4.4 バージョンと改訂履歴（versioning--revision-history）

#### (1) バージョン表記

* Semantic Versioning (`vX.Y.Z`) に準拠。
* MAJOR／MINOR／PATCH を明確に区別し、Front Matter・表紙・履歴表で同一値を保持する。

#### (2) 改訂履歴表書式

| 版      | 日付           | 内容   |
| ------ | ------------ | ---- |
| v1.0.0 | "2025-11-11" | 初版作成 |

* 列構成は **版・日付・内容** の3列固定。
* 記録順序は降順（最新が上位）。
* 日付形式は ISO 8601（YYYY-MM-DD）。

---

## 5. Markdown書式標準（markdown-formatting-standard）

**準拠仕様:**

* GitHub Flavored Markdown (GFM)
* CommonMark Specification

> これらの仕様に準拠し、主要エディタ（VS Code, GitHub, GitLab 等）で完全再現可能であることを前提とする。

### 5.1 表記詳細ルール（formatting-details）

本標準で定義する Markdown 書式の詳細要件は、すべての DocFoundary 標準文書に共通して適用される。
いかなる場合も、次のルールに準拠しなければならない（MUST）。

| 区分                                 | 要件                                                        | 規範性                                            |      |
| ---------------------------------- | --------------------------------------------------------- | ---------------------------------------------- | ---- |
| **表（Tables）**                      | `                                                         | ` 罫線による標準Markdown表を用い、セル内改行は禁止。外枠線や結合セルは使用しない。 | MUST |
| **コードブロック（Code Blocks）**           | 三重バッククォートで囲み、必ず言語名を指定する（例：`yaml / `csharp）。               | MUST                                           |      |
| **引用（Blockquote）**                 | `>` は1段階のみ許可。多段引用は禁止。引用中に他要素（表・画像）を含めない。                  | MUST                                           |      |
| **日付・時刻（Date and Time）**           | ISO 8601形式（例: `2025-11-11`、`2025-11-11T10:00:00Z`）を使用。    | MUST                                           |      |
| **改行（Line Breaks）**                | 段落改行は半角スペース2個＋LF。ハードラップや自動折り返しは禁止。                        | MUST                                           |      |
| **画像・図表（Images and Figures）**      | `![alt text](path)` 形式を用い、alt属性は必須。タイトルは任意。画像の横幅・整列指定は禁止。 | MUST                                           |      |
| **内部リンク（Internal Links）**          | 同一文書内は `#アンカー名` 形式を使用。アンカー名は小文字＋ハイフンで統一。                  | MUST                                           |      |
| **外部リンク（External References）**     | 他標準文書へのリンクは `Gxxxx-XXX-YYYY#節名` の完全形式で記述。                 | MUST                                           |      |
| **脚注（Footnotes）**                  | CommonMark拡張構文 `[^1]` を使用。1階層構造に限定し、本文中で参照しやすい位置に置く。      | SHOULD                                         |      |
| **文書ID参照（Document ID References）** | 文書IDは完全形式（例：`G0300-ARC-COD0`）を用い、省略や略号表現は禁止。              | MUST                                           |      |

> **注:**
> これらの書式定義は、DocFoundary 標準群の**最小単位の表現仕様**であり、
> PDF / HTML / YAML など他形式へ変換しても再現性が損なわれないことを保証する。

### 5.2 図表記法（diagram-notation--mermaid）

DocFoundary 標準群では、シーケンス図、フローチャート、ER図、クラス図などの視覚表現を **Mermaid 記法**（[https://mermaid.js.org](https://mermaid.js.org)）により記述することを推奨する（SHOULD）。

#### (1) 基本方針

* 図表は **Markdownコードブロック内で `mermaid` 言語指定を行う（MUST）**。

  ````
  ```mermaid
  graph TD
    A[開始] --> B{条件}
    B -->|Yes| C[処理1]
    B -->|No| D[処理2]
  ````

  ```
  ```
* Mermaid は CommonMark 拡張の一部として扱い、**GFM 互換環境で再現可能な範囲**に限定する（MUST）。
* Mermaidブロック内では、改行・インデントを厳守し、外部スタイルシートやJavaScript呼び出しを埋め込んではならない（MUST NOT）。

#### (2) 図表の種類と用途

| 図種                           | 用途                 | 記法例                       |
| ---------------------------- | ------------------ | ------------------------- |
| **Flowchart（フローチャート）**       | 手順・処理フローの説明        | `graph TD` または `graph LR` |
| **Sequence Diagram（シーケンス図）** | API呼び出し・イベントの時系列表示 | `sequenceDiagram`         |
| **Class Diagram（クラス図）**      | 型・関係性の整理           | `classDiagram`            |
| **ER Diagram（ER図）**          | データ構造・リレーションの可視化   | `erDiagram`               |
| **Gantt Chart（ガント図）**        | スケジュールや工程の概要       | `gantt`                   |

#### (3) 表示要件

* すべての図表は **テキスト構造として保存可能であること（MUST）**。図の画像出力や外部リンク形式は禁止（MUST NOT）。
* 図表には **タイトル行（コメント形式）を先頭に記載**する（SHOULD）。

  ````
  ```mermaid
  %% 図1：処理フロー概要
  graph TD
    Start --> Process
  ````

  ```
  ```
* 文書中の図表は **章番号連動形式**で参照する（例：「図4-1」「図5-2」）。

#### (4) 他形式出力時の互換性

* Mermaid 記法は **HTML / PDF / Structurizr YAML 変換時に保持されることを前提**とする（SHOULD）。
* CI / 自動出力環境では、`mmdc`（Mermaid CLI）または `PlantUML`互換変換での自動図出力を推奨。

> **注:**
> Mermaid 記法は DocFoundary 標準群における **唯一のテキストベース図表形式**であり、
> YAML 層（G0410）・設計層（ARC）で共通運用される。

---

---

## 6. 禁止事項（prohibited-items）

* `.md` 以外の拡張子を使用しない。
* 非標準キーを Front Matter に追加しない（`status` を除く）。
* 同一カテゴリ内で4桁番号を重複させない。
* H1タイトルとファイル名を不一致のままにしない。

---

## 附録A. 参照文書（referenced-standards）

| 文書ID                               | 名称           | 関係        |
| ---------------------------------- | ------------ | --------- |
| G0000-STD-OVRV-OverView            | ドキュメント標準全体指針 | 上位理念層     |
| G0400-STD-YML0-ContentStructure    | YAML内容構造標準   | 下位構造層     |
| G0410-STD-YML1-LayerModel          | YAML階層モデル標準  | 関連構造層     |
| G0120-REF-DOCR-ReferenceSamples    | 書式例・用語集      | 補助層       |
| G0121-STD-REG-DocumentEnumerations | 列挙レジストリ      | 列挙原本層     |
| G0300-ARC-COD0-CodingStandard      | コーディング標準     | 設計層参照     |
| G0600-SEC-SECP-SecurityPolicy      | セキュリティ標準     | セキュリティ層参照 |

> **注:**
> 参照文書は、DocFoundary 標準群の上位・下位・横断的関連を示すものであり、
> 改訂履歴・カテゴリ更新により自動的に参照関係が更新される。

---

## Revision History（revision-history）

| 版             | 日付           | 内容                                                |
| ------------- | ------------ | ------------------------------------------------- |
| v5.7.1        | "2025-11-11" | 附録Aおよび改訂履歴を完全展開。G0410およびG0300参照を追加。               |
| v5.7.0        | "2025-11-11" | Mermaid図表記法（5.2節）を追加し、テキストベース図表形式を正式定義。           |
| v5.6.0        | "2025-11-11" | 章構成を論理整合順に再構成し、Front Matter・改訂履歴・Markdown書式を整理統合。 |
| v5.5.0        | "2025-11-11" | 表記詳細ルールを追加し、Markdown表現仕様を完全定義。                    |
| v5.4.0        | "2025-11-11" | 目次をタイトル直後に移動。TOC整合を確立。                            |
| v5.3.0〜v5.3.2 | "2025-11-11" | 見出し整合・カテゴリ体系統一・構造順再整理。                            |
| v5.0.0〜v5.2.1 | "2025-11-11" | DOC0統合版の初期設計・安定化。                                 |
