---
schema: "https://schema.org/CreativeWork"
doc_id: "P0501-TST-TEST"
title: "Test Strategy and Folder Guide"
version: "v0.1.0"
date: "2025-10-26"
status: "Draft"
owner: "QA Lead"
reviewers: ["Architecture Review Board"]
confidentiality: "Internal"
scope: "Project"
lifecycle: "Draft"
description: "プロジェクトのテスト戦略、フォルダ構成、命名規則、およびCIとの連携を定義する。"
related_docs: ["G0203-STD-SCD3-TestPhase","G0205-STD-SCD5-ConformancePhase"]
---

# [TST-TEST] テスト戦略およびディレクトリ構成ガイド

## 1. 目的
本書は **Test Phase（G0203）** に基づき、`tests/` ディレクトリ以下で実施する  
ユニットテスト、統合テスト、契約テストの構成と運用ルールを示す。

## 2. テスト分類
| 種別 | 内容 | 成果物 |
|------|------|--------|
| Unit Test | 関数・メソッド単位のロジック検証 | xUnit / NUnit レポート |
| Integration Test | 外部API・DB連携の動作確認 | ログ・スクリーンショット |
| Contract Test | APIスキーマ準拠の確認 | OpenAPI検証結果（T2, T4に連携） |

## 3. ディレクトリ構成例
```plaintext
tests/
├── Unit/
├── Integration/
└── Contract/
```

## 4. 命名・運用規則
- テストクラス名：`<対象>Tests`（例：`OrderServiceTests`）  
- 1メソッド＝1検証意図（単一責任）  
- **T1/T2/T4連携**：
  - 成果は `compliance/T2-ConformanceMatrix.csv` に自動反映。
  - 非適合は `compliance/T4-Deviation/` にレポート。

## 5. CIとの連携
- `ci/workflows/csharp-check.yml` により `.NET test` 実行。  
- 結果を `conformance.yml` に集約し、T2/T4へ書き出す。  
- 成果の自動集計は FeedbackPhase（G0206）で監査。

## 6. 関連標準
- G0203-STD-SCD3-TestPhase（Testing Phase）  
- G0205-STD-SCD5-ConformancePhase（Conformance Phase）  

## 7. 改訂履歴
| 版 | 日付 | 内容 |
|----|------|------|
| v0.1.0 | 2025-10-26 | 初版（テンプレート生成） |
