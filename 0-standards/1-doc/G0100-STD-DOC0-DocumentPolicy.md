---
schema: "https://schema.org/CreativeWork"
doc_id: "G0100-STD-DOC0"
title: "Document Policy"
version: "2.3.5"
date: "2025-10-30"
status: "Approved"
owner: "Project Maintainer"
reviewers: ["Documentation Review Team"]
confidentiality: "Public"
scope: "Generic"
lifecycle: "Canonical"
description: "Defines universal document management structure."
---

# [STD-DOC0] 文書管理規約（汎用版）

## 1. 表紙情報
- 文書番号: `G0100-STD-DOC0`
- バージョン: **v2.3.1**
- 日付: 2025-10-15
- 状態: Approved

---

## 2. 目的と範囲
本書は、**あらゆるプロジェクト・組織活動における文書管理体系を標準化**し、  
分類・命名・番号体系・更新ルール・改訂履歴の統一を目的とする。

適用範囲はリポジトリ内の **`docs/` フォルダ以下の文書（Markdown形式）** とし、  
**ソースコードやツール（例: `src/`, `tools/`, `scripts/`）は本規約の適用外** とする。

本規約は特定の技術領域に限定されず、  
**ソフトウェア開発、製造、研究、運用管理など、多様な分野で再利用可能な汎用モデル**である。

> **個人識別情報（PII）非記載（MUST）**：
> すべての標準文書・テンプレート・出力物において、
> 氏名やアカウントID等の個人識別情報は記載しない。
> 役職名・チーム名などの**汎用ラベル**で代替すること。

---

## 3. 文書体系（Document Categories）

### 3.1 目的
本章は、文書を体系的に分類し、位置づけ・責務・参照関係を明確にする。  
以下のカテゴリは **開発プロジェクトにおける推奨構成** であり、  
同時に **他分野でも利用可能な汎用分類体系** として設計されている。

---

### 3.2 文書カテゴリ一覧（推奨構成）

| コード | 名称 | 主な内容・適用例 | 分野別適用例 |
|:--:|:--|:--|:--|
| **OVR** | 概要（Overview） | プロジェクトや業務全体像、背景、目的、対象範囲 | 事業計画書、研究概要書、設計総覧 |
| **REQ** | 要求（Requirements） | 要件・目的・制約条件・成果定義 | 要求仕様書、企画要件、研究仮説 |
| **ARC** | 構成設計（Architecture） | 構造設計、仕組み設計、関係構造 | システム構成図、業務フロー、研究モデル設計 |
| **IMP** | 実施・実装（Implementation） | 実施手順、方法、ルール、ガイドライン | 開発ガイド、実験手順書、作業要領書 |
| **TST** | 検証・評価（Testing） | 検証計画、品質確認、評価結果 | テスト仕様書、品質報告、検証記録 |
| **OPS** | 運用・管理（Operations） | 日常運用、手順、維持管理 | 運用マニュアル、保守手順書、日常点検要領 |
| **SEC** | 安全・セキュリティ（Security） | 安全確保、リスク管理、情報保護 | 情報セキュリティ方針、安全衛生計画 |
| **STD** | 標準・規約（Standards） | 開発・業務のルール、命名規則、手続き・運用ルール | コーディング規約、業務標準、運用基準 |
| **POL** | 方針（Policy） | 組織的方針、上位規範 | 品質方針、開発方針、倫理指針 |
| **RPT** | 報告（Report） | 実績・記録・成果報告 | 進捗報告書、研究報告書、監査報告書 |
| **REF** | 参考・外部資料（Reference） | 引用・付録・関連文献 | 法令引用、外部規格、付録資料 |

---

### 3.3 分野別適用例

| 分野 | 主カテゴリ構成例 | 補足 |
|------|------------------|------|
| **ソフトウェア開発** | OVR / REQ / ARC / IMP / TST / OPS / SEC / STD | 現行構成に準拠 |
| **製造業・工事業** | OVR / REQ / IMP / TST / OPS / STD / RPT | 工程設計〜検査・報告を一貫管理 |
| **研究開発** | OVR / REQ / ARC / IMP / TST / RPT / REF | 実験計画・モデル設計・検証・報告 |
| **組織運営・内部統制** | POL / STD / OPS / SEC / RPT / REF | 方針・運用・監査・法令対応 |

---

### 3.4 拡張原則
- 新たなカテゴリを追加する場合は **3文字大文字コード** を採用する。  
- 既存カテゴリと概念が重複しないよう命名する。  
- 汎用性を維持するため、可能な限り既存上位8カテゴリ（OVR〜STD）との整合を取る。  

---

### 3.5 カテゴリ選定指針
- 文書の**目的（伝える内容）**に基づき分類する。  
  - 例：計画を示すなら「OVR」または「REQ」  
  - 実施方法を示すなら「IMP」  
  - 成果を報告するなら「RPT」  
- **媒体（Markdown / PDF / Excel）やフォーマット**は分類対象外とする。  
- 複数カテゴリに跨る内容は**主目的に基づき主カテゴリを選定**し、副次的情報は章内で扱う。  

---

### 3.6 柔軟適用の例
- 開発チームでは「ARC」と「IMP」を統合して「Design（DSN）」を使用。  
- 経営層向けでは「POL」と「STD」を併合して「Governance（GVN）」を採用。  
- 教育・研修プロジェクトでは「OPS」を「Learning（LRN）」に置換可能。  

---

## 4. 文書番号体系

### 4.1 ファイル名フォーマット

```
{接頭子1文字}{4桁番号}-{カテゴリ3文字}-{文書4文字}-{タイトル}.md
```

#### 接頭子（Prefix）
| 接頭子 | 意味 | 対象例 |
|:--:|:--|:--|
| **G** | Generic（汎用標準） | G0100-STD-DOC0 |
| **P** | Project（プロジェクト固有） | P0210-REQ-FREQ |

> すべての文書は **接頭子を必須とし、省略を認めない。**  
> 使用可能な接頭子は **G または P のみ**。他の文字・接頭子は使用禁止。

#### 例
```
G0100-STD-DOC0-DocumentPolicy.md
G0160-STD-DOCS-StandardReusePolicy.md
P0210-REQ-FREQ-FunctionalRequirements.md
P0300-ARC-OVRV-ArchitectureOverview.md
P0400-IMP-GUID-ImplementationGuide.md
```

---

### 4.2 構造とルール

| 要素 | 桁数／形式 | 可変性 | 重複 | 内容／役割 |
|------|-------------|--------|------|-------------|
| **接頭子（Prefix）** | 1文字（G または P） | 🚫 不変 | 🚫 重複不可 | 文書スコープを識別。汎用標準＝G、プロジェクト標準＝P。省略不可。 |
| **4桁番号** | 上2桁＝大分類／下2桁＝論理順 | ✅ 可変 | 🚫 重複不可 | 文書の論理順序を表す。構成変更時に再番号可。 |
| **カテゴリ** | 3文字（OVR, REQ, ARC, …） | 🚫 不変 | 🚫 重複不可 | 文書の種別（概要、要件、設計など）を識別。 |
| **文書コード** | 4文字 | 🚫 原則固定／再利用可 | 🚫 同一時点で重複不可 | 識別子。廃止後は再利用可。 |
| **タイトル** | 任意（英語推奨） | ✅ 可変 | — | 英語キャメルケース（例：FunctionalRequirements）を推奨。 |

---

### 4.3 運用原則

1. **対象範囲**  
   - `docs/`配下のMarkdown文書のみを対象。  
   - `src/`・`tools/`・`scripts/`は対象外。

2. **番号の運用**  
   - 4桁番号は論理順序を示し、必要に応じて変更可。  
   - 同一番号の重複は禁止。

3. **識別子の一意性**  
   - `{カテゴリ}-{文書}` は論理的ID。  
   - 同カテゴリ内で一意であること。  
   - 文書削除後の再利用は可。  
   - 履歴はGit管理に委ね、過去版ファイルはリポジトリに残さない。

4. **削除・統合ルール**  
   - 廃止文書は `deprecated/` に残さず完全削除。  
   - 統合時は残存文書側に改訂履歴を引き継ぐ。

5. **タイトル命名規則**  
   - ファイル名は英語キャメルケース。  
   - 文書先頭（H1）タイトルは日本語可。  

6. **P→G 継承の明示**  
   - プロジェクト標準（P）文書が汎用標準（G）文書を継承する場合、Front Matter に次を記載する：  
     ```yaml
     inherit_from: G0100-STD-DOC0
     ```
---

### 4.4 H1タイトル形式

```
# [{カテゴリ3}-{文書4}] {タイトル（日本語可）}
```

例：
```
# [ARC-MODL] モジュール構成詳細
# [IMP-GUID] 実装ガイドライン
```

---

### 4.5 コードレジストリ例（運用参考）

| カテゴリ | コード | 名称 | 状態 | 備考 |
|-----------|--------|------|------|------|
| OVR | INTR | プロジェクト概要 | Approved | 必須文書 |
| REQ | FREQ | 機能要求定義 | Approved | 要求仕様 |
| ARC | MODL | モジュール構成 | Approved | 設計書 |
| IMP | GUID | 実装ガイド | Approved | 手順書 |
| STD | DOCS | 文書管理規約 | Approved | 本書 |

---

## 5. 更新・改訂ルール

- すべての変更は **改訂履歴テーブルに記録**する。  
- 改訂は **Pull Request または正式レビューを経て承認**すること（MUST）。  
- 4桁番号の変更は内容変更と同一コミットに含めないことを推奨。  
- バージョンは `vX.Y.Z` 形式とし、以下を原則とする：  
  - X：構造・体系変更（Breaking）  
  - Y：規約・定義追加（Minor）  
  - Z：文言修正・軽微変更（Patch）

---

### 5.1 Semantic Versioning 準拠方針

本規約およびすべての標準文書の版管理は  
[Semantic Versioning 2.0.0](https://semver.org/) の原則に準拠する。  

この方式では、文書を構成要素として「互換性のある／ない変更」を階層的に区別する：

| 区分 | 対応 | 説明 |
|------|------|------|
| **MAJOR (X)** | 構造・体系変更 | 章構成・ルール体系など、他文書との互換性を破壊する変更。 |
| **MINOR (Y)** | 規約・定義追加 | 新しい定義・ルール・手順を追加し、互換性を維持する変更。 |
| **PATCH (Z)** | 文言修正・軽微変更 | 表記・語句・体裁の修正であり、意味・互換性に影響しない変更。 |

この原則により、文書群の改訂履歴は他プロジェクトや外部標準と整合可能な  
**階層的構成管理（Hierarchical Configuration Control）** を実現する。

参考規格：
- [Semantic Versioning 2.0.0](https://semver.org/)
- ISO/IEC/IEEE 12207（ソフトウェアライフサイクルプロセス）
- ISO/IEC 26514（ユーザー文書構成指針）
- IEEE 828（構成管理標準）

---

### 5.2 文書状態とライフサイクルの関係（新設）

> **補足：用語整備 — status / lifecycle 段階差定義**

文書には、承認段階を示す `status` と、成熟度段階を示す `lifecycle` がある。  
両者の関係は以下の通りとする：

| 区分 | フィールド | 値 | 意味 | 主な使用段階 |
|------|-------------|----|------|----------------|
| **状態（承認レベル）** | `status` | `"Draft"` | 下書き。正式レビュー前段階。 | 作成中文書 |
| |  | `"Approved"` | 正式承認済。内容が安定し、公開可能。 | 安定運用文書 |
| |  | `"Deprecated"` | 廃止予定または無効化済。 | 移行・削除前 |
| **成熟度（ライフサイクル段階）** | `lifecycle` | `"Draft"` | 作成・試行段階。 | 新規作成時 |
| |  | `"Stable"` | 内容が安定し、他文書から参照可能。 | 継続運用時 |
| |  | `"Canonical"` | 標準体系の中核を構成。バージョン付与・継承対象。 | 永続規範文書 |

> 両者の併用例：
> - 初稿作成時：`status: "Draft"`, `lifecycle: "Draft"`
> - 承認後、安定運用時：`status: "Approved"`, `lifecycle: "Stable"`
> - 長期基準化後：`status: "Approved"`, `lifecycle: "Canonical"`

---

## 6. Front Matter（必須）

本規約では、すべての文書の冒頭に **YAML Front Matter を必ず設けること（MUST）**。  
その内容は以下の **Document Configuration Metadata Model（DCMM）** に準拠する。  

本モデルは以下の国際標準およびWeb標準に基づく：  
- ISO/IEC 26514（ユーザー文書構成）  
- IEEE 828（構成管理標準）  
- ISO/IEC 27001 Annex A.5.32（情報分類）  
- Semantic Versioning 2.0.0（バージョン管理）  
- schema.org/CreativeWork（Webメタデータモデル）

---

### 6.1 必須キーセット（DCMM仕様）

> **互換性注記（MUST）**：YAML解析器間の挙動差異を避けるため、  
> Front Matter の **全ての値をダブルクォート（"..."）で囲むこと**。  
> 例：`"Public"`, `"Canonical"`, `"2025-10-15"`, `["Documentation Review Team"]`。

| キー | 必須 | 型 | 出典 | 説明 | 例 |
|------|------|----|------|------|----|
| `schema` | ⬜ 推奨 | string | schema.org | 構造定義スキーマURL | `"https://schema.org/CreativeWork"` |
| `doc_id` | ✅ | string | IEEE 828 / ISO 26514 | 文書ID（一意識別子、接頭子を含む） | `"G0100-STD-DOC0"` |
| `title` | ✅ | string | ISO 26514 | 文書タイトル（英語推奨） | `"Document Policy"` |
| `version` | ✅ | string | SemVer 2.0.0 | バージョン（`vX.Y.Z`形式） | `"2.3.1"` |
| `date` | ✅ | string | ISO 8601 / ISO 26514 | 発行日（`YYYY-MM-DD`形式） | `"2025-10-15"` |
| `status` | ✅ | enum | IEEE 828 | 文書状態（`Draft` / `Approved` / `Deprecated`） | `"Approved"` |
| `owner` | ✅ | string | ISO 26514 | 文書責任者（役職またはチーム名） | `"Project Maintainer"` |
| `reviewers` | ✅ | list[string] | ISO 26514 / 12207 | レビュワー（複数可） | `["Documentation Review Team"]` |
| `confidentiality` | ✅ | enum | ISO 27001 | 機密区分（`Public` / `Internal` / `Confidential`） | `"Public"` |
| `scope` | ✅ | enum | STD-DOCS内部定義 | 適用範囲（`Generic` / `Project`） | `"Generic"` |
| `lifecycle` | ✅ | enum | STD-DOCS内部定義 | 文書成熟度（`Draft` / `Stable` / `Canonical`） | `"Canonical"` |
| `inherit_from` | ⬜ 任意 | string | STD-DOCS拡張 | 継承元文書ID | `"G0100-STD-DOC0"` |
| `description` | ⬜ 任意 | string | schema.org | 文書概要 | `"Defines universal document management structure"` |
| `related_docs` | ⬜ 推奨 | list[string] | STD-DOCS拡張 | 参照関係にある文書IDの配列 | `["G0200-STD-SCD0-CycleGuide","G0210-STD-DVT0-Templates"]` |

> **補足（Schema参照）**：  
> DCMM の検証は JSON Schema (Draft 2020-12) に基づく。  
> 最新スキーマは次のファイルとして管理する：  
> ```
> /schemas/dcmm.schema.json
> ```
> CI システムおよび IDE 補完は本スキーマを参照すること。  
> 本文ではスキーマ定義を内包せず、外部参照により肥大化を防止する。

---

### 6.2 記述例（標準形）

```yaml
---
schema: "https://schema.org/CreativeWork"
doc_id: "G0100-STD-DOC0"
title: "Document Policy"
version: "2.3.3"
date: "2025-10-21"
status: "Approved"
owner: "Project Maintainer"
reviewers: ["Documentation Review Team"]
confidentiality: "Public"
scope: "Generic"
lifecycle: "Canonical"
description: "Defines universal document management structure."
---
```

#### 参照文書付きの例（拡張）
```yaml
---
schema: "https://schema.org/CreativeWork"
doc_id: "G0100-STD-DOC0"
title: "Document Policy"
version: "2.3.3"
date: "2025-10-21"
status: "Approved"
owner: "Project Maintainer"
reviewers: ["Documentation Review Team"]
confidentiality: "Public"
scope: "Generic"
lifecycle: "Canonical"
description: "Defines universal document management structure."
related_docs: ["G0200-STD-SCD0-CycleGuide","G0210-STD-DVT0-Templates","G0220-STD-DEVP-OpsIntegrationGuide"]
---
```

> Front Matter の内容は CI により自動検証される。  
> すべてのドキュメントは DCMM 仕様に準拠していなければならない。  
> `owner` および `reviewers` には実名を用いず、**役職またはチーム名のみを記載すること（MUST）**。
> 文書本文・表・図・付録・メタデータ全体でも **個人名・アカウントID等のPIIを記載しない（MUST）**。

---

### 6.3 適用と拡張

- 各プロジェクトは DCMM を継承し、必要に応じてプロジェクト固有のキーを追加できる。  
- 汎用性維持のため、追加キーは `x-` 接頭子を付与すること（例：`x-department`）。  
- CI では、DCMM必須キーが欠落した文書をエラーとみなす。

---

## 7. 改訂履歴
| 版 | 日付 | 内容 |
|----|------|------|
| v2.2.1 | "2025-10-15" | 接頭子体系統合・構成簡略化 |
| v2.2.2 | "2025-10-15" | Semantic Versioning準拠方針を明記 |
| v2.2.3 | "2025-10-15" | Front Matter必須化 |
| v2.3.0 | "2025-10-15" | DCMM正式統合。国際標準・schema.org整合化。 |
| **v2.3.1** | "2025-10-15" | Front Matter値の**全面ダブルクォート化（MUST）**を明記し、CI互換性を強化。 |
| **v2.3.2** | "2025-10-15" | G0160 Standard Reuse Policy を統合。G/P昇格ルールを §4.3 に正式追加。 |
| **v2.3.3** | "2025-10-21" | Rolling Conformance方針への整合、PII非記載（MUST）を明文化、`related_docs`をDCMMに追加。 |
| **v2.3.4** | "2025-10-23" | `status` と `lifecycle` の関係表を追加（§5.2）。<br>DCMM Schema 外部参照ルールを §6.1 に追記。 |
| **v2.3.5** | "2025-10-30" | status値修正とscope統一に伴う軽微整合更新 |

---
