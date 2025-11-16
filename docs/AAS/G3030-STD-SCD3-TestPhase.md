---
schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0203-STD-SCD3-TestPhase"
name: "テスト策定フェーズガイド"
version: "v1.1.0"
datePublished: "2025-11-14"
inLanguage: ["ja"]
creator:
  "@type": "Person"
  name: "Individual Developer"
description: "テスト策定フェーズガイド"
---

# [SCD-TEST] テスト策定フェーズガイド（v3.0統一構成）

**Version:** v1.0.0
**Date:** 2025-10-15
**Status:** Approved

---

## 1. 表紙情報
- 文書番号: `G0203-STD-SCD3`
- バージョン: **v1.0.0**
- 日付: 2025-10-15
- 状態: Approved

---


## 2. フェーズ概要（Purpose & Scope）

本フェーズの目的は、仕様（Spec）および契約（Contract）をもとに、
**動かして確認できる仕様（Executable Specification）** を定義することである。

Example（例示仕様）を作成し、CIで自動的に検証される状態を確立する。

目的：
- 仕様の曖昧さをなくし、全員が同じ動作を想定できるようにする。
- ReqIDに基づき、Exampleとして動作を確認可能にする。
- 自動テスト結果（T2ログ）と設計判断（T3）を連携する。

---

## 3. フェーズ原則（Principles）

| No | 原則名 | 内容 |
|:--|:--|:--|
| 1 | **Behavior‑Driven** | テストは「どう動作するか」を明確に記述する。Exampleは仕様の一部である。 |
| 2 | **Executable Specification** | Exampleはドキュメントではなく、実際に動かして確認する仕様書である。 |
| 3 | **Traceable** | ReqID Example Result ADR T2 を相互に結びつける。 |
| 4 | **Automated Validation** | ExampleはCIで自動実行され、T2ログとして保存される。 |
| 5 | **Human Oversight** | 最終承認は人間が行う（MUST）。 |

---

## 4. 実務ガイド（Practical Flow）

| ステップ | 内容 | 担当 | AI支援（MAY） | 成果物 |
|:--|:--|:--|:--|:--|
| ① 定義 | ReqIDごとにExampleを作成（Given/When/Then形式） | QA／設計担当 | Example雛形生成 | Example初稿 |
| ② レビュー | Exampleの妥当性・一貫性を確認 | QA／開発者 | 曖昧語検出 | 修正版Example |
| ③ 承認 | Exampleを正式テスト仕様として登録 | QA責任者 | 整合判定・承認補助 | **Test vX.Y.Z** |
| ④ CI実行 | 自動テスト実行・結果をT2に記録 | CI管理者 | ログ整形・要約 | **T2: AI Validation Log** |
| ⑤ 判断 | テスト結果・逸脱内容をADRに記録 | QA責任者 | 結果要約生成 | **T3: ADR** |

---

## 5. 成果物（Deliverables）

| 成果物 | 形式 | 内容 | 備考 |
|:--|:--|:--|:--|
| **Example（Gherkin）** | `.feature` | ReqID単位の実行可能仕様 | `tests/features/` |
| **Test Reports** | HTML／JSON | CI結果レポート | 自動生成 |
| **T2: AI Validation Log** | JSON／Markdown | 自動実行結果ログ | CI出力 |
| **T3: ADR** | Markdown | テスト判断・変更理由 | `docs/adr/` |
| **Conformance Matrix** | Markdown | ReqID Example Result | 自動更新 |

---

## 6. チェックリスト（Checklist）

| No | 確認項目 | 判定 | 意義 |
|:--|:--|:--|:--|
| 1 | 全ReqIDに対応するExampleが定義されている | | 仕様網羅性の確認 |
| 2 | Exampleが仕様どおりに動作している | | 一貫性維持 |
| 3 | 曖昧な表現が修正されている | | テスト精度確保 |
| 4 | ADR（T3）がリンクされている | | 判断の追跡性 |
| 5 | 未解決の逸脱（Deviation）がない | | 品質担保 |
| 6 | CI結果がT2に出力されている | | 自動検証完了 |
| 7 | Pass率100%を維持している | | 適合完了条件 |

> **完了基準:** 全項目がチェック済みであれば「テスト策定フェーズ完了（MUST）」とする。

---

## 7. 付録（Appendix）

### A. Example記述例（Gherkin構文）
```gherkin
Feature: Login authentication
  Scenario: 正しいユーザーがログインできる
    Given 正しいユーザー名とパスワードがある
    When ログインボタンを押す
    Then ホーム画面に遷移する
```

### B. 用語定義（Glossary, L1〜L3対応）
| 用語 | レベル | 定義 |
|:--|:--|:--|
| **Example** | L1 | 仕様を動作例として表したテスト。 |
| **Gherkin** | L1 | Given／When／Then構文による自然文テスト形式。 |
| **T2** | L2 | AI Validation Log：テストの実行結果記録。 |
| **T3** | L2 | ADR：設計・判断の記録。 |
| **CI** | L3 | Continuous Integration：自動テスト実行プロセス。 |

### C. 参照文書（References）
- G0200‑STD‑SCD0‑CycleOverview（開発サイクル概要）
- G0210‑STD‑SCDT‑Templates（共通テンプレート集）
- G0220‑STD‑SCDM‑PhaseActionMap（実務行動マップ）

---

## 8. 改訂履歴 / *Revision History*

| Version | Date | Description |
| --- | --- | --- |
| v1.0.0 | 2025-10-15 | DocFoundry 初版FIXとして再ベースライン。 |
| v3.0.0 | 2025-10-15 | DCMMメタデータ更新とSCDテスト指針の整合化。 |

---

**End of Document**
