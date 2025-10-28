---
schema: "https://schema.org/CreativeWork"
doc_id: "G0101-STD-DOC1"
title: "Compliance Pack (Checklist + Automation) for G0100-STD-DOC0"
version: "v1.1.0"
date: "2025-10-30"
status: "Approved"
owner: "Documentation Review Team"
reviewers: ["Project Maintainer"]
confidentiality: "Internal"
scope: "Generic"
lifecycle: "Canonical"
description: "Executable compliance and automation package extending the G0100 Document Policy with CI/AI validation features."
inherit_from: "G0100-STD-DOC0"
related_docs: ["G0100-STD-DOC0"]
x-ai:
  threshold_B: 0.8
  report_format: "jsonl"
  rule_prefix: "DOCCHK-"
  x-schema: "/schemas/dcmm.schema.json"
---

# [STD-DOC1] Compliance Pack（Checklist + Automation Guide）

目的は、**1ファイルで準拠確認（レビュー時）と自動化実装（CI時）に必要な情報を完結**させることである。  
本書は codex-AI による**自動準拠判定・修正提案の基準文書**として機能する。

---

## 1. 適用範囲と判定方式

- 対象：`docs/` 配下のすべての Markdown 文書（`*.md`）  
- 単位：**1ファイル単位**  
- 判定：**✅ 準拠 / ⚠ 要修正 / ❌ 未準拠**  
- 分類：チェック項目は **A/B/C** の3区分で扱う（§3 参照）

---

## 2. 準拠チェックリスト

| # | rule_id | 検査項目 | 要件概要 | 区分 | severity | 判定 | 備考 |
|:-:|:--|:--|:--|:--:|:--:|:--:|:--|
| 1 | DOCCHK-FM-001 | Front Matter構造 | **[MUST]** `---` で囲まれた YAML Front Matter が存在 | A | error |  |  |
| 2 | DOCCHK-FM-002 | 必須キー（DCMM） | **[MUST]** G0100 §6.1 の必須キーが揃っている | A | error |  |  |
| 3 | DOCCHK-FM-003 | ダブルクォート囲み | **[MUST]** すべての値が `"` で囲まれている | A | error |  |  |
| 4 | DOCCHK-ID-001 | version形式 | **[MUST]** `vX.Y.Z`（SemVer 2.0.0 準拠） | A | error |  |  |
| 5 | DOCCHK-ID-002 | 日付形式 | **[MUST]** ISO8601 `YYYY-MM-DD` | A | error |  |  |
| 6 | DOCCHK-ID-003 | doc_id形式 | **[MUST]** `^[GP]\d{4}-[A-Z]{3}-[A-Z0-9]{4}$` に一致 | A | error |  |  |
| 7 | DOCCHK-ID-004 | Prefix妥当性 | **[MUST]** `G` または `P` のみを使用 | A | error |  |  |
| 8 | DOCCHK-CAT-001 | カテゴリ妥当性 | **[MUST]** 既定カテゴリ（OVR〜REF）に含まれる | A | error |  |  |
| 9 | DOCCHK-HDR-001 | H1構造 | **[MUST]** `# [CAT-CODE] タイトル` 構文を満たす | A | error |  |  |
| 10 | DOCCHK-PII-001 | 個人情報非記載 | **[MUST]** 氏名・ID・個人識別情報を含まない | C | critical |  |  |
| 11 | DOCCHK-OWN-001 | owner/reviewers表記 | **[MUST]** 役職・チーム名のみで記載 | C | critical |  |  |
| 12 | DOCCHK-STA-001 | status/lifecycle整合 | **[MUST]** G0100 §5.2 の許容組合せに一致 | A | error |  |  |
| 13 | DOCCHK-CAT-002 | 文書分類整合 | **[SHOULD]** 文書の主目的がカテゴリ定義と一致 | B | warning |  |  |
| 14 | DOCCHK-REF-001 | inherit_from形式 | **[MUST]** 正しい doc_id 形式で記載 | A | error |  |  |
| 15 | DOCCHK-REF-002 | related_docs形式 | **[MUST]** 配列形式で doc_id のみを含む | A | error |  |  |
| 16 | DOCCHK-HIS-001 | 改訂履歴整合 | **[MUST]** 最新版が Front Matter と一致 | A | error |  |  |
| 17 | DOCCHK-FN-001 | ファイル名一致 | **[MUST]** ファイル名と `doc_id` が整合 | A | error |  |  |
| 18 | DOCCHK-SCH-001 | schema値 | **[MUST]** `"https://schema.org/CreativeWork"` に一致 | A | error |  |  |
| 19 | DOCCHK-STD-001 | PII禁止の明文化 | **[MUST]** STD文書にPII禁止文を含む | A | error |  |  |
| 20 | DOCCHK-MD-001 | Markdown構文整合 | **[MUST]** 見出し・表・コード構文が正しい | A | warning |  |  |

---

## 3. 自動化区分（A/B/C）

### 3.1 区分定義
- **A: Deterministic / Schema-Lint Layer**  
  正規表現・JSON Schema・CIルールで完全自動判定可能。  
  codex-AIは `severity` に基づき自動修正またはPRリジェクトを行う。  

- **B: Semantic / LLM Layer**  
  意味解釈を要する。codex-AIは確率スコアを算出し、`x-ai.threshold_B` 以上を合格とする。  

- **C: Human / Review Layer**  
  組織文脈を含む判断を人間が実施。codex-AIは補助コメントを提示する。  

---

## 4. CI 実装ガイド

### 4.1 JSON Schema（A区分）
- 位置：`/schemas/dcmm.schema.json`  
- 主な定義項目：
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

# ファイル名=doc_id 検証
filename_without_ext == front_matter.doc_id + "-" + TitleCamelCase
```

### 4.3 LLM 自動判定（B区分：項目13）
1. 本文から見出しと主要要約（最大 1,000 文字）を抽出。  
2. G0100 §3.2 / §3.5 のカテゴリ定義をプロンプトに付与。  
3. codex-AIは「一致／不一致／不明」と確率スコアを返す。  
4. スコア ≥ `x-ai.threshold_B`（既定：0.8）を合格とする。  

---

## 5. 人間レビュー指針（C区分）

### 5.1 PII 非記載（項目10）
- 対象：署名、個人連絡先、アカウントID、SNSハンドル等。  
- 原則：疑わしい場合は役職・チーム名へ**全置換**。  

### 5.2 owner / reviewers 表記（項目11）
- 許容例：`"Project Maintainer"`, `"Documentation Review Team"`  
- 非許容例：実名・社員番号・SNSハンドル等。  

---

## 6. 運用（レビューフロー）

1. **Schema 検証（A）** → 失敗時は即終了。  
2. **正規表現検証（A）** → 一致しない場合はPR差戻し。  
3. **LLM 判定（B）** → スコア判定し合格／要再確認を出力。  
4. **リンタ（A）** → Markdown整形。  
5. **人間レビュー（C）** → 承認または修正要求。  
6. **レポート生成** → 出力形式は `x-ai.report_format`（既定: jsonl）。  

---

## 7. codex-AI 実装設定例

```yaml
# codex-ai-config.yaml
base_policy: "G0100-STD-DOC0"
compliance_pack: "G0101-STD-DOC1"
ruleset: "/rules/G0101-STD-DOC1.json"
auto_fix:
  enable: true
  scope: ["A"]
  restrict_pii: true
```

codex-AIはこの設定を読み込み、A区分ルールを即時自動修正対象とし、  
B区分をスコア判定、C区分をコメント提案に留める。

---

## 8. 改訂履歴

| 版 | 日付 | 内容 |
|----|------|------|
| v1.0.0 | "2025-10-23" | 初版。G0110（Checklist）と G0111（Automation Guide）を統合。 |
| v1.1.0 | "2025-10-30" | rule_id・severity追加、Front Matter拡張、codex-AI実行指針を新設。 |
