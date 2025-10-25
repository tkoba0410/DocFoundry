---
schema: "https://schema.org/CreativeWork"
doc_id: "G0101-STD-DOC1"
title: "Compliance Pack (Checklist + Automation) for G0100-STD-DOC0"
version: "1.0.0"
date: "2025-10-23"
status: "Approved"
owner: "Documentation Review Team"
reviewers: ["Project Maintainer"]
confidentiality: "Internal"
scope: "Generic"
lifecycle: "Stable"
description: "Integrated compliance checklist and automation guide derived from G0100-STD-DOC0 Document Policy."
inherit_from: "G0100-STD-DOC0"
related_docs: ["G0100-STD-DOC0","G0110-STD-DCHK","G0111-STD-AUTO"]
---

# [STD-DOC1] Compliance Pack（Checklist + Automation Guide）

本書は以下の2文書を**統合**したパッケージである：  
- **G0110-STD-DCHK**（Compliance Checklist）  
- **G0111-STD-AUTO**（Compliance Automation Guide）

目的は、**1ファイルで準拠確認（レビュー時）と自動化実装（CI時）に必要な情報を完結**させること。

---

## 1. 適用範囲と判定方式

- 対象：`docs/` 配下のすべての Markdown 文書（`*.md`）  
- 単位：**1ファイル単位**  
- 判定：**✅ 準拠 / ⚠ 要修正 / ❌ 未準拠**  
- 分類：チェック項目は **A/B/C** の3区分で扱う（§3 参照）

---

## 2. 準拠チェックリスト

> 表の「区分」は §3 の A/B/C に対応。

| # | 検査項目 | 要件概要 | 区分 | 判定 | 備考 |
|:-:|:--|:--|:--:|:--:|:--|
| 1 | Front Matter（YAML）構造 | `---` で囲まれた YAML FM が存在 | A |  |  |
| 2 | 必須キー（DCMM） | §6.1 の必須キーが揃っている | A |  |  |
| 3 | ダブルクォート囲み | すべての値が `"` で囲まれる | A |  |  |
| 4 | version 形式 | `vX.Y.Z`（SemVer） | A |  |  |
| 5 | 日付形式 | `YYYY-MM-DD`（ISO8601） | A |  |  |
| 6 | doc_id 形式 | `^[GP]\d{4}-[A-Z]{3}-[A-Z0-9]{4}$` | A |  |  |
| 7 | Prefix 妥当性 | `G` または `P` | A |  |  |
| 8 | カテゴリ妥当性 | OVR/REQ/ARC/IMP/TST/OPS/SEC/STD/POL/RPT/REF | A |  |  |
| 9 | H1 構造 | `# [CAT-CODE] タイトル` | A |  |  |
| 10 | PII 非記載 | 氏名・ID 等の個人特定情報なし | C |  |  |
| 11 | owner/reviewers 表記 | 役職/チーム名で記載 | C |  |  |
| 12 | status/lifecycle 整合 | §5.2 の許容組合せ | A |  |  |
| 13 | 文書分類整合 | 本文の主目的がカテゴリ定義と一致 | B |  |  |
| 14 | inherit_from | 参照があれば正しい doc_id 形式 | A |  |  |
| 15 | related_docs | 配列で正しい doc_id 形式 | A |  |  |
| 16 | 改訂履歴 | 直近版が Front Matter と一致 | A |  |  |
| 17 | ファイル名一致 | ファイル名と `doc_id` の整合 | A |  |  |
| 18 | schema 値 | `"https://schema.org/CreativeWork"` | A |  |  |
| 19 | PII禁止の明記（STD） | STD文書に警告文がある | A |  |  |
| 20 | Markdown 構文 | 見出し/表/コードブロック整合 | A |  |  |

---

## 3. 自動化区分（A/B/C）

### 3.1 区分定義
- **A: CI自動化（Deterministic）** … 正規表現 / JSON Schema / リンタで**完全自動判定**可。  
- **B: AI完全チェック（LLM-Only）** … 意味解釈を要するが **LLMのみで最終判定**可（しきい値 ≥ 0.8）。  
- **C: 人間レビュー必須（Human-Only）** … 組織文脈が不可欠で、**最終判断は人間**。

### 3.2 項目→区分マッピング
- **A**：1,2,3,4,5,6,7,8,9,12,14,15,16,17,18,19,20  
- **B**：13  
- **C**：10,11

---

## 4. CI 実装ガイド

### 4.1 JSON Schema（A区分）
- 位置：`/schemas/dcmm.schema.json`  
- 代表定義：
  - `version`: `^v\d+\.\d+\.\d+$`
  - `date`: `^\d{4}-\d{2}-\d{2}$`
  - `doc_id`: `^[GP]\d{4}-[A-Z]{3}-[A-Z0-9]{4}$`
  - `status`: `Draft|Approved|Deprecated`
  - `lifecycle`: `Draft|Stable|Canonical`
  - `confidentiality`: `Public|Internal|Confidential`
  - `schema`: 固定 `"https://schema.org/CreativeWork"`

### 4.2 正規表現例（A区分）
```txt
# H1 構造
^# \[[A-Z]{3}-[A-Z0-9]{4}\] .+

# YAML 値のダブルクォート（簡易）
^\s*[a-zA-Z0-9_-]+:\s*".*"

# ファイル名=doc_id（CIで比較の擬似式）
filename_without_ext == front_matter.doc_id + "-" + TitleCamelCase
```

### 4.3 LLM 自動判定（B区分：項目13）
1. 本文から見出しと要約（最大 1,000 文字）を抽出。  
2. 期待カテゴリ定義（§3.2/§3.5：G0100）をプロンプトに付与。  
3. 出力：`一致 / 不一致 / 不明` と確率スコア。  
4. **スコア ≥ 0.8 を合格**、それ未満は CI 失敗（差戻し）。

---

## 5. 人間レビュー指針（C区分）

### 5.1 PII 非記載（項目10）
- 観点：署名・連絡先・アカウントID・個人宛評価の記載有無。  
- 原則：疑わしい場合は **全置換**（氏名→役職/チーム）。

### 5.2 owner / reviewers 表記（項目11）
- 許容例：`"Project Maintainer"`, `"Documentation Review Team"`  
- 非許容：個人名・ハンドル・社員番号 等。

---

## 6. 運用（レビューフロー）

1. **Schema 検証**（A）→ 失敗なら終了  
2. **正規表現検証**（A）→ 失敗なら終了  
3. **LLM 判定**（B）→ しきい値合格で自動可決  
4. **リンタ**（A）→ 体裁統一  
5. **人間レビュー**（C）→ 最終承認 / 差戻し  
6. **レポート**：結果は `RPT-xxxx` 文書で保存

---

## 7. 改訂履歴

| 版 | 日付 | 内容 |
|----|------|------|
| v1.0.0 | "2025-10-23" | 初版。G0110（チェックリスト）と G0111（自動化ガイド）を統合。 |

---
