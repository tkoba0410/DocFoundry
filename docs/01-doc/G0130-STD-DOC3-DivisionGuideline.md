---

schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0130-STD-DOC3-DivisionGuideline"
name: "分冊（Volume）方式・汎用ファイル名規則（末尾番号方式）"
description: "DocFoundary における大規模 Markdown 文書の分冊方式と末尾番号方式のファイル名規則を定義する。"
version: "v1.0.0"
datePublished: "2025-11-13"
inLanguage:
  - "ja"

creator:
  - "@type": "Person"
    name: "Individual Developer"

---

# 分冊（Volume）方式・汎用ファイル名規則（末尾番号方式）

本書は DocFoundary における **大規模 Markdown 文書の分冊（Volume）方式** のうち、従来方式（文書コード直後に番号を置く）をアップデートし、**末尾番号方式（Title の直後に Vol 番号を付与する方式）** を正式案として定義する。

単一ファイル文書との整合性、直感的な可読性、シリーズ構造の明示性に優れ、将来の拡張性も高い方式である。

---

## 1. 基本原則（Core Principles）

### ★ Front Matter に関する原則（明確化 / MUST）

* **すべての分冊ファイル（00および Vol01〜VolNN）は CreativeWork 9キーの Front Matter を持たなければならない（MUST）。**

* **各分冊は独立した CreativeWork として成立する必要があるため、省略不可（MUST NOT omit）。**

* **00番と各Volは、identifier／name／description を巻ごとに固有の値へ設定しなければならない（MUST）。**

* **改訂履歴は 00番専用とし、Vol側の Front Matter に含めてはならない（MUST NOT）。**

* 分冊（Volume）は **実ファイルとして作成する（MUST）**。

* 分冊番号は **00 から始まる 2 桁整数**（00, 01, 02…）。

* 番号は **タイトルの末尾に付与する**（本方式の最大特徴）。

* **00番ファイルは総合編（Index）** とし、本文を持たない（MUST）。

* Vol01 以降は本文のみを持ち、参照文書・改訂履歴を記載しない（MUST NOT）。

* Volume 構造は、行数・トークン数が本書で定義する上限値以内である限り **任意項目（optional）** とする。ただし基準値を超える場合は本方式に従って分冊しなければならない（MUST）。

---

## 2. 末尾番号方式のファイル名規則（Naming Convention）

### 2.1 基本フォーマット

```
{Prefix}{4桁番号}-{カテゴリ3}-{文書4}-{タイトル}-{Vol番号2桁}.md
```

**例：G0100-STD-DOC0-FormatPolicy-01.md**

### 2.2 定義

* Prefix：`G`（汎用） or `P`（プロジェクト）
* Title：ASCII英字＋ハイフン、UpperCamelCase 推奨
* Vol番号：00＝総合編、01〜＝本編

### 2.3 非分割文書（番号なし）

```
G0300-ARC-DES0-ApiDesign.md
```

→ Vol番号を持たず単一で完結する（MUST）。

### 2.4 Volファイルの `name` 表記方式（正式採用 / MUST）

```
{日本語正式タイトル} 第N巻（第X,Y,Z章）
```

例：

* ドキュメント書式標準 第1巻（第1,2,3章）
* ドキュメント書式標準 第2巻（第4,5,6章）
* ドキュメント書式標準 第3巻（附録A）

仕様要点：

* 章は **列挙形式（第1,2,3章）** を用いる（MUST）。
* 附録は `附録A` の形式で列挙可能。
* `name` には英数字略号（c1–c3 など）を使用しない（MUST NOT）。

---

## 3. ファイル名例（G0100-STD-DOC0-FormatPolicy）

```
G0100-STD-DOC0-FormatPolicy-00.md
G0100-STD-DOC0-FormatPolicy-01.md
G0100-STD-DOC0-FormatPolicy-02.md
G0100-STD-DOC0-FormatPolicy-03.md
```

---

## 4. 00番ファイル（総合編 / Index）の役割

* Front Matter（CreativeWork 9キー）
* H1タイトル
* **Vol → 章 → 節** の3階層目次
* 参照文書
* 改訂履歴
* 本文を保持しない（MUST NOT）

---

## 5. Vol01 以降の構造

* Front Matter（CreativeWork 9キー）
* Volタイトル（H1）
* 収録章一覧
* 本文（該当章）
* 改訂履歴・参照文書は含めない（MUST NOT）

---

## 6. Volume 分割基準（Unified 基準）

本標準では、行数とトークン数の二重基準に基づき、**単一の統一基準（Unified 基準）** によって Volume 方式の適用を判断する。

## 6.1 統一基準（Unified 基準）

| 上限トークン数 | 上限行数 | 適用対象 |
|----------------|----------|-----------|
| **3000 tokens** | **220 行** | すべての標準文書に適用される唯一の Volume 分割基準 |

## 6.2 判定ルール（MUST）

以下のいずれかを満たした場合、Volume 分割を適用する（MUST）。

* 文書が **3000 tokens を超える**
* 文書が **220 行を超える**

追加要件：

* 章途中での分割は禁止（MUST NOT）。
* コードはクラス／関数単位など、自然なまとまりで分割する（MUST）。

## 6.3 Rationale（背景）

Markdown 文書は構造密度が高く、LLM による内部圧縮は 4000〜5000 tokens 付近で発生するため、**3000 tokens 以下** が最も編集安定性が高い。  
本基準は長期運用・追加改訂・反復編集における安定性を確保するための安全余裕を含む値として定めている。

---

## 7. 末尾番号方式のメリット

* **非分割文書との整合性が高い（最大の利点）**
* 読み手に自然なタイトル体系
* Vol構造の後付け追加が容易
* ソート順が安定し揺らぎがない
* シリーズとしての一体感が高い

---

## 8. 分割不要文書の扱い

* 行数基準およびトークン基準の双方が基準内であれば、単一ファイルで完結する（MUST）。
* Vol番号は付けない（MUST）。
* 00番ファイルも不要である（MUST）。
* 将来分冊が必要になった場合のみ Volume 方式へ移行可能である（SHOULD）。


