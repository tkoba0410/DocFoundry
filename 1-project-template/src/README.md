---
schema: "https://schema.org/CreativeWork"
doc_id: "P0401-IMP-SRCG"
title: "Source Code Structure Guide"
version: "0.1.0"
date: "2025-10-26"
status: "Draft"
owner: "Project Maintainer"
reviewers: ["Architecture Review Board"]
confidentiality: "Internal"
scope: "Project"
lifecycle: "Draft"
description: "プロジェクトのソースコード構造および実装方針を定義する。"
related_docs: ["G0204-STD-SCD4-ImplPhase","G0103-STD-DOC3-CodingStandard"]
---

# [IMP-SRCG] ソースコード構造ガイド

## 1. 目的
本書は、SCDモデルの **Implementation Phase（G0204）** に基づき、  
`src/` ディレクトリ以下に配置する実装コードの構造、命名規則、責務分離の方針を示す。

## 2. ディレクトリ構成例
```plaintext
src/
├── Core/             # ドメインロジック（DDDのDomain層）
├── Application/      # ユースケース層・サービス定義
├── Infrastructure/   # 外部接続・DB・APIアダプタ
└── Presentation/     # WebAPI・UI・CLIなどのエントリポイント
```

## 3. 命名・配置規則
- **クラス名**：PascalCase、ファイル名と一致（C#標準準拠）  
- **名前空間**：`ProjectName.Layer.Component` 構成（例：`ExchangeApi.Core.Trade`）  
- **フォルダ構成**：DDDの層に基づき、循環依存を禁止（MUST）  
- **コメント標準**：`/// <summary>` XMLコメント形式で記述（MUST）  
- **コード規約**：`G0103-STD-DOC3`（CodingStandard）および `G0104-LANG-CS` に準拠。

## 4. ビルド・構築ルール
- .NET 8.0を標準とし、`dotnet build` / `dotnet test` により検証する。  
- 外部パッケージは NuGet を通じて明示管理（ローカルコピー禁止）。  
- 公開API契約は `project-template/docs/P0202-REQ-OVRV-Overview.md` に対応。

## 5. 関連標準
- G0204-STD-SCD4-ImplPhase（Implementation Phase）  
- G0103-STD-DOC3-CodingStandard（Core Coding Rules）  
- G0104-STD-LANG-CS（C#言語規範）

## 6. 改訂履歴
| 版 | 日付 | 内容 |
|----|------|------|
| 0.1.0 | 2025-10-26 | 初版（テンプレート生成） |
