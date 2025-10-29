---
schema: "https://schema.org/CreativeWork"
doc_id: "G0210-STD-SCDT"
title: "開発フェーズ共通テンプレート集（v3.0統一構成）"
version: "v3.0.0"
date: "2025-10-15"
status: "Approved"
lifecycle: "Canonical"
scope: "Generic"
owner: "Standards-Governance-Team"
reviewers:
  - "Template-Management-Guild"
  - "Quality-Assurance-Guild"
confidentiality: "Public"
---

# [SCD-TMPL] 開発フェーズ共通テンプレート集（v3.0統一構成）

**Version:** v3.0.0
**Date:** 2025-10-15
**Status:** Approved

---

## 1. 目的と位置づけ（Purpose & Scope）

本書は ExchangeApi 開発標準 v3.0 における全フェーズ（SCD1〜SCD6, SCDM）を支える
**共通テンプレートセット（T1〜T4）および用語集・教育リソース** を提供する。

目的は以下のとおり：

- 各フェーズで使用する標準テンプレートを一元管理する。
- ReqID・Conformance・ADR・Deviation の共通形式を維持する。
- 教育・監査・CI整合の基礎資産として運用する。

---

## 2. テンプレート概要（Overview of Templates）

| No | テンプレート名 | 用途 | 主な利用フェーズ | 管理形式 |
|:--|:--|:--|:--|:--|
| **T1** | ReqID一覧表 | 要求ID・要求強度（MUST/SHOULD/MAY）を管理 | SCD1（Spec） | CSV／YAML／Markdown |
| **T2** | Conformance Matrix (AI Validation Log対応) | ReqID ⇄ Test ⇄ Impl 整合を追跡 | SCD3〜SCD5 | CSV／Markdown |
| **T3** | ADR（Architecture Decision Record） | 設計判断・根拠・変更理由の記録 | SCD2／SCD4／SCD6 | Markdown |
| **T4** | Deviation Record | 不適合項目と再試験結果の追跡 | SCD5／SCD6 | JSON／Markdown |

---

## 3. テンプレート構造（Template Structures）

### **T1: ReqID一覧表**
| ReqID | 要求名 | RFC2119強度 | 概要 | 試験方法 | 状態 |
|:--|:--|:--|:--|:--|:--|
| API-R001 | リトライポリシー実装 | MUST | 429応答時に再試行制御を行う | 自動テスト | 承認済 |
| API-R002 | タイムアウト設定 | SHOULD | 接続断時の再送間隔制御 | 手動確認 | 草稿 |

### **T2: Conformance Matrix (AI Validation Log対応)**
| ReqID | TestID | ImplRef | Status | CI RunID | T2 LogRef | 備考 |
|:--|:--|:--|:--|:--|:--|:--|
| API-R001 | ApiClientTests.R001 | ApiClient | ✅ Passed | 2025-10-07-#134 | T2-Log-001 | 自動 |
| API-R002 | ApiClientTests.R002 | ApiClient | ⚠️ Failed | 2025-10-08-#135 | T2-Log-002 | 要再試験 |

### **T3: ADR (Architecture Decision Record)**
| No | 日付 | 判断概要 | 背景・選択肢 | 決定内容 | 関連ReqID | 承認者 |
|:--|:--|:--|:--|:--|:--|:--|
| ADR-001 | 2025-10-21 | リトライポリシー戦略 | Exponential Backoff vs Fixed Delay | Exponential Backoffを採用 | API-R001 | T.Lead |
| ADR-002 | 2025-10-21 | API契約管理方法 | OpenAPI vs JSON Schema | OpenAPI採用 | ALL | Architect |

### **T4: Deviation Record**
| No | 発生日 | 関連ReqID | 概要 | 対応状況 | 再検証結果 | 登録者 |
|:--|:--|:--|:--|:--|:--|:--|
| DEV-001 | 2025-10-08 | API-R002 | タイムアウト例外発生 | 修正完了 | ✅ 再試験合格 | QA |
| DEV-002 | 2025-10-21 | API-R003 | 仕様未対応項目あり | 対応中 | ⏳ | QA |

---

## 4. 用語レベル体系（Glossary Level Framework）

| レベル | 対象読者 | 用語理解の深さ | 例 |
|:--|:--|:--|:--|
| **L1（基礎）** | 初心者・QA・管理補助 | 基本概念と用語の意味を理解 | ReqID, ADR, Spec |
| **L2（運用）** | 開発者・テスター | テンプレートの使い方を理解し運用できる | Conformance Matrix, T2, Deviation |
| **L3（監査）** | 標準化担当・リード | 各テンプレート間の整合と品質基準を監査できる | Rolling Conformance, RFC2119 |

---

## 5. 運用ルール（Usage and Governance）

| 項目 | ルール | 備考 |
|:--|:--|:--|
| **命名規則** | T番号（T1〜T4）を必ず明記し、成果物間で整合を取る | 例: `T2-ConformanceMatrix.csv` |
| **管理場所** | `/docs/std/templates/` 以下に配置 | バージョン管理対象 |
| **更新ルール** | SCDT文書更新後は各Phaseの参照も同日更新 | 参照先差分を最小化 |
| **教育運用** | Glossary・誤例・良例をSCDTで一元管理 | 教育リソース化 |
| **CI整合性** | T2とT4は自動生成可、他は手動登録 | AI Validation Log連携 |

---

## 6. 付録（Appendix）

### A. T番号とPhase対応
| テンプレ | 対応フェーズ | 主要利用目的 |
|:--|:--|:--|
| **T1** | SCD1（Spec） | 要求管理 |
| **T2** | SCD3〜SCD5（Test〜Conformance） | 適合確認・自動検証 |
| **T3** | SCD2／SCD4／SCD6（Contract／Impl／Feedback） | 設計判断・根拠記録 |
| **T4** | SCD5／SCD6（Conformance／Feedback） | 不適合追跡・再試験 |

### B. 用語略称一覧
| 略称 | 名称 | 対応フェーズ |
|:--|:--|:--|
| **T1** | ReqID一覧表 | SpecPhase |
| **T2** | Conformance Matrix (AI Log対応) | Test〜Conformance |
| **T3** | ADR (Architecture Decision Record) | Contract〜Feedback |
| **T4** | Deviation Record | Conformance〜Feedback |

### C. Cycle連携図（v3.0対応）
```
[SPEC] → [CONTRACT] → [TEST] → [IMPL] → [CONFORMANCE] → [FEEDBACK]
     │                                               │
     └────────────── Templates (SCDT: T1〜T4) ───────────────┘
```

### D. 改訂履歴
| Version | Date | 概要 | 担当 |
|:--|:--|:--|:--|
| v3.0.0 | 2025-10-15 | DCMM準拠のメタデータ更新とテンプレート記述整合。 | Standards-Governance-Team |
| v2.0.0 | 2025-10-21 | v2.2系からv3.0構造へ統一。Glossary追加。 | Documentation Team |

---

**End of Document**
