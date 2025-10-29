---
schema: "https://schema.org/CreativeWork"
doc_id: "G0220-STD-SCDM"
title: "フェーズ別実務行動マップ（v3.1汎用統合版）"
version: "v3.1.0"
date: "2025-10-30"
status: "Approved"
lifecycle: "Canonical"
scope: "Generic"
owner: "Standards-Governance-Team"
reviewers:
  - "Operations-Enablement-Guild"
  - "Quality-Assurance-Guild"
confidentiality: "Public"
links:
  - doc_id: "G0200-STD-SCD0"
    relation: "base_on"
    comment: "Cycle Overview v3.1.0 準拠"
---

# [SCD-MAP] フェーズ別実務行動マップ（v3.1汎用統合版）

**Version:** v3.1.0
**Date:** 2025-10-30
**Status:** Approved

---

## 1. 目的と位置づけ（Purpose & Scope）

本書は **汎用標準体系** における
全フェーズ（SCD0〜SCD6, SCDT）を統合的に俯瞰し、
**「誰が・何を・どう・何の成果を得て・いつ完了するか」** を明確化する行動ガイドである。

目的：
- 各フェーズの実務行動を統一構造で整理する。
- 教育（L1〜L3）・実務・CI連携を同一図上で理解できるようにする。
- Rolling Conformance を行動レベルで定義する。

---

## 2. フェーズ別実務行動マップ

| フェーズ | 主担当（Who） | 作業内容（What） | 手順（How／Step） | 成果物（Deliverables） | 終了基準（Outcome） |
|:--|:--|:--|:--|:--|:--|
| **SCD1 – Spec Phase** | 仕様責任者／QA | 要求を抽出・形式化・承認 | ① 要求抽出<br>② RFC2119形式化<br>③ 曖昧語除去レビュー<br>④ 承認・登録 | **T1: ReqID一覧表**<br>Spec Document<br>Conformance Matrix初期版 | ReqIDが明確・承認済み（100%） |
| **SCD2 – Contract Phase** | アーキテクト／設計責任者 | API契約・DTO・Schema確立 | ① IF／DTO定義<br>② Schema作成<br>③ 破壊的変更検出<br>④ 承認・ADR登録 | **Contract Schema**<br>**T3: ADR**<br>**T2: Validation Log** | 契約整合率100%、破壊的変更なし |
| **SCD3 – Test Phase** | QA／Tester／開発補助 | Example仕様を定義し自動実行 | ① Example作成<br>② レビュー<br>③ 承認<br>④ CI実行 | **Example（.feature）**<br>**T2: Validation Log**<br>**T3: ADR** | CI Pass率100%、網羅率100% |
| **SCD4 – Impl Phase** | 開発者／レビュー担当 | TDDで最小実装 | ① Red→② Green→③ Refactor→④ CI | **実装コード**<br>**T2: Log**<br>**T3: ADR** | すべてのテストGreen、CI成功 |
| **SCD5 – Conformance Phase** | QA／CI管理者 | CIで仕様・実装の整合性検証 | ① Suite実行<br>② 結果集計<br>③ Fail登録<br>④ 承認 | **T2: Matrix**<br>**T4: Deviation Record**<br>**T3: ADR** | 適合率100%、Fail=0 |
| **SCD6 – Feedback Phase** | QA／設計責任者／Tech Lead | 不適合分析→修正→再試験→仕様更新 | ① Fail抽出<br>② 原因分析<br>③ 修正／再試験<br>④ Spec更新 | **T4: Deviation Record**<br>**T3: ADR更新**<br>Spec更新版 | Deviation=0、全更新反映済 |
| **SCDT – Template Phase** | 全員／標準管理者 | T1〜T4管理・教育・Glossary統合 | ① テンプレ改訂<br>② 用語整備<br>③ 教育反映 | **T1〜T4共通資源**<br>Glossary | 全Phaseの語彙・テンプレ整合 |
| **SCD0 – Cycle Overview** | 標準化チーム／教育担当 | 開発サイクル全体の設計・維持 | ① フェーズ統合<br>② 関係図更新<br>③ 教育運用 | **Cycle Overview文書** | SCDサイクル全体が運用可能 |

---

## 3. フェーズ連携フロー（Rolling Conformance）

```mermaid
flowchart TD
    A1[Spec (T1)] --> A2[Contract (T3)]
    A2 --> A3[Test (T2)]
    A3 --> A4[Impl (T2,T3)]
    A4 --> A5[Conformance (T2,T4)]
    A5 --> A6[Feedback (T3,T4)]
    A6 --> A1
    subgraph SCDT [Templates]
    T1[ReqID] -.-> A1
    T2[Conformance Matrix] -.-> A3 & A4 & A5
    T3[ADR] -.-> A2 & A4 & A6
    T4[Deviation Record] -.-> A5 & A6
    end
```

> **意味:** すべてのPhaseがテンプレート（T1〜T4）で閉ループ化される。
> Rolling Conformance により整合性を常時維持。

---

## 4. 教育レベルと活用範囲（Education Level Mapping）

| レベル | 対象 | 主に利用する文書 | 学習目的 |
|:--|:--|:--|:--|
| **L1（基礎）** | 新メンバー／QA | SCDM（本書）／CycleOverview | 全体像・流れの理解 |
| **L2（運用）** | 開発者／設計者 | SCD1〜SCD6／SCDT | 各フェーズで実際に作業できる |
| **L3（監査・教育）** | 標準・品質管理者 | SCDT／CycleOverview | 整合性監査・教育資料化 |

---

## 5. 運用ポイント（Operational Notes）

| 項目 | 説明 |
|:--|:--|
| **行動の粒度** | 各フェーズの手順表は「1ステップ＝1作業単位」で構成される。 |
| **完了条件の明示** | Outcome列で完了基準を定義。チェックリストと同期する。 |
| **教育導線** | L1→L2→L3に段階的に進行できるように設計。 |
| **自動化連携** | CI/CDは常にT2/T4を更新し、Feedbackへ情報を渡す。 |
| **変更管理** | ADR（T3）を中心に全履歴を追跡。 |

---

## 6. 参照体系（Cross‑Reference）

| 区分 | 文書ID | タイトル | 主な目的 |
|:--|:--|:--|:--|
| Core | **G0200** | 開発サイクル概要（v3.1） | 全体統括 |
| Phase | **G0201〜G0206** | 各フェーズガイド | 各工程の標準手順 |
| Template | **G0210** | 開発フェーズ共通テンプレート集 | T1〜T4定義 |
| Action | **G0220** | 本書（フェーズ別実務行動マップ） | 実践・教育統合 |
| Support | SCDT／SCDM連携資料 | Glossary／Checklist | 教育・監査用途 |

---

## 7. まとめ（Summary）

本書は、汎用標準体系における **行動実行・教育・整合維持の中心文書** である。

- 各Phaseの行動・成果物・完了基準を統一構造で定義。
- 教育レベル（L1〜L3）に対応し、理解から運用まで一貫支援。
- Rolling Conformance により、常時整合・自動検証が可能。

> 📘 **SCDMは、汎用開発の“実務オペレーション基盤”として機能する。**

---

## 8. 改訂履歴 / *Revision History*

| Version | Date | Description |
|:--|:--|:--|
| v3.1.0 | 2025-10-30 | ExchangeApi依存表現を除去し、DCMMリンクを追加。 |
| v3.0.1 | 2025-10-15 | DCMM準拠のメタデータ整備とフェーズ行動表の整合。 |
| v3.0.0 | 2025-08-30 | ExchangeApi標準v3.0統合版として行動マップを刷新。 |

---

**End of Document**
