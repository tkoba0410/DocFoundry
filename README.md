# リポジトリ概要（standards + project-template 構成）

このリポジトリは、開発標準文書（standards）と、プロジェクト雛型（project-template）を同居させた構成です。  
小規模導入や初期試行段階での運用を想定しており、2件目以降のプロジェクト開始時に standards を独立リポジトリとして分離することを前提としています。

---

## 📘 構成の目的

- **standards/** : 全プロジェクト共通の「汎用開発標準文書群」  
  文書方針（DocumentPolicy）、準拠基準（CompliancePack）、SCDモデル、コーディング標準などを含みます。
- **project-template/** : 各プロジェクトがコピーして利用する「導入雛型」  
  config／docs／ci／src／tests など、標準に準拠した構成を初期から提供します。

---

## 📂 ディレクトリ構成

```plaintext
repo-root/
├── standards/
│   ├── 1-doc/
│   │   ├── G0100-STD-DOC0-DocumentPolicy.md
│   │   ├── G0101-STD-DOC1-CompliancePack.md
│   │   ├── G0102-STD-DOC2-ProjectAdaptationGuide.md
│   │   ├── G0103-STD-DOC3-CodingStandard.md
│   │   └── lang/
│   │       └── G0104-STD-LANG-CS-CodingStandard.md
│   ├── 2-scd/
│   │   ├── G0200〜G0210
│   │   └── G0220-STD-SCDM-PhaseActionMap.md
│   └── README.md
│
├── project-template/
│   ├── config/
│   │   ├── project-config.yml
│   │   └── project-coding-overrides.yml
│   ├── compliance/
│   │   ├── T1-ReqID.csv
│   │   ├── T2-ConformanceMatrix.csv
│   │   ├── T3-ADR/
│   │   └── T4-Deviation/
│   ├── docs/
│   │   ├── P0200-STD-PJ0-Overview.md
│   │   ├── P0201-STD-PJ1-Architecture.md
│   │   ├── P0202-STD-PJ2-Interfaces.md
│   │   ├── P0203-STD-PJ3-TestStrategy.md
│   │   ├── P0204-STD-PJ4-Deployment.md
│   │   ├── P0205-STD-PJ5-Operation.md
│   │   ├── P0206-STD-PJ6-SecurityPolicy.md
│   │   ├── P0207-STD-PJ7-Licensing.md
│   │   └── index.md
│   ├── ci/
│   │   └── workflows/
│   │       ├── core-check.yml
│   │       ├── csharp-check.yml
│   │       └── conformance.yml
│   ├── src/
│   └── tests/
│
└── README.md
```

---

## 🧭 運用ポリシー

| 項目 | 方針 |
|------|------|
| **standards/** | 標準化チーム専用領域。プロジェクトチームは改変禁止。 |
| **project-template/** | 新規プロジェクトがコピーして使用。個別設定・文書・CIを含む。 |
| **改変手続き** | standards内の修正は Pull Request＋レビュー＋タグ付与（SemVer管理）。 |
| **コードオーナー** | `/standards/**` は CODEOWNERSで標準チーム専権。 |
| **差異管理** | `config/project-coding-overrides.yml` で Core/LANG 規約を部分上書き（ADR必須）。 |

---

## ⚙️ 利用手順（新プロジェクト開始時）

1. `project-template/` をコピーして新規プロジェクトディレクトリを作成  
   例：`cp -r project-template project-exa`
2. `config/project-config.yml` を編集し、プロジェクトIDや契約方式を設定  
3. 必要に応じて `config/project-coding-overrides.yml` を作成し、差異を定義  
4. `/docs/` 以下の雛型文書を埋めてプロジェクト仕様を記録  
5. `/ci/workflows/` に含まれる core-check / csharp-check / conformance CI を実行  
6. 検証結果（T2, T4）を `/compliance/` に保存  

---

## 🔒 標準との関係

- **参照優先順位**
  1. G0103（Coding Standard – Core）
  2. G0104（LANG-CS）
  3. project-coding-overrides.yml（承認済み差異）

- **不整合時の扱い**
  - Core／LANG 規約に反する差異は ADR（T3）で承認が必要
  - 差異の有効期限を定め、FeedbackPhase で再評価する

---

## 🪜 将来の移行計画（2プロジェクト目以降）

| ステップ | 内容 |
|----------|------|
| 1️⃣ | `/standards` を独立リポジトリ化（例：`org-standards`） |
| 2️⃣ | 本リポの standards を削除し、submodule または release zip で参照 |
| 3️⃣ | 各プロジェクトでタグ固定参照 (`v3.0.0`) を設定 |
| 4️⃣ | CIで standards バージョンの整合チェックを自動化 |
| 5️⃣ | 変更理由を ADR に記録し、Conformance で検証 |

---

## 📄 参照・連絡・改訂履歴

- 管理者: Documentation Team / QA
- バージョン: v3.0.0（SCDモデル準拠）
- ライフサイクル: Stable
- 連絡先: standards@org.example

| 版 | 日付 | 内容 |
|----|------|------|
| v1.0.0 | 2025-10-26 | 初版。standards＋project-template同居構成を正式化。 |
