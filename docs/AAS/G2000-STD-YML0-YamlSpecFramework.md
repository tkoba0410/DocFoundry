---

schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "B2000-STD-YML0-YamlSpecFramework"
name: "DocFoundary YAML/Spec フレームワーク"
version: "v1.0.0"
datePublished: "2025-11-15"
inLanguage: ["ja"]
creator:
  "@type": "Person"
  name: "Framework Maintainer"
description: "DocFoundary Framework における YAML/Spec 領域（仕様・チェックリスト・指示書などの構造化表現）の構造・責務・アーティファクト構成を定義する分野フレームワーク文書。A層の抽象原則に基づき、AI が扱いやすい機械可読フォーマットとしての要件を明確化し、C層の具体的 YAML 手法へ橋渡しする。"

---

# [YML] DocFoundary YAML/Spec フレームワーク（Yaml / Spec Framework）

## 1. 目的
本書は DocFoundary Framework の B層（分野フレームワーク）の一部として、仕様・チェックリスト・指示書などを機械可読な構造化フォーマットで扱うための基盤規範を定義する。A層で定義された構造化表現・機械可読性・最小原則に従い、C層における具体的な YAML/Spec 手法の前提となる枠組みを提供する。

## 2. 適用範囲
- 仕様記述（API仕様、ドメインモデル仕様、業務フロー仕様など）
- チェックリスト（レビュー・テスト・リグレッションなど）
- 指示書（AI プロンプト／実装・テスト生成指示など）
- これらを表現する機械可読な構造化フォーマット全般

## 3. アーティファクト構成（Artifact Types）
YAML/Spec フレームワークは、少なくとも以下の 3 種のアーティファクトで構成される。

### 3.1 Spec（仕様）
- システムやドメインの振る舞い・構造を定義する
- 人間用文書（仕様書）と 1:1 あるいは N:1 で対応する

### 3.2 Checklist（チェックリスト）
- Spec に対して「満たすべき条件」や「確認すべき観点」を列挙する
- レビュー・テスト・リグレッション等の観点を構造化

### 3.3 Instruction（指示書）
- AI や開発者に対して「どの Spec/Checklist をどのように利用するか」を指示する
- プロンプトテンプレート、生成手順、検証手順などを含む

## 4. 抽象原則との関係（A層との整合）

### 4.1 Structured Representation
- Spec/Checklist/Instruction は、構造化され、参照・ID・型を明示したモデルを持つ

### 4.2 Single Source of Truth
- 文書と Spec は 1 つの真実の源に従い、矛盾した定義を持たない
- 必要であれば文書と Spec のどちらをソースとするかを明示する

### 4.3 Technology-Agnostic
- 実装フォーマット（YAML/JSON/他）は C層の責務とし、本書では抽象構造のみを扱う

### 4.4 AI Readability
- AI が安定して解釈できるよう、粒度・命名・ID・参照方法を規格化する

## 5. レイヤ構造との対応

```text
A層（理念）
 ├─ A0000 CorePrinciples
 └─ A0100 MetaFrameworkRules
    └─ 構造化表現・参照・Artifact モデル

B層（本書）
 └─ B2000 YamlSpecFramework
      ├─ Spec / Checklist / Instruction の役割定義
      └─ C層に渡す抽象構造の要求

C層（個別手法）
 ├─ C2110 SpecDesignMethod
 ├─ C2120 ChecklistPatterns
 └─ C2130 InstructionPatterns
```

## 6. YAML/Spec フレームワークの責務
- A層の抽象原則を YAML/Spec 領域に適用可能な形で具体化する
- 分野固有のアーティファクト（Spec/Checklist/Instruction）の関係を定義する
- C層の具体的 YAML スキーマ・テンプレートが従うべき制約を示す

## 7. 今後の拡張
- 分野別の Spec プロファイル（API, Domain, Flow など）を C層で定義
- チェックリストや指示書の共通パターンを C層に追加
- AI 専用の Instruction 拡張（対話履歴・役割分担など）を検討

