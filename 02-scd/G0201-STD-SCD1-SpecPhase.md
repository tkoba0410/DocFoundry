---
schema: "https://schema.org/CreativeWork"
doc_id: "G0201-STD-SCD1"
title: "仕様定義フェーズガイド（v3.0統一構成）"
version: "v1.0.0"
date: "2025-10-15"
status: "Approved"
lifecycle: "Canonical"
scope: "Generic"
owner: "Standards-Governance-Team"
reviewers:
  - "Specification-Architecture-Guild"
  - "Quality-Assurance-Guild"
confidentiality: "Public"
inherit_from: ["G0100-STD-DOC0"]
x-schema: "/schemas/dcmm.scd.schema.json"
---

# [SCD-SPEC] 仕様定義フェーズガイド（v3.0統一構成）

**Version:** v1.0.0
**Date:** 2025-10-15
**Status:** Approved

---

## 1. 表紙情報
- 文書番号: `G0201-STD-SCD1`
- バージョン: **v1.0.0**
- 日付: 2025-10-15
- 状態: Approved

---


## 2. フェーズ概要（Purpose & Scope）

本フェーズは、ExchangeApi 開発プロセスの最上流工程であり、
要求を形式化し、**全員が同じ理解と基準で作業を進められる状態** を確立することを目的とする。

目的：
- プロジェクト全体の整合性を確立する。
- 曖昧な要求を形式化し、誤解を防止する。
- ReqID（要求識別子）を基盤として、後続フェーズとの連携を保証する。

---

## 3. フェーズ原則（Principles）

| No | 原則名 | 内容 |
|:--|:--|:--|
| 1 | **Formalization First** | 曖昧な自然文ではなく、RFC2119に準拠した形式文で要求を定義する。 |
| 2 | **Traceability** | ReqIDをすべての工程（Test・Impl・Conformance）に紐づける。 |
| 3 | **AI-Assisted Validation** | AIを検証補助者として活用する（MAY）。最終判断は人が行う。 |
| 4 | **RFC2119 Compliance** | MUST／SHOULD／MAY の明確なキーワードで要求強度を定義。 |
| 5 | **Human Final Authority** | すべての承認は人間が最終決定者となる。 |

---

## 4. 実務ガイド（Practical Flow）

| ステップ | 内容 | 担当 | AI支援（MAY） | 成果物 |
|:--|:--|:--|:--|:--|
| ① 要求抽出 | ユーザ要求・業務要件を収集し観点を整理 | 要求分析者 | 要求分類・重複検出 | 要求候補リスト |
| ② 明文化 | 各要求をRFC2119形式で定義 | 仕様責任者 | 構文提案・曖昧語検出 | ReqID仕様文 |
| ③ レビュー | 曖昧・重複・漏れを確認 | QA／レビュー担当 | 差分比較・曖昧語抽出 | レビューレポート |
| ④ 承認 | 承認者が最終判断し登録を許可 | プロジェクト責任者 | 依存関係チェック | 承認ログ |
| ⑤ 登録 | ReqIDを一覧化しMatrixへ反映 | CI管理者 | 自動マッピング | **T1: ReqID一覧表** |

---

## 5. 成果物（Deliverables）

| 成果物 | 形式 | 内容 | 備考 |
|:--|:--|:--|:--|
| **Spec Document** | Markdown | RFC2119準拠の仕様書 | canonical |
| **T1: ReqID一覧表** | CSV／YAML | ReqID・強度・説明・状態 | Traceable |
| **Conformance Matrix (初期版)** | Markdown | ReqID⇄Test⇄Impl対応 | 初期登録 |
| **AI Validation Log (T2)** | JSON／Markdown | AI検証ログ（任意） | 任意保存 |

---

## 6. チェックリスト（Checklist）

| No | 確認項目 | 判定 | 意義 |
|:--|:--|:--|:--|
| 1 | 全要求が「1観点＝1ReqID」で定義されている | ☐ | トレーサビリティ確保 |
| 2 | RFC2119キーワード（MUST／SHOULD／MAY）が使用されている | ☐ | 要求強度の明確化 |
| 3 | 曖昧表現・重複要求が除去されている | ☐ | 品質向上 |
| 4 | ReqID一覧表（T1）に全要求が登録済み | ☐ | 管理一元化 |
| 5 | Conformance Matrix（初期版）が生成されている | ☐ | Test・Impl連携準備 |
| 6 | 承認記録（署名／承認者名）が残っている | ☐ | 監査対応 |
| 7 | フェーズ完了報告が承認済である | ☐ | 次工程移行条件 |

> **完了基準:** 全項目がチェック済みであれば「仕様定義フェーズ完了（MUST）」とする。

---

## 7. 付録（Appendix）

### A. 用語定義（Glossary, L1〜L3対応）
| 用語 | レベル | 定義 |
|:--|:--|:--|
| **ReqID** | L1 | 要求識別子。1観点1IDで管理する。 |
| **RFC2119** | L2 | 要求強度（MUST／SHOULD／MAY）を定義する国際文書規約。 |
| **Conformance Matrix** | L2 | ReqIDとTest／Implの対応表。整合確認に使用。 |
| **AI Validation Log (T2)** | L3 | AIによる要求検証結果の記録ログ。 |
| **Formalization** | L3 | 曖昧表現を排除し形式的に仕様を定義するプロセス。 |

### B. 記述例（Example）
```text
REQ-ID: API-R001
Keyword: MUST
Statement: サービスは429応答時に再試行ポリシーを適用する。
Linked-Test: TST-R001
Linked-Impl: IMPL-API-RETRY
```

### C. 参照文書
- G0200‑STD‑SCD0‑CycleOverview（開発サイクル概要）
- G0210‑STD‑SCDT‑Templates（共通テンプレート集）
- G0220‑STD‑SCDM‑PhaseActionMap（実務行動マップ）

---

## 8. 改訂履歴 / *Revision History*

| Version | Date | Description |
|:--|:--|:--|
| v1.0.0 | 2025-10-15 | DocFoundry 初版FIXとして再ベースライン。 |
| v3.0.0 | 2025-10-15 | DCMM準拠のメタデータ整備とテンプレート更新。 |

---

**End of Document**
