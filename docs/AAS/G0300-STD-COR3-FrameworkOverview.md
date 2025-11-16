---
schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0300-STD-COR3-FrameworkOverview"
name: "DocFoundaryフレームワーク概要"
version: "v1.0.0"
datePublished: "2025-11-15"
inLanguage: ["ja"]
creator:
  "@type": "Person"
  name: "Framework Maintainer"
description: "DocFoundary Framework 全体の構造・目的・レイヤ体系（A/B/C）の関係を説明し、各分野フレームワークおよび個別手法の配置を統一的に示す。Framework の理解と全体像把握のための地図として機能する文書。"
---

# [FW] DocFoundary フレームワーク概要（Framework Overview）

## 1. 目的
本書は DocFoundary Framework 全体の構造・思想・目的を俯瞰的に提示し、A 層（理念）、B 層（分野フレームワーク）、C 層（個別手法）の相互関係と役割を明確化することを目的とする。Framework 全体の“地図”として、分野間の一貫性維持と整合を支援する。

## 2. フレームワークの背景
現代の開発では、文書・仕様・AI支援・自動化が密接に関係し、単一の標準体系では運用が破綻しやすい。DocFoundary Framework は、理念に基づく抽象層から分野フレームワーク・具体手法への一貫した体系的構成を提供することで、文書と仕様の重複・曖昧化・属人化・肥大化を防ぐ。

## 3. レイヤ体系（A/B/C）
DocFoundary Framework は 3 層の体系で構成される。

### 3.1 A層（Top Layer：理念・抽象原理）
- A0000 CorePrinciples：揺らがない理念
- A0100 MetaFrameworkRules：理念を抽象構造に翻訳する層
- 本層は Framework の憲法として機能し、技術や形式に依存しない

### 3.2 B層（Domain Layer：分野フレームワーク）
- 各分野のフレームワーク（例：Document、YAML、SCD、Coding 等）を統一原則に基づき構造化
- A 層の抽象規範を受け、分野ごとに必要な構造・ルール・標準を定義する

### 3.3 C層（Concrete Layer：個別手法・実務）
- B 層の分野規範を具体的な手法・パターン・テンプレートとして具現化
- 仕様YAML、チェックリスト、指示書、運用ガイドなど、実行可能な成果物が含まれる

## 4. フレームワーク全体構造

```text
A層（理念）
 ├─ G0000 CorePrinciples
 └─ G0100 MetaFrameworkRules

B層（分野フレームワーク）
 ├─ G1000 DocumentFramework
 ├─ G2000 YamlSpecFramework
 ├─ G3000 DevelopmentFramework(SCD)
 └─ G4000 CodingFramework

C層（個別手法）
 ├─ G1xxx 文書設計の具体ポリシー
 ├─ G2xxx YAML/Spec 設計・生成手法
 ├─ G3xxx 開発フロー・レビュー手法
 └─ G4xxx コーディング実務ガイド
```

## 5. フレームワークの目的と特徴
### 5.1 一貫性の維持
A 層→B 層→C 層の流れにより、理念から実務までの整合を保証する。

### 5.2 抽象と具体の分離
理念（WHY）、抽象構造（WHAT）、手法（HOW）を分離し、混乱を防ぐ。

### 5.3 AI 時代への適応
AI が解釈できる構造化表現を前提とし、文書・仕様・チェック等を一元的に扱う。

### 5.4 拡張性と長寿命
A 層により体系の根が安定し、B 層と C 層は分野や手法の追加に柔軟に対応できる。

## 6. 分野フレームワークの概要（B 層）
### 6.1 Document Framework（B1000）
- 文書構造・形式・運用の標準化

### 6.2 YamlSpec Framework（B2000）
- 仕様・チェックリスト・指示書の構造化ルール
- AI 支援開発における参照源としての役割

### 6.3 Development Framework（B3000）
- SCD モデルに基づく開発プロセスの標準化

### 6.4 Coding Framework（B4000）
- コーディング規約・モデル設計・レビュー基準

## 7. 今後の拡張指針
- A 層は原則として追加最小限
- B 層は必要に応じて分野追加可能（例：AI Framework / OPS Framework）
- C 層は無制限に増やせる手法層

## 8. 改訂ポリシー
- Framework Overview は B/C 層の拡張に応じて柔軟に改訂する
- A 層との整合が第一優先

