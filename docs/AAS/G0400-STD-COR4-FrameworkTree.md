---

schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0400-STD-COR4-FrameworkTree"
name: "DocFoundary フレームワーク全体系ツリー"
version: "v1.0.0"
datePublished: "2025-11-15"
inLanguage: ["ja"]
creator:
"@type": "Person"
name: "Framework Maintainer"
description: "DocFoundary Framework の A/B/C/D 各層および旧体系とのマッピングを統合し、体系全体を俯瞰可能な樹形図として整理した文書。A 層に属する補助的総覧文書。"

---


# A0400-FWK-TREE-FrameworkTree（DocFoundary Framework 全体系ツリー）（A/B/C/D 層モデル・最新版）

---

## **概要（Overview）**

本書は DocFoundary Framework の **A/B/C/D 4 層モデル**に基づき、思想（A）、分野フレームワーク（B）、標準手法（C）、個別プロジェクト（D）の全体構造を俯瞰可能な形で整理したツリードキュメントである。

DocFoundary におけるすべての文書・仕様・構造化データ・AI指示書は、本体系に従って配置される。

---

# **1. A 層：理念・哲学（Foundation / Principles / Meta）**

A層は DocFoundary の最上位。思想→理念→抽象規範→全体像の順で構成される。

```
G0000-STD-COR0-Foundation
    └─ DocFoundary の背景・思想・課題認識・存在理由

G0100-STD-COR1-CorePrinciples
    └─ 揺らがない理念（SOFT / 構造化 / AI可読性 / 最小 / 一貫性）

G0200-STD-COR2-MetaFrameworkRules
    └─ Artifactモデル、層間参照、抽象構造、AI可読要求

G0300-STD-COR3-FrameworkOverview
    └─ A/B/C/D 全体の構造図・レイヤ説明

G0400-STD-COR4-FrameworkTree
    └─ A/B/C/D 全体のツリー図
```

---

# **2. B 層：分野フレームワーク（Domain Frameworks）**

A層の理念と抽象規範を受け、分野ごとに「構造・役割・責務」を定義する層。

```
G1000-STD-DOC-DocumentFramework
    ├─ 文書の構造・形式・責務
    ├─ フロントマター規範
    └─ 文書ライフサイクル（Draft/Review/Approved/Deprecated）

G2000-STD-YML-YamlSpecFramework
    ├─ Spec / Checklist / Instruction の役割
    ├─ AI可読な構造化Specの原型
    └─ C層の YAML手法への抽象的橋渡し

G3000-STD-SCD-DevelopmentFramework
    ├─ 開発サイクル全体構造（SCD）
    ├─ Phaseモデル（Spec/Contract/Impl/Conformance/Feedback）
    └─ C層手法へ展開する枠組み

G4000-STD-COD-CodingFramework
    ├─ コーディング原則
    ├─ レイヤ/責務/設計基準
    └─ 言語固有手法（C層）へのブリッジ
```

---

# **3. C 層：標準手法・テンプレート（Methods）**

C層は B層で定義された構造・規範に基づき、実際の手法・テンプレートとして具体化される層。

```
G1xxx Document Methods（文書手法）
    ├─ G1010 FormatPolicy（旧 G0100）
    ├─ G1020 AuthoringGuideline（旧 G0110）
    ├─ G1030 DocumentOperation（旧 G0120）
    └─ G1040 DivisionGuideline（旧 G0130）

G2xxx YAML / Spec Methods（構造化仕様手法）
    ├─ G2110 SpecDesignMethod（旧 G0400/G0410）
    ├─ G2120 ChecklistPatterns（旧 G0410）
    ├─ G2130 InstructionPatterns（旧 G0420）
    └─ G2140 SpecExamples / Templates

G3xxx SCD Methods（開発プロセス手法）
    ├─ G3010 SCD-SpecPhase（旧 G0201）
    ├─ G3020 SCD-ContractPhase（旧 G0202）
    ├─ G3040 SCD-ImplPhase（旧 G0204）
    ├─ G3050 SCD-Conformance（旧 G0205）
    ├─ G3060 SCD-Feedback（旧 G0206）
    └─ G3100 SCD Templates（旧 G0210）

G4xxx Coding Methods（コーディング手法）
    ├─ G4010 CodingStandard-CSharp（旧 G0301）
    └─ G4020 CodeReviewGuidelines
```

---

# **4. D 層：プロジェクト層（Project Layer）**

DocFoundary を基盤に、個別プロジェクトごとの仕様・設計・手順を記述する層。標準と混ぜないことが重要。

```
P1000 ProjectOverview
    └─ プロジェクト背景・目的・体制

P2xxx Project Specs（構造化仕様）
    ├─ P2100 ProjectSpec
    ├─ P2200 ProjectChecklist
    └─ P2300 ProjectInstruction

P3xxx Project SCD（開発プロセス適用）
    └─ 各プロジェクト固有の開発フェーズ定義

P4xxx Project Coding（個別言語/実装ガイド）
```

---

# **5. 旧体系（G0000〜G0400〜G0200〜G0300）からの移行マッピング（完全版）**

旧体系はすべて A/B/C 層にマッピングされる。

```
A層：理念
    G0500 → G0100 CorePrinciples

B層：分野フレームワーク
    G0000 → G1000 DocumentFramework
    G0200 → G3000 DevelopmentFramework
    G0300 → G4000 CodingFramework

C層：具体手法
    G0100〜0130 → G1xxx（Document Methods）
    G0400〜0420 → G2xxx（Spec Methods）
    G0201〜0206 → G3xxx（SCD Methods）
    G0301       → G4010
```

---

# **6. A/B/C/D 層の関係（全体構造図）**

```
A層：思想・理念・抽象規範
    ├─ Foundation（背景・思想）
    ├─ CorePrinciples（理念）
    ├─ MetaRules（抽象構造）
    └─ FrameworkOverview（地図）

B層：分野フレームワーク（Document / YAML / SCD / Coding）
    └─ 分野ごとの枠組みと責務

C層：標準手法・テンプレート
    └─ 文書 / YAML / SCD / コーディングの具体手法

D層：プロジェクト
    └─ 個別の仕様・チェック・AI指示書・開発運用
```

---

# **7. 本体系の意義**

* 文書体系と開発体系を一本化する
* 文章中心から**構造中心**に移行

---

## 8. 追加ツリー（詳細階層図）

```
G0000〜G0999 A層（理念・哲学）
 ├─ G0000-STD-COR0-Foundation
 ├─ G0100-STD-COR1-CorePrinciples
 ├─ G0200-STD-COR2-MetaFrameworkRules
 ├─ G0300-STD-COR3-FrameworkOverview
 └─ G0400-STD-COR4-FrameworkTree

G1000〜G4999 B層（分野フレームワーク）
 ├─ G1000-STD-DOC-DocumentFramework
 ├─ G2000-STD-YML-YamlSpecFramework
 ├─ G3000-STD-SCD-DevelopmentFramework
 └─ G4000-STD-COD-CodingFramework

G1xxx〜G4xxx C層（標準手法・テンプレート）
 ├─ G1xxx Document Methods（文書手法）
 │    ├─ G1010 FormatPolicy
 │    ├─ G1020 AuthoringGuideline
 │    ├─ G1030 DocumentOperation
 │    └─ G1040 DivisionGuideline
 │
 ├─ G2xxx YAML / Spec Methods（構造化仕様手法）
 │    ├─ G2110 SpecDesignMethod
 │    ├─ G2120 ChecklistPatterns
 │    ├─ G2130 InstructionPatterns
 │    └─ G2140 SpecExamples / Templates
 │
 ├─ G3xxx SCD Methods（開発プロセス手法）
 │    ├─ G3010 SCD-SpecPhase
 │    ├─ G3020 SCD-ContractPhase
 │    ├─ G3040 SCD-ImplPhase
 │    ├─ G3050 SCD-ConformancePhase
 │    ├─ G3060 SCD-FeedbackPhase
 │    └─ G3100 SCD-Templates
 │
 └─ G4xxx Coding Methods（コーディング手法）
      ├─ G4010 CodingStandard-CSharp
      └─ G4020 CodeReviewGuidelines

P1000〜P4xxx D層（プロジェクト）
 ├─ P1000 ProjectOverview
 ├─ P2xxx Project Specs / Checklist / Instruction
 ├─ P3xxx Project SCD（開発プロセス適用）
 └─ P4xxx Project Coding（個別言語/実装ガイド）
```

---

## 9. 表形式マッピング（旧体系 → 新 G/P 体系対応表）

| 旧体系（G旧）     | 新体系（G/P）                           | 層  | 備考                                |
| ----------- | ---------------------------------- | -- | --------------------------------- |
| G0500       | G0100-STD-COR1-CorePrinciples      | A層 | CorePrinciples に統合                |
| G0000       | G1000-STD-DOC-DocumentFramework    | B層 | 文書フレームワーク                         |
| G0100〜G0130 | G1xxx Document Methods             | C層 | FormatPolicy / Authoring など文書手法   |
| G0400〜G0420 | G2xxx YAML / Spec Methods          | C層 | Spec / Checklist / Instruction 手法 |
| G0200       | G3000-STD-SCD-DevelopmentFramework | B層 | SCD 開発フレームワーク                     |
| G0201〜G0206 | G3xxx SCD Methods                  | C層 | 各SCDフェーズの具体手法                     |
| G0210       | G3xxx SCD Templates                | C層 | SCD テンプレート類                       |
| G0300       | G4000-STD-COD-CodingFramework      | B層 | コーディングフレームワーク                     |
| G0301       | G4xxx Coding Methods               | C層 | 言語別コーディング手法（C# など）                |

（必要に応じて、分野別にさらに詳細なサブツリーやマッピング表を追加できる。）
