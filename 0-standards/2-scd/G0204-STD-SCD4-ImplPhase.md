---
schema: "https://schema.org/CreativeWork"
doc_id: "G0204-STD-SCD4"
title: "実装フェーズガイド（v3.0統一構成）"
version: "v3.0.0"
date: "2025-10-15"
status: "Approved"
lifecycle: "Canonical"
scope: "Generic"
owner: "Standards-Governance-Team"
reviewers:
  - "Implementation-Engineering-Guild"
  - "Quality-Assurance-Guild"
confidentiality: "Public"
---

# [SCD-IMPL] 実装フェーズガイド（v3.0統一構成）

**Version:** v3.0.0
**Date:** 2025-10-15
**Status:** Approved

---

## 1. フェーズ概要（Purpose & Scope）

本フェーズの目的は、テスト（Example／Spec）で定義された要件を、
**Test‑Driven Development（TDD）** に基づいて実装へと具現化することである。

すべての実装はテストを起点に行われ、品質を落とさず継続的開発を可能にする。

目的：
- 仕様・テストと完全に整合した実装を行う。
- Red→Green→Refactor サイクルを徹底する。
- CI／ADR／T2ログで実装履歴を追跡可能にする。

---

## 2. フェーズ原則（Principles）

| No | 原則名 | 内容 |
|:--|:--|:--|
| 1 | **Specification‑Driven Implementation** | 実装は仕様とテストに従い、意図を超える機能を追加しない。 |
| 2 | **Test‑First Development** | コードを書く前にテストを書く。失敗から正解を導く流れを守る。 |
| 3 | **Refactor Continuously** | テスト通過後も設計品質を保ち改善を続ける。 |
| 4 | **Traceable & Auditable** | ReqID ⇄ Test ⇄ Implementation ⇄ ADR ⇄ T2 が追跡可能であること。 |
| 5 | **CI Integration** | すべての変更はCIジョブで自動検証される。 |

---

## 3. 実務ガイド（Practical Flow）

| ステップ | 内容 | 担当 | AI支援（MAY） | 成果物 |
|:--|:--|:--|:--|:--|
| ① Red | 失敗するテストを作成 | 開発者 | テスト雛形生成 | 初版テスト |
| ② Green | テストを通す最小実装を記述 | 開発者 | コード提案・差分要約 | 実装コード |
| ③ Refactor | 機能を変えずに構造改善 | 開発者／レビュワー | リファクタ提案 | 改善済コード |
| ④ CI検証 | 自動テスト実行・結果記録 | CI管理者 | 結果整形・要約 | **T2: AI Validation Log** |
| ⑤ PR承認 | 100%成功したPRのみ承認 | QA責任者 | 差分整合チェック | **T3: ADR（判断記録）** |

---

## 4. 成果物（Deliverables）

| 成果物 | 形式 | 内容 | 備考 |
|:--|:--|:--|:--|
| **実装コード** | ソースコード | 仕様を満たす最小実装 | `src/` |
| **自動テスト** | Unit／Integration | ReqIDに基づく検証 | `tests/` |
| **Conformance Matrix** | Markdown／JSON | ReqID⇄Test⇄Impl対応表 | CIで更新 |
| **T2: AI Validation Log** | JSON／Markdown | CI実行結果の記録 | 自動生成 |
| **T3: ADR** | Markdown | 設計・判断・リファクタ理由 | PR連携 |

---

## 5. チェックリスト（Checklist）

| No | 確認項目 | 判定 | 意義 |
|:--|:--|:--|:--|
| 1 | 全ReqIDに対応するテストが存在する | ☐ | 仕様と実装の整合性 |
| 2 | 全テストが通過（Green）状態である | ☐ | 実装完了確認 |
| 3 | コーディング規約・Lintに準拠している | ☐ | 品質統一 |
| 4 | Matrix／ADR／T2が更新済み | ☐ | 追跡可能性維持 |
| 5 | 設計品質（リファクタ後）を維持している | ☐ | 技術的負債防止 |
| 6 | CIジョブが100%成功している | ☐ | 自動検証完了 |
| 7 | PR単位が1目的で明確である | ☐ | 履歴追跡性 |

> **完了基準:** 全項目がチェック済みであれば「実装フェーズ完了（MUST）」とする。

---

## 6. 付録（Appendix）

### A. 簡易TDD例
```python
# Red: まだ存在しない関数をテスト
def test_add():
    assert add(1, 2) == 3

# Green: 必要最小限の実装
def add(a, b):
    return a + b

# Refactor: 構造改善（冗長性除去など）
```

### B. 用語定義（Glossary, L1〜L3対応）
| 用語 | レベル | 定義 |
|:--|:--|:--|
| **Red／Green／Refactor** | L1 | TDDの3段階。失敗→通過→改善を繰り返す手法。 |
| **TDD（Test‑Driven Development）** | L1 | テストを先に書く開発手法。 |
| **T2** | L2 | AI Validation Log：テスト結果の自動記録。 |
| **T3** | L2 | ADR：設計・変更理由を記録。 |
| **CI/CD** | L3 | 継続的統合・継続的デプロイメントの自動化概念。 |

### C. Pull Request運用ルール
- 1PR＝1目的（例：ReqID追加、ADR修正、Deviation対応）
- CI成功（100% Pass）以外のPRはマージ禁止（MUST NOT）
- PRタイトル命名例：
  - `feat(req): add API-R003 retry policy`
  - `fix(test): update timeout scenario for API-R002`

### D. 参照文書
- G0203‑STD‑SCD3‑TestPhase（テスト策定フェーズ）
- G0210‑STD‑SCDT‑Templates（共通テンプレート集）
- G0220‑STD‑SCDM‑PhaseActionMap（実務行動マップ）

---

## 8. 改訂履歴 / *Revision History*

| Version | Date | Description |
|:--|:--|:--|
| v3.0.0 | 2025-10-15 | DCMMメタデータ更新と実装フェーズ標準の整合。 |

---

**End of Document**
