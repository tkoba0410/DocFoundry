
# 🧱 DocFoundry
**A Personal Documentation Standards Foundry**  
再利用可能なテンプレートとポリシーを鍛える、個人開発者のための文書標準工房。

---

## 🧭 1. 概要 / *Overview*
**DocFoundry** は、あらゆるプロジェクトで再利用可能な  
文書構成・命名規則・開発プロセス標準を体系化した  
**個人開発者向けの汎用文書標準リポジトリ**です。  

目的は次のとおりです：

- プロジェクトごとに文書体系を再設計する手間を省く  
- 命名・分類・改訂ルールを一貫化し、再利用しやすくする  
- Markdown ベースでシンプルに維持できる標準群を提供する  

---

## ⚙️ 2. 構成 / *Structure*
本リポジトリは以下の文書群で構成されます：

| 群 | 名称 | 主な内容 |
|----|------|----------|
| **0100-STD-DOCS群** | 文書管理標準 | 命名・分類・改訂・履歴管理の統一ルール。 |
| **0200-STD-DEVP群** | 開発プロセス標準 | Spec–Conformance Cycle に基づく開発プロセス標準。 |

---

## 📘 3. 主要文書 / *Core Standards*

| ファイル | 説明 |
|-----------|------|
| `0100-STD-DOCS-DocumentPolicy.md` | 文書番号体系と命名規則の中核規約。 |
| `0200-STD-DEVP-CycleGuide.md` | 開発サイクルの統合ガイド。 |
| `0210-STD-DEVP-Templates.md` | ReqID・ADR・Matrix テンプレート集。 |
| `0220-STD-DEVP-OpsIntegrationGuide.md` | 運用・CI/CD 統合ガイドライン。 |

---

## 🧩 4. 特徴 / *Key Features*
- ✅ **完全汎用化**：特定のプロジェクトや技術領域に依存しない。  
- ⚙️ **シンプル構造**：Markdown ファイルのみで管理。  
- 🔁 **再利用可能**：他プロジェクトへのコピー＆リンク運用が容易。  
- 🧱 **拡張自在**：Annex 形式（例：`0990-STD-ANX-*`）で拡張可能。  

---

## 🚀 5. 利用方法 / *Usage*
1. 任意のプロジェクトに `docs/standards/` フォルダとしてコピー。  
2. 自分の開発ルールや文書カテゴリに合わせてテンプレートを調整。  
3. `0100-STD-DOCS-DocumentPolicy.md` に基づき、番号体系と命名を統一。  
4. Git の改訂履歴を用いて標準文書の改訂を管理。  

---

## 🧱 6. 拡張ガイド
- 追加標準は「03xx」以降の番号を使用。  
- プロジェクト専用文書を追加する場合は「0990-STD-ANX-*」形式で命名。  
- 各文書は Front Matter（YAML）を持ち、CI/Lint による検証も想定。  

---

## 🧾 7. 改訂履歴
| 版 | 日付 | 内容 |
|----|------|------|
| v1.0.0 | 2025-10-10 | 初版作成（個人開発者向け汎用版として分離）。 |

---

## ⚖️ 8. ライセンス
MIT License（または個人利用ポリシーに応じて変更可）

---

## 🪶 9. 作者表記（任意）
> Maintained by **the DocFoundry Project**  
> (No personal identifiers included)

---

### 💡 GitHub リポジトリ説明文（Description 用）
> 🧱 A personal documentation standards foundry for reusable templates and policies.  
> 再利用可能なテンプレートとポリシーを鍛える、個人開発者向け文書標準工房。
