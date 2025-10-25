
# 📘 標準文書体系（現行版）
**対象範囲:** docs/standards/  
**構成単位:** 「0100-STD-DOCS群」「0200-STD-DEVP群」  
（現存する文書のみを対象とする）

---

## 🧭 1. 目的 / *Purpose*
本ディレクトリは、あらゆる組織・プロジェクトに共通して利用可能な  
**文書管理および開発プロセス標準の中核文書群** を収録しています。  

ここに含まれる標準文書は、以下の2群に整理されます：  
- 0100-STD-DOCS群：文書管理標準（Document Standards）  
- 0200-STD-DEVP群：開発プロセス標準（Development Process Standards）  

---

## 📘 2. 0100-STD-DOCS群 — 文書管理標準

> 文書番号・命名・改訂・体系管理を定義する基盤規約。  
> すべての標準文書はこの規約のルールに従って作成されます。

| 番号 | 文書名 | 説明 |
|------|---------|------|
| [0100-STD-DOCS-DocumentPolicy](0100-STD-DOCS-DocumentPolicy.md) | 文書管理規約。番号体系・命名・改訂ルールの中核標準。 |

---

## ⚙️ 3. 0200-STD-DEVP群 — 開発プロセス標準

> Spec–Conformance Cycle に基づく、開発プロセスの標準化群。  
> 仕様・契約・テスト・実装・運用を一貫的に統制します。

| 番号 | 文書名 | 概要 |
|------|---------|------|
| [0200-STD-DEVP-CycleGuide](0200-STD-DEVP-CycleGuide.md) | Spec–Conformance 開発手法の循環モデル（統合ガイド）。 |
| [0210-STD-DEVP-Templates](0210-STD-DEVP-Templates.md) | ReqID, ADR, Matrix などの標準テンプレート集。 |
| [0220-STD-DEVP-OpsIntegrationGuide](0220-STD-DEVP-OpsIntegrationGuide.md) | 開発サイクルを運用・CI/CDへ統合する実践指針。 |

---

## 🔗 4. 群間の関係と依存方向

```
0100-STD-DOCS群 → 0200-STD-DEVP群
```

- **0100群** は命名・番号・改訂ルールの基盤を提供します。  
- **0200群** はその基盤上で、Spec–Conformance 開発プロセスを定義します。  
- 双方は独立運用可能ですが、常に一方向の参照関係を維持します。

---

## 🧩 5. 運用・改訂指針

- 各文書は、`0100-STD-DOCS-DocumentPolicy` に定める命名・改訂ルールに準拠すること。  
- 改訂は Pull Request 経由で行い、履歴を明確に残すこと。  
- 新規標準を追加する場合は、番号体系に従い「03xx」以降を予約して拡張可。  

---

## 🧾 6. 改訂履歴

| 版 | 日付 | 内容 |
|----|------|------|
| v1.0 | 2025-10-09 | 「0100群」「0200群」構成による現行版 README 新規作成。 |

---

**Status:** Draft  
**Location:** `docs/standards/README.md`

## 目次（目安の参照順）

1. **文書運用ポリシー層（1-doc/）**
   - [G0100-STD-DOC0-DocumentPolicy](1-doc/G0100-STD-DOC0-DocumentPolicy.md)
   - [G0101-STD-DOC1-CompliancePack](1-doc/G0101-STD-DOC1-CompliancePack.md)

2. **開発サイクル定義層（2-scd/）**
   - [G0200-STD-SCD0-CycleOverview](2-scd/G0200-STD-SCD0-CycleOverview.md)
   - [G0201-STD-SCD1-SpecPhase](2-scd/G0201-STD-SCD1-SpecPhase.md)
   - [G0202-STD-SCD2-ContractPhase](2-scd/G0202-STD-SCD2-ContractPhase.md)
   - [G0203-STD-SCD3-TestPhase](2-scd/G0203-STD-SCD3-TestPhase.md)
   - [G0204-STD-SCD4-ImplPhase](2-scd/G0204-STD-SCD4-ImplPhase.md)
   - [G0205-STD-SCD5-ConformancePhase](2-scd/G0205-STD-SCD5-ConformancePhase.md)
   - [G0206-STD-SCD6-FeedbackPhase](2-scd/G0206-STD-SCD6-FeedbackPhase.md)

3. **テンプレート／マップ**
   - [G0210-STD-SCDT-Templates](2-scd/G0210-STD-SCDT-Templates.md)
   - [G0220-STD-SCDM-PhaseActionMap](2-scd/G0220-STD-SCDM-PhaseActionMap.md)

---

## 参照ルール（Reference Rules）

- **正式名称**：本体系は「SCD（Spec–Conformance Development）」で統一します。旧称 *SCD³* は使用しません。
- **単一真実源（SSoT）**：契約仕様（Contract Schema）を唯一の参照源とし、自動生成成果物の直接改変を禁止します。
- **テンプレートの徹底**：T1（ReqID一覧）、T2（Conformance Matrix）、T3（ADR）、T4（Deviation）は全フェーズで必須です。
- **トレーサビリティ**：ReqID ⇄ Test ⇄ Impl ⇄ ADR ⇄ Deviation を相互リンクで維持します。
- **版管理**：Semantic Versioning（MAJOR.MINOR.PATCH）で統一し、Breaking変更はMAJORで示します。
- **承認責任**：自動検証（CI）は必須ですが、最終承認は人が行います（Human-in-the-Loop）。
