---
schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0200-STD-COR2-MetaFrameworkRules"
name: "DocFoundaryメタフレームワーク規範"
version: "v1.0.0"
datePublished: "2025-11-15"
inLanguage: ["ja"]
creator:
  "@type": "Person"
  name: "Framework Maintainer"
description: "DocFoundary Framework において、理念（G0000）と分野別フレームワーク（B層）を接続し、全体系を統合するための抽象規範を定義する文書。技術やフォーマットに依存せず、Artifact・構造・参照関係の抽象モデルを提示する。"
---

# [META] DocFoundary メタフレームワーク規範（Meta Framework Rules）

## 1. 目的
本書は G0100-CorePrinciples に定義される理念を、分野別フレームワーク（B層）および個別手法（C層）へ一貫性を保って橋渡しするための抽象規範を定義する。Framework 全体の「論理的な背骨」を提供し、技術や手法が変化しても体系構造が崩れないようにすることを目的とする。

## 2. 適用範囲
- A層 → B層 → C層の階層的接続
- すべての Artifact（文書・仕様・チェックリスト・プロンプトなど）
- 技術非依存の抽象規範

## 3. Artifact 抽象モデル（Artifact Abstract Model）
DocFoundary におけるすべての Artifact は、以下の 3 層で構造化されるものとする。

### 3.1 Metadata Layer（メタデータ層）
- identifier, name, version, status など
- 意味的識別と追跡を担う

### 3.2 Structure Layer（構造層）
- 構造化表現（階層構造、参照、ID 体系）
- 人間用文章（Documentation）と機械可読構造（Schema）の分離

### 3.3 Content Layer（内容層）
- 文章
- 表
- 補足定義

この 3 層はいずれも、技術（YAML/JSON/DSLなど）に依存しない抽象構造である。

## 4. 参照構造（Reference Model）
Artifact 間の参照は以下の抽象規範に従う。

### 4.1 Logical Reference（論理参照）
- identifier を基点とした論理的一意参照

### 4.2 Structural Reference（構造参照）
- Artifact 内部の ID（sectionId 等）による階層参照

### 4.3 Cross-Layer Reference（層間参照）
- A→B、B→C 方向は許可
- C→A の直接参照は不可（META 層を経由する）

## 5. AI 可読性の抽象要求（AI Readability Requirements）
- 機械が誤解しないための「意味構造」が明示されていること
- 情報粒度が一貫しており、省略・暗黙の前提を避けること
- 文脈依存を最小限にし、ID体系で関係性が表現されていること
- 形式は問わないが、階層性・参照性・一貫性を備えること

## 6. 層間統合規範（Layer Integration Rules）
### 6.1 A層 → B層
- 原則は、分野フレームワークに抽象構造として継承される

### 6.2 B層 → C層
- 分野フレームワークで定義された構造規範に基づいて個別手法を実装する

### 6.3 C層 → A層（禁止）
- 個別手法から理念層への逆参照は禁止（META 層で翻訳する）

## 7. 改訂と維持の方針
- META 層は Framework の安定性を担うため、頻繁な改訂は行わない
- 技術の変化に合わせて抽象規範を拡張することは許可
- A層の原則と矛盾する場合は META 層を優先して調整する

