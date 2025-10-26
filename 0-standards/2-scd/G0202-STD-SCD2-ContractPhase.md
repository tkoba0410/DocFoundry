---
doc_id: G0202-STD-SCD2-ContractPhase
title: 契約確立フェーズガイド（v3.0統一構成）
version: 3.0.0
date: 2025-10-XX
scope: ExchangeApi Standard
lifecycle: canonical
status: Stable
---

# [STD-SCD2] 契約確立フェーズガイド（v3.0統一構成）

**Version:** v3.0.0  
**Date:** 2025-10-XX  
**Status:** Stable  

---

## 1. フェーズ概要（Purpose & Scope）

本フェーズは、仕様（Spec）で定義された要求を技術的契約（Contract）として固定する段階である。  
Contract-First 原則に基づき、**全チームが共有する唯一の真実源（Single Source of Truth）** を確立することを目的とする。  

目的：  
- API／DTO／Schema を正式な契約仕様として定義する。  
- 各フェーズが同一の契約仕様を参照する基盤を作る。  
- Breaking 変更を検知・管理し、安定した開発を維持する。

---

## 2. フェーズ原則（Principles）

| No | 原則名 | 内容 |
|:--|:--|:--|
| 1 | **Contract-First** | 実装やテストよりも先に契約（API／DTO／Schema）を確定させる。 |
| 2 | **Single Source of Truth (SSoT)** | 契約仕様を唯一の信頼情報源とし、他文書に依存しない。 |
| 3 | **Non‑Modifiable** | 自動生成物は手動で修正しない（MUST NOT）。変更は契約の更新として扱う。 |
| 4 | **Version Control (SemVer)** | 契約は Semantic Versioning に基づいて管理する。 |
| 5 | **Decision Traceability** | 変更や設計判断は必ず ADR（T3）に記録し、追跡可能にする。 |

---

## 3. 実務ガイド（Practical Flow）

| ステップ | 内容 | 担当 | AI支援（MAY） | 成果物 |
|:--|:--|:--|:--|:--|
| ① 定義（Define） | 契約境界（IF／DTO／Schema）を定義 | 設計責任者 | Schema雛形提案 | 初版Schema |
| ② 固定（Fix） | 契約を承認し、バージョンを固定 | 承認者（設計＋QA） | 破壊的変更の自動判定 | **Contract vX.Y.Z** |
| ③ 検証（Validate） | 契約差分と生成物の整合をCIで確認 | QA／CI管理者 | 契約整合チェック、AI Validation Log出力 | **T2: AI Validation Log** |
| ④ 記録（Record） | 変更理由・決定内容をADRに登録 | アーキテクト／設計責任者 | 自動テンプレ補助 | **T3: ADR** |

---

## 4. 成果物（Deliverables）

| 成果物 | 形式 | 内容 | 備考 |
|:--|:--|:--|:--|
| **Contract Schema** | YAML／JSON／Proto | 契約仕様（SSoT） | `contracts/` 配下 |
| **Generated Artifacts** | ソースコード | 自動生成されたコード | 改変禁止 |
| **Contract Tests** | テストスイート | MUSTエンドポイント検証 | CI必須 |
| **T3: ADR** | Markdown | 契約変更の設計判断記録 | PR連携／`docs/adr/` |
| **T2: AI Validation Log** | JSON／Markdown | 契約検証ログ | CI出力 |

---

## 5. チェックリスト（Checklist）

| No | 確認項目 | 判定 | 意義 |
|:--|:--|:--|:--|
| 1 | 契約（IF／DTO／Schema）が Contract‑First で確定している | ☐ | 上流整合性の確保 |
| 2 | 契約が唯一の真実源（SSoT）として運用されている | ☐ | 情報源の一元化 |
| 3 | 自動生成物が改変されていない（Non‑Modifiable） | ☐ | 品質維持・差分防止 |
| 4 | 互換性規約に基づき差分が判定されている | ☐ | 破壊的変更の防止 |
| 5 | Breaking変更時にADR（T3）が登録されている | ☐ | 設計判断の透明性 |
| 6 | CIで契約整合が確認されている | ☐ | 自動化による保証 |
| 7 | 契約バージョン（SemVer）が明示されている | ☐ | 更新履歴の明確化 |

> **完了基準:** 全項目がチェック済みであれば「契約確立フェーズ完了（MUST）」とする。

---

## 6. 付録（Appendix）

### A. 用語定義（Glossary, L1〜L3対応）
| 用語 | レベル | 定義 |
|:--|:--|:--|
| **Contract‑First** | L1 | 契約仕様を最初に設計・固定する開発原則。 |
| **Schema** | L1 | API／DTO構造を形式的に記述した仕様定義。 |
| **ADR（T3）** | L2 | Architecture Decision Record。設計判断と理由の記録。 |
| **Breaking Change** | L2 | 後方互換性を破壊する変更。 |
| **SSoT（Single Source of Truth）** | L3 | 唯一の信頼情報源。契約仕様が基準となる。 |

### B. 参考ツール例
- `spectral lint`：OpenAPI／JSON Schemaのルール検証  
- `buf breaking check`：gRPC／Protobufの互換性検証  
- `ADR-Tools`：ADR作成・履歴管理自動化ツール  

### C. 参照文書
- G0200‑STD‑SCD0‑CycleOverview（開発サイクル概要）  
- G0210‑STD‑SCDT‑Templates（共通テンプレート集）  
- G0320‑STD‑SCDM‑PhaseActionMap（実務行動マップ）  

---

**End of Document**
