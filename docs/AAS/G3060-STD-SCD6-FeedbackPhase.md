---
schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0206-STD-SCD6-FeedbackPhase"
name: "フィードバックフェーズガイド"
version: "v1.1.0"
datePublished: "2025-11-14"
inLanguage: ["ja"]
creator:
  "@type": "Person"
  name: "Individual Developer"
description: "フィードバックフェーズガイド"
---

# [SCD-FEEDBACK] フィードバックフェーズガイド（v3.0統一構成）

**Version:** v1.0.0
**Date:** 2025-10-15
**Status:** Approved

---

## 1. 表紙情報
- 文書番号: `G0206-STD-SCD6`
- バージョン: **v1.0.0**
- 日付: 2025-10-15
- 状態: Approved

---


## 2. フェーズ概要（Purpose & Scope）

本フェーズは、Conformance（適合確認）で検出された不適合（Deviation）を分析し、
**仕様・設計・実装・テストのいずれかを修正して閉ループ化する** 段階である。

目的：
- 不適合を放置せず、原因を特定し再試験まで完結させる。
- ADR／Spec／Contractを更新し、同一問題の再発を防ぐ。
- “Rolling Conformance” による自己修復型サイクルを完結させる。

---

## 3. フェーズ原則（Principles）

| No | 原則名 | 内容 |
|:--|:--|:--|
| 1 | **Closed‑Loop Feedback** | 不適合を検出→修正→再試験→更新→完了までを1ループで処理する。 |
| 2 | **Learning from Deviation** | 逸脱はエラーではなく改善の契機として扱う。 |
| 3 | **Traceable Update** | 修正内容は必ずADR（T3）に記録し、T4で状態を管理する。 |
| 4 | **Zero Pending Deviation** | 未解決のDeviationを残さない。 |
| 5 | **Spec Reintegration** | 修正結果をSpec／Contractに再反映して整合を保つ。 |

---

## 4. 実務ガイド（Practical Flow）

| ステップ | 内容 | 担当 | AI支援（MAY） | 成果物 |
|:--|:--|:--|:--|:--|
| ① 抽出（Extract） | Conformance結果からFail項目を抽出 | QA／AI補助 | 自動Fail検出 | **T4: Deviation Record** |
| ② 分析（Analyze） | 原因分析・影響範囲の特定 | QA／開発者／設計者 | 要因分類・依存解析 | 分析報告 |
| ③ 修正（Fix） | 必要な箇所を修正（Spec／Test／Impl） | 開発者／設計者 | 修正提案 | 修正版 |
| ④ 再試験（Re‑Test） | 修正後に再度CI実行・適合確認 | QA／CI管理者 | 自動再実行 | **T2更新** |
| ⑤ 更新（Update） | Spec／Contract／ADRを更新 | 仕様責任者／アーキテクト | 差分反映 | **T3: ADR（更新記録）** |
| ⑥ 承認（Close） | 全DeviationがClose済みであることを確認 | QA責任者 | 状態検証 | フェーズ完了報告 |

---

## 5. 成果物（Deliverables）

| 成果物 | 形式 | 内容 | 備考 |
|:--|:--|:--|:--|
| **T4: Deviation Record** | JSON／Markdown | 不適合項目と対応状況 | QA管理 |
| **T3: ADR** | Markdown | 修正内容・判断根拠・再発防止策 | 更新必須 |
| **T2: Conformance Matrix** | Markdown／CSV | 再試験結果更新後の整合表 | 自動更新 |
| **Spec／Contract更新版** | Markdown／YAML | 改訂後の仕様書 | Canonical更新 |
| **Feedback Report** | PDF／Markdown | 総括レポート | 任意 |

---

## 6. チェックリスト（Checklist）

| No | 確認項目 | 判定 | 意義 |
|:--|:--|:--|:--|
| 1 | すべてのFailがT4に登録されている | | 不適合管理の徹底 |
| 2 | 原因分析・対策がADR（T3）に記録されている | | 再発防止の根拠 |
| 3 | 修正版が再試験でPassしている | | 修正効果の確認 |
| 4 | Conformance Matrix（T2）が最新化されている | | 整合性維持 |
| 5 | Spec／Contractが更新反映済み | | 文書整合の回復 |
| 6 | 未解決Deviationが存在しない（Zero Pending） | | フェーズ完了条件 |
| 7 | Closed‑Loop完了が承認済み | | SCDサイクル完結 |

> **完了基準:** Deviation=0、全更新反映済みで「フィードバックフェーズ完了（MUST）」とする。

---

## 7. 付録（Appendix）

### A. Deviation Closeフロー（概要）
```
検出 → 登録(T4) → 分析 → 修正 → 再試験(T2) → ADR更新(T3) → Spec反映 → Close
```

### B. ADR更新例
| No | 日付 | 判断概要 | 対応内容 | 関連Deviation | 承認者 |
|:--|:--|:--|:--|:--|:--|
| ADR‑005 | 2025‑10‑23 | Timeout異常の原因特定 | 再送処理の条件を修正 | DEV‑001 | QA Lead |

### C. 用語定義（Glossary, L1〜L3対応）
| 用語 | レベル | 定義 |
|:--|:--|:--|
| **Deviation（T4）** | L1 | 不適合記録。修正が完了するまで管理される。 |
| **Feedback Loop** | L1 | 不適合を仕様更新に還元する循環構造。 |
| **ADR（T3）** | L2 | 設計判断記録。原因分析や防止策を明文化。 |
| **Re‑Test** | L2 | 修正後の再試験。CIで自動化。 |
| **Rolling Conformance** | L3 | 常時整合状態を維持する継続的SCD手法。 |

### D. 参照文書
- G0205‑STD‑SCD5‑ConformancePhase（適合確認フェーズ）
- G0210‑STD‑SCDT‑Templates（共通テンプレート集）
- G0220‑STD‑SCDM‑PhaseActionMap（実務行動マップ）

---

## 8. 改訂履歴 / *Revision History*

| Version | Date | Description |
| --- | --- | --- |
| v1.0.0 | 2025-10-15 | DocFoundry 初版FIXとして再ベースライン。 |
| v3.0.0 | 2025-10-15 | DCMM準拠メタデータ追加とフィードバック指針の整合。 |

---

**End of Document**
