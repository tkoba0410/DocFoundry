---

schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0120-STD-DOC2-DocumentOperation"
name: "ドキュメント運用標準（構造・検証・不整合管理指針）"
version: "v1.2.0"
datePublished: "2025-11-11"
inLanguage: ["ja"]
creator:
"@type": "Person"
name: "Individual Developer"
description: >
DocFoundary 標準群における文書構成・検証仕様・不整合管理の運用方式を定義する標準文書。
設計文書（docs/）、検証仕様（work/checklist/）、不整合結果（work/report/）の三層構造によって、
再現可能で誠実な AI 協働ドキュメント運用を実現する。
----------------------------

# [STD-DOC2] ドキュメント運用標準（構造・検証・不整合管理指針）

## 1. 目的（Purpose）

DocFoundary 標準群における文書（`docs/`）、検証仕様（`work/checklist/`）、検証結果（`work/report/`）の構成および運用方法を統一し、
再現可能で誠実な AI 協働ドキュメント運用を実現することを目的とする。

---

## 2. 構成原則（Principles）

1. **再現可能性（Reproducibility）**：構造と履歴の両面で再実行・再検証が可能であること。
2. **分離と整合（Separation & Coherence）**：設計文書・検証定義・検証結果を責務別に分離し、整合を維持すること。
3. **誠実性（Integrity）**：検証結果は不整合のみを出力し、虚偽の整合を避けること。
4. **継続性（Continuity）**：改訂履歴において変更点を差分で追跡可能とすること。

---

## 3. ディレクトリ構成（Directory Structure）

```plaintext
project-root/
├─ docs/                      # 設計・標準文書（正本）
│   └─ G0000-STD-OVRV-OverView.md
└─ work/
    ├─ checklist/             # チェック仕様（検証定義）
    │   └─ G0000-STD-OVRV-OverView.yml
    └─ report/                # 検証結果（不整合のみ出力）
        └─ G0000-STD-OVRV@G0110-STD-DOC0.yml
```

| フォルダ              | 内容               | 更新主体     | ファイル内容例       |
| ----------------- | ---------------- | -------- | ------------- |
| `docs/`           | 標準・設計・理念文書の正本    | 人間（開発者）  | Markdown, PDF |
| `work/checklist/` | 各文書に対応するチェック仕様定義 | 人間＋AI支援  | YAML          |
| `work/report/`    | チェック結果。不整合のみ出力   | AI／CI/CD | YAML（最小出力）    |

---

## 4. チェック運用サイクル（Operation Cycle）

| フェーズ     | 実施者      | 内容                                | 成果物                     |
| -------- | -------- | --------------------------------- | ----------------------- |
| **定義**   | 開発者      | `work/checklist/` に基準をYAML化       | チェック仕様ファイル              |
| **検証**   | AI／スクリプト | `docs/` を基に `work/checklist/` を実行 | `work/report/` に不整合のみ出力 |
| **レビュー** | 人間       | `work/report/` の指摘内容を確認・修正        | 修正版 `docs/`             |
| **再検証**  | AI       | 再実行し `work/report/` が空になることを確認    | 空ファイルまたは削除              |

---

## 5. 出力ポリシー（Error Output Policy）

AIによる検証結果は「不整合（NG／警告）」のみ出力する。出力形式は以下の最小構造とする。

```yaml
meta:
  target: "G0000-STD-OVRV-OverView"
  target_version: "v2.4.0"
  checklist: "G0110-STD-DOC0-OperationPolicy"
  executed_by: "ai"
  executed_at: "2025-11-11T10:30:00+09:00"
issues:
  - id: "PR-002"
    severity: "high"
    status: "missing"
    message: "AI最終責任の明示が不足"
    location: "2. 基本理念"
    suggestion: "人間最終判断の一文を追加"
summary:
  total_issues: 1
```

---

## 6. 整合保証（Alignment Assurance）

* `docs/` と `work/checklist/` のファイル名・識別子を完全一致させる。
* `work/report/` ファイルは自動生成物だが、レビュー履歴として残す。
* 改訂後は必ず再チェックを行い、`work/report/` が空になるまで修正を続ける。

---

## 7. 改訂管理（Revision Management）

| 版      | 日付         | 内容                                                    |
| ------ | ---------- | ----------------------------------------------------- |
| v1.2.0 | 2025-11-11 | フォルダ構成を `docs` と `work/checklist`・`work/report` に再定義。 |
| v1.1.0 | 2025-11-11 | フォルダ名称を `docs/checklist/report` に改訂。                  |
| v1.0.0 | 2025-11-11 | 初版：3層構造によるドキュメント運用方式を定義。                              |

---

## 8. 付録（Appendix）
- **上位参照標準**：
  - G0100-STD-DOC0（ドキュメント書式標準）
  - G0110-STD-DOC1（文書作成指針）
- **関連標準**：
  - G0000-STD-OVRV（理念）
  - G0410-TST-OVRV（チェック仕様）
- **推奨拡張**：
  - `work/report/` の履歴化による継続レビュー
  - CI/CDでの自動整合検証（YAMLパイプライン）
