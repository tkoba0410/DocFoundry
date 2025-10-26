---
schema: "https://schema.org/CreativeWork"
doc_id: "P0200-STD-DOC2"
title: "Project Adaptation Guide – ExchangeApi"
version: "1.0.0"
date: "2025-10-26"
status: "Draft"
owner: "Project Maintainer"
reviewers: ["Architecture Review Board", "QA Lead"]
confidentiality: "Internal"
scope: "ExchangeApi"
lifecycle: "Stable"
description: "Defines project-level parameters for adapting the standard documentation (G0100–G0210) to the ExchangeApi project context."
---

# [P02-DOC2] ExchangeApi プロジェクト適用ガイド

## 1. 目的と適用範囲
本書は、汎用標準文書体系（G0100〜G0210）を ExchangeApi プロジェクトに適用する際の
**プロジェクト固有設定項目**を定義し、標準との整合を保ちながら開発・品質・運用の一貫性を確保することを目的とする。

本ガイドにより、チーム内での命名、要求管理、契約仕様、検証、監査が標準化され、
ExchangeApi プロジェクトに特化した SCD 開発運用が実現される。

---

## 2. 適用範囲
- 対象：ExchangeApi（デジタル会計インフラ）関連の全リポジトリ
- 開発対象：Rest.Core, Rest.Adapter, Exchange, AbstractExchange 層
- 関連標準：G0100〜G0210 のうち全フェーズ（SCD0〜SCD6）およびテンプレート（SCDT）

---

## 3. プロジェクト固有設定一覧
| 区分 | 項目名 | 設定値 | 備考 |
|------|---------|---------|------|
| **基本情報** | Project ID | EXA | ExchangeApi 固有識別子 |
|  | Project Name | ExchangeApi Development | プロジェクト正式名称 |
|  | Domain Scope | FinTech / API Integration | 業務・技術領域 |
| **組織・責任** | Owner Role | Project Maintainer | 標準適用責任者 |
|  | Review Team | [QA Lead, Architecture Review Board] | 文書・仕様レビュー担当 |
| **文書体系** | Prefix Policy | `P02xx` | ExchangeApi 専用文書番号プレフィックス |
|  | Category Extension | DSN（Design） | 設計系文書拡張カテゴリ |
| **要求管理** | ReqID Naming Rule | `EXA-R###` | 例: EXA-R001, EXA-R002 |
|  | Traceability Policy | 1 ReqID ⇄ 1 TestCase ⇄ 1 ADR | トレーサビリティ方針 |
| **契約・仕様** | Contract Format | OpenAPI 3.1 | API契約仕様形式 |
|  | Versioning Rule | SemVer 2.0.0 | 破壊的変更はMAJORで管理 |
| **テスト・品質** | Test Definition Style | Gherkin (BDD) | Example仕様形式 |
|  | CI Integration Policy | GitHub Actions + PyTest | 自動検証環境設定 |
|  | Conformance Threshold | 100% (Fail=0) | 適合率目標 |
| **改善・維持** | Feedback Interval | per release | 各リリース後に再検証 |
|  | Deviation Handling | Register → Fix → Retest → Close | 不適合処理手順 |
| **テンプレート運用** | Template Location | `/docs/templates/` | T1〜T4配置場所 |
|  | Evidence Storage | `/docs/compliance/YYYYMMDD/` | CI出力エビデンス保存先 |
| **監査・準拠** | Compliance Targets | G0100〜G0210 | 適用対象標準群 |
|  | Exception Handling | ADRに記録、3か月再審査 | 適用除外処理 |
| **付加情報** | Language Policy | 日本語／英語併記 | 文書併記方針 |
|  | Confidentiality | Internal | 機密区分 |

---

## 4. 運用ルール
1. すべての設定は `project-config.yml` に定義し、リポジトリルートで管理する。
2. 設定変更時は Pull Request によりレビューチームが承認する。
3. 変更理由は ADR（T3）に記録し、ConformancePhase で整合を再検証する。
4. FeedbackPhase にて標準文書との差異を年次確認し、必要に応じて改訂を提案する。

---

## 5. 設定ファイル例
```yaml
project_id: EXA
project_name: ExchangeApi Development
domain: FinTech
owner_role: Project Maintainer
review_team: [QA Lead, Architecture Review Board]
doc_prefix: P02
reqid_prefix: EXA-R
contract_format: OpenAPI 3.1
test_format: Gherkin
ci_system: GitHub Actions
compliance_targets:
  - G0100-STD-DOC0
  - G0101-STD-DOC1
  - G0200-STD-SCD0
  - G0201-STD-SCD1
  - G0210-STD-SCDT
feedback_interval: per release
deviation_policy: Register → Fix → Retest → Close
```

---

## 6. 改訂履歴
| 版 | 日付 | 内容 |
|----|------|------|
| v1.0.0 | 2025-10-26 | 初版。G0102-STD-DOC2をExchangeApiプロジェクト仕様に適用。 |

