---
schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0100-STD-DOC0-01-FormatPolic"
name: "ドキュメント書式標準 第1巻（Vol.01：第1〜3章）"
version: "v5.7.1"
datePublished: "2025-11-11"
inLanguage: ["ja"]
creator:
  "@type": "Person"
  name: "Individual Developer"
description: "ドキュメント書式標準の第1〜3章（定義・体系・命名規則）を収録する巻。"
---

# [STD-DOC0] ドキュメント書式標準 第1巻（Vol.01）

## 収録章
- 第1章：定義と適用範囲
- 第2章：文書体系とカテゴリ構造
- 第3章：ファイル命名規則

---

# 1. 定義と適用範囲（definition-and-scope）
<a id="1"></a>

本標準は、DocFoundary 標準群における **Markdown 文書の形式層仕様** を定義する。
文書の意味や運用手順ではなく、その **構造・命名・書式** を統一し、再現性と整合性を保証することを目的とする。

## 1.1 目的（purpose）
<a id="1-1"></a>

DocFoundary 全体で共通利用される Markdown 文書の形式を標準化し、GFM / CommonMark 準拠の書式に統一する。
また、本標準は全標準群に共通する **形式層（Format Layer）** の基盤仕様として位置づけられる。

## 1.2 適用範囲（scope-of-application）
<a id="1-2"></a>

* **対象**：設計書、仕様書、報告書など Markdown で作成される開発文書。
* **非対象**：ソースコードやスクリプト。ただし解説用文書は含む。
* **位置付け**：本標準は G0000-STD-OVRV（理念層）と G0400-STD-YML0（構造層）の間に位置し、両層を接続する **形式層（Format Layer）** に属する。

---

# 2. 文書体系とカテゴリ構造（document-taxonomy-and-category-model）
<a id="2"></a>

本章では、DocFoundary 標準群で使用されるカテゴリ、および言語コードを定義する。
これらは文書構造の基本分類として本文内で正式に定義され、別レジストリ文書（G0121）への参照は不要である。

## 2.1 Categories（カテゴリ定義）
<a id="2-1"></a>

| コード | 名称 | 用途概要 | 代表文書例 |
| :-: | :-- | :-- | :-- |
| OVR | 概要（Overview） | 背景・目的・原則を定義 | G0000-STD-OVRV-Overview |
| REQ | 要求仕様（Requirements） | 機能・非機能要求 | G0200-REQ-REQF |
| ARC | 設計書（Architecture） | システム構成・API定義 | G0300-ARC-COD0 |
| TST | 試験仕様（Test） | テスト方針・手順 | G0500-TST-TSTP |
| OPS | 運用（Operations） | 運用・保守 | G0110-OPS-DOCO |
| SEC | セキュリティ（Security） | リスク・対策 | G0600-SEC-SECP |
| RPT | 報告書（Report） | 分析・評価 | G0700-RPT-RPTA |
| REF | 参考資料（Reference） | 用語集・例示 | G0120-REF-DOCR |

## 2.2 Language Codes（言語コード）
<a id="2-2"></a>

DocFoundary 標準群では、**日本語（`ja`）を唯一の公式言語コード（MUST）** とする。
すべての標準文書は `inLanguage: ["ja"]` を持たねばならない。

---

# 3. ファイル命名規則（naming-convention）
<a id="3"></a>

```
{Prefix}{4桁番号}-{カテゴリ3}-{文書4}-{タイトル}.md
```

| 要素 | 定義 | 例 |
|------|------|------|
| Prefix | `G`（汎用）または`P`（プロジェクト） | G0100 |
| 4桁番号 | 上2桁＝カテゴリ群／下2桁＝順序 | 0100 / 0110 |
| カテゴリ（3文字） | 文書種別コード | REQ / ARC / OPS |
| 文書コード（4文字） | 英大文字＋数字（最大4桁） | DOC0 / MODL |
| タイトル | UpperCamelCase、ASCII英字＋ハイフン | FormatPolicy |

---

## 3.1 ファイル名と文書名の言語仕様
<a id="3-1"></a>

| 項目 | 言語 | 規範性 | 説明 |
|------|------|------|------|
| ファイル名 | ASCII英数字＋ハイフン | MUST | システム互換性のため完全制限 |
| Front Matter `name` | 日本語のみ | MUST | 正式タイトルとして使用 |
| Front Matter `description` | 日本語（1〜3文） | MUST | 概要説明も日本語 |

---

## 3.2 例と補足
<a id="3-2"></a>

Markdown 本文の H1 見出しでは、必要に応じて
日本語＋英語副題を併記してよい（SHOULD）。

例：
```
# [STD-DOC1] 文書作成指針（Documentation Authoring Guideline）
```

