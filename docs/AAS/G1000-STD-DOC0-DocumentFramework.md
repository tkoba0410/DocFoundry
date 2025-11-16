---
schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "B1000-STD-DOC0-DocumentFramework"
name: "DocFoundary 文書フレームワーク"
version: "v1.0.0"
datePublished: "2025-11-15"
inLanguage: ["ja"]
creator:
  "@type": "Person"
  name: "Framework Maintainer"
description: "DocFoundary Framework における文書領域（Document Domain）の構造・責務・形式・運用モデルを定義し、文書作成および体系管理の統一性を確保する分野フレームワーク文書。A層の理念・抽象構造に基づき、C層の個別手法へと接続する役割を担う。"
---

# [DOC] DocFoundary 文書フレームワーク（Document Framework）

## 1. 目的
本書は DocFoundary Framework の B層（分野フレームワーク）の一部として、文書（Document）領域における構造・形式・運用規範を定義する。文書作成・維持・整合性確保のための基盤を提供し、A層（理念）と C層（個別手法）を接続する。

## 2. 適用範囲
- すべての DocFoundary 文書（Markdown/HTML/生成物）
- 文書のフロントマター、構造、章立て規則
- 文書の状態管理（Draft/Review/Approved/Deprecated）
- 個別手法（C層）に先行する抽象規範

## 3. 文書構造モデル（Document Structure Model）
文書は以下の要素で構成される。

### 3.1 Metadata（必須）
- schema, identifier, name, version, datePublished, description
- A0100 の Artifact Model に準拠

### 3.2 Body Structure（本文構造）
- 章（Section）
- 小節（Subsection）
- 定義（Definition）
- 参照（Reference）

### 3.3 Attachment / Supplement
- 図表
- 付録
- 参考資料

## 4. 文書責務（Document Responsibilities）
### 4.1 A層の原則を具現化
文書は A0000（理念）・A0100（抽象規範）の要求を満たす形で階層構造を持つ。

### 4.2 B層とC層をつなぐ中間構造
文書フレームワークは C層（具体手法）に必要な最小限の構造を提供する。

### 4.3 不要な文書の増殖防止
文書の作成には目的・責務が必要。この基準に合わない文書は作成しない。

## 5. 文書分類（Document Categories）
DocFoundary の文書は次の種類に分類する。

- **STD**：標準文書
- **POL**：方針文書
- **ARC**：アーキテクチャ文書
- **DOC**：説明文書

文書コードは C層で詳細化される。

## 6. 文書の状態管理（Lifecycle）
- **Draft**：初期作成
- **Review**：レビュー段階
- **Approved**：承認済み
- **Deprecated**：廃止予定

変更時はすべて識別子・日付を更新すること。

## 7. 分野間の整合性
### 7.1 A層との関係
- 本 Framework は A0000/A0100 の原則を遵守する。

### 7.2 他の B層との関係
- YAML/Spec Framework, SCD Framework, Coding Framework と論理整合を確保

### 7.3 C層との接続
- 文書生成手法、レビュー手法（C1xxx）に構造規範を提供

## 8. 付録（予定）
- 文書テンプレート
- 標準章立て
- 推奨 Front Matter 記述例

