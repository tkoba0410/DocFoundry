---

schema: "[https://schema.org/CreativeWork](https://schema.org/CreativeWork)"
@type: "CreativeWork"
identifier: "G0000-STD-OVRV-OverView"
name: "Documentation Standard – General Overview (Canonical Edition)"
version: "v1.1.0"
datePublished: "2025-11-09"
status: "Canonical Edition (Refined)"
creator:
@type: "Person"
name: "Individual Developer"
inLanguage: ["ja", "en"]
confidentiality: "Public"
description: >
Defines governance and structural principles for all documentation standards within DocFoundary.
Canonical Edition integrates common policies: version governance, terminology unification,
confidentiality classes, external standards, and unified layer map.
-------------------------------------------------------------------

# [STD-OVRV] ドキュメント標準全体指針（Documentation Standard – General Overview / Canonical Edition）

> 本書は、DocFoundary の全標準群（G0100〜G04xx）を統括する上位指針として、
> 個人開発を基本単位とする運用理念・体系構造・適用範囲を定義し、共通原則を統合する。

---

## 目次

* [1. 目的と位置付け](#1-目的と位置付け)
* [2. 基本理念と共通原則](#2-基本理念と共通原則)

  * [2.1 用語定義（Glossary Reference）](#21-用語定義glossary-reference)
  * [2.2 共通バージョン管理原則](#22-共通バージョン管理原則)
  * [2.3 情報分類（Confidentiality Classes）](#23-情報分類confidentiality-classes)
  * [2.4 用語統一方針（Terminology Governance）](#24-用語統一方針terminology-governance)
* [3. 構成体系（Standard Hierarchy）](#3-構成体系standard-hierarchy)
* [4. 運用分離方針（Operational Separation）](#4-運用分離方針operational-separation)
* [5. 適用範囲と改訂責務モデル](#5-適用範囲と改訂責務モデル)
* [6. 外部準拠仕様（External References）](#6-外部準拠仕様external-references)
* [Annex A. 統合層マップ](#annex-a-統合層マップ)
* [7. 改訂履歴](#7-改訂履歴)

---

## 1. 目的と位置付け

本書は、DocFoundaryにおける**標準文書体系の最上位レイヤ（L0）**として、
各規約の位置付けと共通方針を明示し、全体整合性を維持する。

* 開発対象：個人または小規模チームによる技術開発・記録活動。
* 非対象：商用製品ドキュメント・企業内文書体系。
* 本標準群の最上位に位置し、すべての文書運用・構造定義・改訂方針の共通理念を提供する。

---

## 2. 基本理念と共通原則

### 2.1 用語定義（Glossary Reference）

| 用語                                  | 定義                            | 補足                   |
| :---------------------------------- | :---------------------------- | :------------------- |
| **個人開発（Personal Development）**      | 営利目的を伴わない自己管理下の技術活動。          | OSS・教育・研究・試作を含む。     |
| **標準群（Standard Set）**               | DocFoundary における全ての STD 文書体系。 | G0100〜G04xxを含む。      |
| **静的基準（Static Standard）**           | 書式・構造を定義する不変要素。               | G0100 / G0400〜G0420。 |
| **動的基準（Dynamic Standard）**          | 運用・検証・改訂を定義する要素。              | G0110 / CI運用設定。      |
| **責務分離（Responsibility Separation）** | 静的設計と動的運用を明確に分ける方針。           | CIとの整合性確保。           |

---

### 2.2 共通バージョン管理原則

* すべての標準文書は **Semantic Versioning 2.0.0** に準拠する。
* `MAJOR` 構造変更、`MINOR` 内容追加、`PATCH` 軽微修正を示す。
* Front Matter・表紙・改訂履歴表でバージョン番号を一致させる（MUST）。
* 改訂履歴は `版・日付・内容` の3列表形式で記載する（MUST）。

---

### 2.3 情報分類（Confidentiality Classes）

| 区分           | 意味   | 例                 |
| :----------- | :--- | :---------------- |
| Public       | 公開文書 | GitHub・Web公開可     |
| Internal     | 内部資料 | 非公開の個人メモ・ドラフト     |
| Confidential | 機密文書 | 個人情報・商用情報を含む非公開資料 |

---

### 2.4 用語統一方針（Terminology Governance）

以下のキー語彙は体系全体で統一する（MUST）。

| 意味  | 採用キー                           | 非推奨キー             |
| :-- | :----------------------------- | :---------------- |
| 発行日 | datePublished / date_published | date              |
| 作成者 | creator                        | author, editor    |
| 説明  | description                    | summary, abstract |

---

## 3. 構成体系（Standard Hierarchy）

|            レイヤ            | 文書群                  | 主題                | 代表文書                             |
| :-----------------------: | :------------------- | :---------------- | :------------------------------- |
|      **L0: Overview**     | 体系全体指針               | 標準群の理念・位置付け       | G0000-STD-OVRV-OverView（本書）      |
|       **L1: Format**      | 文書構造・命名・Front Matter | 書式・命名・構成          | G0100-STD-DOCF-FormatPolicy      |
|     **L2: Operation**     | 運用・改訂・CI             | 改訂履歴・CIルール・レビュー手順 | G0110-STD-DOCO-OperationalPolicy |
| **L3: Content Structure** | 構造化YAML・三層モデル        | 内容・形式・意味層定義       | G0400, G0410, G0420              |
|       **L4: Coding**      | 言語非依存のコーディング標準       | コード原則・測定・逸脱管理     | G0300-STD-COD0-CodingStandard    |

> 将来拡張レイヤ（L5〜L6）として **Test** および **Security** 系列を追加可能。

---

## 4. 運用分離方針（Operational Separation）

* YAML構造（G0400〜）および書式標準（G0100）は**静的設計基準**として扱う。
* CI・レビュー・改訂は**動的運用基準（G0110）**に分離し、責務を明確化する。
* この分離により、構造検証・生成自動化・再利用を安全に行える。
* Coding標準（G0300）は静的基準として位置付け、運用CI例はG0110に委譲する。

> 構造と運用の境界を固定することで、個人開発環境でも標準化が維持可能となる。

---

## 5. 適用範囲と改訂責務モデル

* 適用範囲：個人開発、学習、教育、研究、OSS公開用ドキュメント。
* 拡張範囲：小規模チームまたはCI/CD統合を行う環境（G0110で定義）。
* 将来的には「Enterprise Profile（P****）」として派生可能。

### 改訂責務モデル（Revision Responsibility Model）

| モード                 | 概要                              | 対象       |
| :------------------ | :------------------------------ | :------- |
| **Self Review**     | 個人開発では自己承認を基本とする。               | 個人プロジェクト |
| **Two-step Review** | 技術レビュー＋文書レビューの二段階承認を推奨（SHOULD）。 | チーム・共同開発 |

> 詳細手順は G0110-STD-DOCO-OperationalPolicy に従う。

---

## 6. 外部準拠仕様（External References）

本標準体系は以下の外部仕様を共通参照とする。

* **GitHub Flavored Markdown (GFM)** – [https://github.github.com/gfm/](https://github.github.com/gfm/)
* **CommonMark Specification** – [https://spec.commonmark.org/](https://spec.commonmark.org/)
* **JSON Schema Draft 2020-12** – [https://json-schema.org/draft/2020-12/schema](https://json-schema.org/draft/2020-12/schema)
* **Schema.org CreativeWork Vocabulary** – [https://schema.org/CreativeWork](https://schema.org/CreativeWork)

---

## Annex A. 統合層マップ（Unified Layer Overview）

|       層      | 名称             | 内容           | 主要文書                             |
| :----------: | :------------- | :----------- | :------------------------------- |
|      L0      | Overview       | 標準体系全体指針     | G0000-STD-OVRV-OverView          |
|      L1      | Format         | 文書構造・書式統一    | G0100-STD-DOCF-FormatPolicy      |
|      L2      | Operation      | 改訂・レビュー・CI   | G0110-STD-DOCO-OperationalPolicy |
|      L3      | YAML Structure | 内容・形式・意味層    | G0400〜G0420                      |
|      L4      | Coding         | コーディング規範・適合性 | G0300-STD-COD0-CodingStandard    |
| L5 (Reserve) | Test           | 検証・品質保証      | 将来定義                             |
| L6 (Reserve) | Security       | 安全・リスク管理     | 将来定義                             |

---

## 7. 改訂履歴

| 版      | 日付           | 内容                                                                                           |
| :----- | :----------- | :------------------------------------------------------------------------------------------- |
| v1.1.0 | "2025-11-09" | Canonical Edition：共通原則（Version, Terminology, Confidentiality, External Spec）を統合。Annex層マップ追加。 |
| v1.0.1 | "2025-11-09" | Star5 Edition：用語定義・SemVer原則・将来拡張記述追加。                                                        |
| v1.0.0 | "2025-11-09" | 初版作成。全標準群の体系・適用範囲・分離方針を定義。                                                                   |
