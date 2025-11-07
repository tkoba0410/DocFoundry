---
schema: "https://schema.org/CreativeWork"
@type: "CreativeWork"
identifier: "G0110-STD-DOCO-OperationalPolicy"
name: "Personal Software Documentation Operational Policy"
version: "v4.2.1"
datePublished: "2025-11-12"
status: "Approved"                     # ← G0400と統一
creator:
  @type: "Person"                      # ← G0400に合わせJSON-LD形式
  name: "Individual Developer"
description: "Defines unified operation, revision, and publication management policy compliant with Format Policy v4.3.0."

---

# [STD-DOCO] 文書運用・保守規約（Operational Policy v4.2.0）

> 本規約は、個人または小規模チームによるソフトウェア開発活動における文書の**運用・改訂・保守・公開管理**を統一することを目的とする。  
> G0100-STD-DOCF-FormatPolicy v4.3.0 に完全準拠し、Markdown構造、Front Matter、履歴管理、セキュリティおよびCI検証の運用基準を定義する。

---

## 目次
- [1. 目的と適用範囲](#1-目的と適用範囲)
- [2. バージョン管理規定](#2-バージョン管理規定)
- [3. 改訂履歴規定](#3-改訂履歴規定)
- [4. セキュリティおよびプライバシ管理](#4-セキュリティおよびプライバシ管理)
- [5. 改訂手順と運用フロー](#5-改訂手順と運用フロー)
- [6. CI連携と自動検証](#6-ci連携と自動検証)
- [7. Markdown表記標準（準拠）](#7-markdown表記標準準拠)
- [8. 関連規約](#8-関連規約)
- [9. 改訂履歴](#9-改訂履歴)

---

## 1. 目的と適用範囲
- 対象：個人および小規模チーム開発における技術文書の公開・保守・履歴管理。  
- 形式：Markdown文書（G0100準拠形式）。  
- 本規約は G0100 を前提とし、運用ルール層として適用する。  

---

## 2. バージョン管理規定（MUST）
| 区分 | 意味 | 例 |
|------|------|----|
| MAJOR | 構造・章変更（非互換） | v2.0.0 |
| MINOR | 内容追加（互換維持） | v2.1.0 |
| PATCH | 軽微修正・文言更新 | v2.1.1 |

- すべての文書は `vX.Y.Z` 形式（`v`付き）を使用する（MUST）。  
- バージョンはFront Matter・表紙・履歴の全てで一致させる（MUST）。  
- 改訂時には、変更区分に基づきバージョン番号を適切に昇格させる（SHOULD）。  

---

## 3. 改訂履歴規定（MUST）
1. 各文書末尾に「改訂履歴（Revision History）」表を設ける（MUST）。  
2. 表は **「版」「日付」「内容」** の3列を基本とする。  
3. 記録順序は **降順（最新上位）** とする。  
4. 日付形式は `"YYYY-MM-DD"`（ISO 8601）に統一する。  
5. 改訂内容は1行で簡潔に記述する（MAY）。  
6. 補助的に `CHANGELOG.md` ファイルを併用してもよい（SHOULD）。

---

## 4. セキュリティおよびプライバシ管理

### 4.1 公開前チェックリスト（SHOULD）
- 機密情報（APIキー、認証情報、内部URL）が含まれていない。  
- 個人特定情報（PII）を含まない。  
- 添付資料・画像の公開可否を確認した。  
- 外部リンク先の安全性を確認した。  
- 引用・ライセンス表記を適切に記載した。  
- 保存先のアクセス権限を確認した（閲覧・編集）。  

### 4.2 情報分類ラベル
| 区分 | 意味 | 例 |
|------|------|----|
| Public | 公開文書 | GitHub・Web公開可 |
| Internal | 内部用 | 非公開の個人資料・メモ |
| Confidential | 機密文書 | 個人情報・商用情報を含む非公開資料 |

- `confidentiality` フィールドにこれらの値を設定する（MUST）。

---

## 5. 改訂手順と運用フロー
1. 改訂時は以下の順に作業する（推奨）：  
   1. 文書内容を更新。  
   2. バージョン番号を昇格。  
   3. 改訂履歴表に記載。  
   4. ファイルを保存し、必要に応じてGitなどで管理。  
2. 軽微修正（誤記・表記揺れ）はPATCH扱いとする。  
3. 内容追加はMINOR、構成変更はMAJORとする。  
4. **レビュー方針（明確化）**：  
   - 個人開発の場合、レビューは任意とする。  
   - 共同開発・チーム運用時は、次の2段階承認を推奨する（SHOULD）：  
     1. **技術レビュー**（内容確認）  
     2. **文書レビュー**（構成・命名・整合性確認）  
   - これらはPull Requestまたは共同レポジトリ内レビュー機能を用いて実施できる。  

---

## 6. CI連携と自動検証（SHOULD）
- 文書の品質と構造一貫性を保つため、CIツールを用いた自動検証を推奨する。  
- 推奨構成：  
  - **DocLint** または **Markdownlint** により以下を検証：  
    1. ファイル名形式（G0100準拠）  
    2. H1タイトル整合（`[CAT-CODE]` 構文）  
    3. Front Matter必須キー存在  
  - **GitHub Actions / GitLab CI** を用いた自動検証例：  
    ```yaml
    name: Doc Validation
    on: [push, pull_request]
    jobs:
      lint:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - name: Run Markdown Lint
            uses: avto-dev/markdown-lint@v1
          - name: Validate Front Matter
            run: python tools/doclint.py docs/
    ```  
- 自動検証は個人・チーム双方で利用可能。  
- CI結果はコミット時の品質保証記録として活用できる。  

---

## 7. Markdown表記標準（準拠）
本規約は、Markdown表記ルールを以下の外部標準に準拠するものとする：

- **GitHub Flavored Markdown (GFM) Specification**  
  <https://github.github.com/gfm/>  
  （CommonMarkに準拠し、表・チェックリスト・リンク等を拡張）

- **CommonMark Specification**  
  <https://spec.commonmark.org/>  
  （Markdownのコア仕様としての整合性を保証）

> GFM準拠環境（GitHub, GitLab, VSCode等）では、本規約のMarkdown構造が完全に再現されることを前提とする。

---

## 8. 関連規約
- Format Policy（G0100-STD-DOCF-FormatPolicy v4.3.0）  
- CreativeWork schema（schema.org）  
- Semantic Versioning 2.0.0

---

## 9. 改訂履歴
| 版 | 日付 | 内容 |
|----|------|------|
| v4.2.0 | "2025-11-12" | 共同開発レビューおよびCI自動検証を明文化。曖昧性を完全排除。 |
| v4.1.0 | "2025-11-11" | TOCおよびGFM準拠明記を追加。Format Policy v4.3.0に完全準拠。 |
| v4.0.1 | "2025-11-08" | 文書識別子を `G0110-STD-DOCO-OperationalPolicy` に改訂。 |
| v4.0.0 | "2025-11-08" | Operational Policy初版（Format Policy準拠）。 |
