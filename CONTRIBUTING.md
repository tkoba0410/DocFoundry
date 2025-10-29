---
schema: DOCF-CONTRIB
title: DocFoundry Contributing Guide
version: 1.0.0
---

# 🤝 Contributing Guide

本ドキュメントは、DocFoundry リポジトリへの貢献手順を定義する。

## 1. 原則
- standards 配下の改訂は **Pull Request + レビュー + タグ発行** で行う。
- project-template 配下の改訂は **コピー利用後、個別リポジトリで管理**。
- 変更理由は `T3-ADR` に必ず記録する。

## 2. 命名・版管理
- 文書ID: `G####-STD-` + カテゴリ + 名称  
- バージョン: Semantic Versioning 準拠 (`vMAJOR.MINOR.PATCH`)

## 3. レビュー体制
| 階層 | 承認責任者 |
|------|-------------|
| standards | Documentation Team |
| project-template | Project Lead |
| compliance | QA / Auditor |

## 4. Checklist
| No | 確認項目 | 判定 | 備考 |
|----|------------|------|------|
| 1 | PRにタグとReviewerが設定されている |  |  |
| 2 | ADRが作成・リンク済み |  |  |
| 3 | バージョン更新がSemanticに準拠 |  |  |
