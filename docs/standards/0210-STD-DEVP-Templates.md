# [STD-DEVP-Templates] 開発プロセステンプレート集 / *Development Process Templates*
**Version:** v1.0.0  
**Date:** 2025-10-09  
**Status:** Draft  

---

## 1. 表紙情報 / *Document Information*
- 文書番号: `STD-DEVP-Templates`  
- バージョン: **v1.0.0**  
- 日付: 2025-10-09  
- 状態: Draft  

**準拠文書:**
- [STD-DEVP-CycleGuide v2.1.0](0200-STD-DEVP-CycleGuide.md)（開発サイクルガイド・汎用標準）

---

## 2. 目的と位置づけ / *Purpose and Scope*
本書は「STD-DEVP-CycleGuide v2.2」で定義された開発サイクルを、  
実務として運用するための**最小限のテンプレート（記録書式）**を提供する。  

- 本書は「補助標準」として機能し、CycleGuideを補完する。  
- 各テンプレートは **構造を示すものであり、内容はプロジェクト固有に調整可能**。  
- 各テンプレートは Markdown／Excel／CSV 形式のいずれでも管理可能。  

---

## 3. テンプレート概要 / *Template Overview*

| No | テンプレート名 | 用途 | 主な利用工程 | CycleGuide参照章 |
|----|----------------|------|----------------|------------------|
| T1 | ReqID一覧表 | 要求定義と追跡 | 仕様定義〜適合確認 | 5.1, 5.5 |
| T2 | Conformance Matrix | ReqID・テスト・実装対応の整合確認 | 適合確認 | 5.5 |
| T3 | ADR (Architecture Decision Record) | 設計上の判断・根拠記録 | 契約確立〜実装 | 5.2, 5.6 |
| T4 | Deviation Record | 仕様逸脱と是正対応の記録 | 適合確認〜フィードバック | 5.6 |

---

## 4. テンプレート例 / *Template Examples*

### **T1: ReqID一覧表**
| ReqID | 要求名 | RFC2119強度 | 概要 | 試験方法 | 状態 |
|--------|--------|---------------|--------|----------|------|
| API-R001 | リトライポリシー実装 | MUST | 429応答時の再試行制御 | 自動テスト | 承認済 |
| API-R002 | タイムアウト設定 | SHOULD | 接続断時の再送間隔制御 | 手動確認 | 草稿 |

---

### **T2: Conformance Matrix**
**表1: Conformance Matrix Template**
| ReqID | TestID | ImplRef | Status | CI RunID | 備考 |
|--------|--------|----------|---------|-----------|------|
| API-R001 | ApiClientTests.R001 | ApiClient | ✅ Passed | 2025-10-07-#134 | 自動 |
| API-R002 | ApiClientTests.R002 | ApiClient | ⚠️ Failed | 2025-10-08-#135 | 要再試験 |

---

### **T3: Architecture Decision Record (ADR)**
**表2: ADR Template**
| No | 日付 | 判断概要 | 背景・選択肢 | 決定内容 | 関連ReqID | 承認者 |
|----|------|------------|----------------|------------|------------|----------|
| ADR-001 | 2025-10-09 | リトライポリシー戦略 | Exponential Backoff vs Fixed Delay | Exponential Backoffを採用 | API-R001 | T.Lead |
| ADR-002 | 2025-10-09 | API契約管理方法 | OpenAPI vs JSON Schema | OpenAPI採用 | ALL | Architect |

---

### **T4: Deviation Record**
**表3: Deviation Record Template**
| No | 発生日 | 関連ReqID | 概要 | 対応状況 | 再検証結果 | 登録者 |
|----|--------|------------|--------|-------------|-------------|----------|
| DEV-001 | 2025-10-08 | API-R002 | タイムアウト例外発生 | 修正完了 | ✅ 再試験合格 | QA |
| DEV-002 | 2025-10-09 | API-R003 | 仕様未対応項目あり | 対応中 | ⏳ | QA |

---

## 5. 運用ルール / *Usage and Maintenance*

- **テンプレート改訂方針:**  
  各テンプレートは、CycleGuideのプロセス変更に合わせて見直す。  
  CycleGuide本体を改訂しない限り、独立したマイナーバージョン更新（例: v1.1）で対応可。  

- **プロジェクト運用ルール:**  
  - ReqIDは一意であること。命名規則は「[領域]-[通番]」を推奨。  
  - Conformance Matrixは常に最新状態をCIで自動生成可能とする。  
  - ADRとDeviationは同一PRに含め、履歴と再検証を追跡可能にする。  

- **改訂履歴管理:**  
  - 本書およびテンプレート変更は `docs/std/` 下で管理。  
  - バージョン履歴はCHANGELOGまたはGitタグにより追跡。  

---

## Appendix A. 更新記録 / *Revision Record*

| Version | Date | 概要 | 担当 |
|----------|------|------|------|
| v1.0.0 | 2025-10-09 | 初版作成。CycleGuide v2.1.0に準拠。 | 標準化チーム |

---

**Version:** v1.0.0  
**Date:** 2025-10-09  
**Status:** Draft  
