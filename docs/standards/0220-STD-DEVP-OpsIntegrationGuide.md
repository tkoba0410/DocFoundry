# [STD-DEVP-Ops-IntegrationGuide] 運用統合ガイド / *Operational Integration Guide*
**Version:** v0.1.0  
**Date:** 2025-10-09  
**Status:** Draft  

---

## 1. 目的と位置づけ / *Purpose and Scope*
本書は、開発プロセス標準 [STD-DEVP-CycleGuide v2.1.0](0200-STD-DEVP-CycleGuide.md) と
その補助文書 [STD-DEVP-Templates v1.0.0](0210-STD-DEVP-Templates.md) を、実際の開発運用に統合するための指針を示す。

目的は、**整合性サイクル（Spec–Conformance Cycle）を運用面で途切れさせないこと**。  
特に、テンプレート更新・CI/CD連携・レビュー・履歴管理を一貫化し、  
CycleGuideの理念を日常的運用へ落とし込むことを目指す。  

---

## 2. 運用統合の基本原則 / *Integration Principles*

| 原則 | 内容 |
|------|------|
| **1. 一方向整合性** | 仕様変更は常に ReqID → Contract → Test → Impl の順で反映する。 |
| **2. 自動化優先** | Conformance Matrix更新・テスト結果反映は可能な限りCI/CDで自動処理。 |
| **3. 単一情報源化** | ReqID, ADR, Deviationは 標準文書ディレクトリ 内で集中管理。 |
| **4. 変更責任明確化** | 各テンプレートの更新責任者（Author, QA, Lead）を明示する。 |
| **5. 履歴追跡可能性** | すべての変更はGit履歴またはPR単位で追跡可能にする。 |

---

## 3. 運用フロー / *Operational Flow*

**図1: Spec–Conformance 運用統合フロー**  

```
[Spec更新]
    │（ReqID追加・修正）
    ▼
[Templates更新]
    ├─ ReqID一覧更新 (T1)
    ├─ ADR追記 (T3)
    └─ Conformance Matrix反映 (T2)
    │
    ▼
[CI/CD検証]
    ├─ 自動テスト実行
    ├─ 合格率集計 (100% = Merge条件)
    └─ Deviation自動登録 (T4)
    │
    ▼
[レビュー・承認]
    ├─ Tech Lead承認
    ├─ QA再確認
    └─ マージ（新状態を反映）
    │
    ▼
[フィードバック]
    └─ ADR/Deviation結果を仕様書へ反映
```

---

## 4. 実務運用ルール / *Practical Rules*

- **ReqIDの運用:**  
  - 新規追加は `T1: ReqID一覧表` に登録。  
  - RFC2119強度（MUST/SHOULD/MAY）を明示し、レビュー対象とする。  

- **Conformance Matrix（T2）:**  
  - CIジョブ完了後に自動更新される形式を推奨。  
  - Fail項目は自動的に `T4: Deviation Record` に登録される。  

- **ADR（T3）:**  
  - 設計判断をIssueまたはPRに紐づけて管理。  
  - 承認済みADRは次回仕様改訂時にCycleGuideへ反映。  

- **Deviation Record（T4）:**  
  - テスト失敗・仕様逸脱を即時記録。  
  - 修正完了後に再試験結果を更新し、状態を「✅再試験合格」に変更。  

- **更新単位:**  
  - 各更新は1PR＝1変更単位とする（ReqID追加やADR修正ごとに独立）。  
  - CIで100%合格しない限りマージ不可。  

---

## 5. 維持管理 / *Maintenance*

- **責任区分:**  
  | 区分 | 主担当 | 補助担当 |
  |------|--------|-----------|
  | ReqID／仕様整備 | Spec Author | Tech Lead |
  | 契約・設計判断 | System Architect | QA |
  | CI/CD・自動検証 | CI Maintainer | Developer |
  | 逸脱・品質記録 | QA | Tech Lead |

- **改訂サイクル:**  
  - CycleGuideの改訂に合わせ、本書およびTemplatesを見直す。  
  - 軽微な変更（CIスクリプト・記録形式）はOpsレベルで独立改訂可。  

---

## Appendix A. 運用確認チェックリスト / *Operational Checklist*

| 項目 | 内容 | 確認者 | 状態 |
|------|------|--------|------|
| ReqID一覧が最新か | 新規要求・修正が反映されているか | QA | ☐ |
| Conformance合格率 | CI結果100%が確認されたか | CI Maintainer | ☐ |
| ADR記録 | 直近の設計判断が記録されているか | Architect | ☐ |
| Deviation再試験結果 | 再試験合格まで登録が完了しているか | QA | ☐ |
| Git履歴整合 | すべての変更がPR単位で追跡可能か | Tech Lead | ☐ |

---

**Version:** v0.1.0  
**Date:** 2025-10-09  
**Status:** Draft  
