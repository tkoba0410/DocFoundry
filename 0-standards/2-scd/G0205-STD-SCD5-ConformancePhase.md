---
schema: "https://schema.org/CreativeWork"
doc_id: "G0205-STD-SCD5"
title: "適合確認フェーズガイド（v3.0統一構成）"
version: "v3.0.0"
date: "2025-10-15"
status: "Approved"
lifecycle: "Canonical"
scope: "Generic"
owner: "Standards-Governance-Team"
reviewers:
  - "Conformance-Engineering-Guild"
  - "Quality-Assurance-Guild"
confidentiality: "Public"
---

# [SCD-CONF] 適合確認フェーズガイド（v3.0統一構成）

**Version:** v3.0.0
**Date:** 2025-10-15
**Status:** Approved

---

## 1. フェーズ概要（Purpose & Scope）

本フェーズは、実装（Impl）と仕様（Spec／Contract／Test）が完全に整合しているかを  
**Conformance Testing（適合試験）** により自動的に検証する段階である。  

目的：  
- すべてのReqIDに対しテスト結果が期待通りであることを保証する。  
- 不適合（Deviation）を自動検出・登録・修正へ接続する。  
- 開発全体の品質整合性を定量的に可視化する。

---

## 2. フェーズ原則（Principles）

| No | 原則名 | 内容 |
|:--|:--|:--|
| 1 | **Continuous Verification** | すべての変更後に自動検証を実施し、整合性を常に維持する。 |
| 2 | **T2/T4 Traceability** | Conformance結果をT2・T4に登録して履歴を一元管理する。 |
| 3 | **Zero‑Deviation Policy** | 不適合を放置せず、すべて解消してから次工程に進む。 |
| 4 | **CI Automation** | 適合確認はCIジョブで完全自動化される（MUST）。 |
| 5 | **Transparency** | 結果を全関係者が閲覧できるようにする。 |

---

## 3. 実務ガイド（Practical Flow）

| ステップ | 内容 | 担当 | AI支援（MAY） | 成果物 |
|:--|:--|:--|:--|:--|
| ① 実行（Run） | CI上でConformance Suiteを実行 | CI管理者 | ログ整形・自動分類 | Conformance Log |
| ② 集計（Aggregate） | ReqID単位で結果を集約 | QA／AI補助 | 成否集計 | **T2: Conformance Matrix** |
| ③ 記録（Record） | FailをDeviationとして登録 | QA | 自動抽出・要約 | **T4: Deviation Record** |
| ④ 評価（Evaluate） | 適合率・重要度を算出 | QA／管理者 | 自動スコアリング | 適合率レポート |
| ⑤ 承認（Approve） | Zero‑Deviationを確認し完了を承認 | QA責任者 | 判定要約 | フェーズ完了報告 |

---

## 4. 成果物（Deliverables）

| 成果物 | 形式 | 内容 | 備考 |
|:--|:--|:--|:--|
| **Conformance Matrix (T2)** | CSV／Markdown | ReqID単位の整合結果 | 自動生成 |
| **Deviation Record (T4)** | JSON／Markdown | 不適合・修正履歴 | QA更新 |
| **Conformance Report** | HTML／PDF | 適合率・統計結果 | CI成果物 |
| **CI Execution Log** | テキスト／JSON | 実行ログ | 保存対象 |
| **ADR（T3）** | Markdown | 検証上の設計判断 | オプション |

---

## 5. チェックリスト（Checklist）

| No | 確認項目 | 判定 | 意義 |
|:--|:--|:--|:--|
| 1 | 全ReqIDがConformance対象となっている | ☐ | テスト網羅性確保 |
| 2 | T2（Matrix）が最新化されている | ☐ | 整合データ維持 |
| 3 | 不適合（Deviation）がT4に記録されている | ☐ | 逸脱追跡 |
| 4 | Conformance結果がCIに保存されている | ☐ | 自動化確認 |
| 5 | 適合率100%（Failなし）を達成している | ☐ | フェーズ完了条件 |
| 6 | 承認者が結果をレビュー済である | ☐ | 品質保証 |
| 7 | 結果がチームに共有されている | ☐ | 透明性 |

> **完了基準:** 適合率100%、Deviation=0の状態で「適合確認フェーズ完了（MUST）」とする。

---

## 6. 付録（Appendix）

### A. Conformance出力例（T2抜粋）
| ReqID | Result | ImplRef | RunID | 備考 |
|:--|:--|:--|:--|:--|
| API‑R001 | ✅ Pass | ApiClient | #134 | 自動 |
| API‑R002 | ⚠️ Fail | ApiClient | #135 | Timeout異常 |

### B. Deviation記録例（T4抜粋）
| No | 関連ReqID | 概要 | 対応状況 | 再試験 | 登録者 |
|:--|:--|:--|:--|:--|:--|
| DEV‑001 | API‑R002 | Timeout異常発生 | 修正中 | 未再試験 | QA |

### C. 用語定義（Glossary, L1〜L3対応）
| 用語 | レベル | 定義 |
|:--|:--|:--|
| **Conformance Test** | L1 | 実装が仕様に適合しているか検証するテスト。 |
| **Deviation（T4）** | L1 | 不適合記録。再試験・解決まで追跡する。 |
| **適合率** | L2 | 成功したテスト件数／全件数。 |
| **CI Job** | L2 | 自動化されたテスト実行単位。 |
| **Zero‑Deviation** | L3 | 不適合ゼロ状態。Conformance完了条件。 |

### D. 参照文書
- G0204‑STD‑SCD4‑ImplPhase（実装フェーズ）  
- G0210‑STD‑SCDT‑Templates（共通テンプレート集）  
- G0220‑STD‑SCDM‑PhaseActionMap（実務行動マップ）

---

## 8. 改訂履歴 / *Revision History*

| Version | Date | Description |
|:--|:--|:--|
| v3.0.0 | 2025-10-15 | DCMM準拠メタデータ追加と適合フェーズ指針更新。 |

---

**End of Document**
