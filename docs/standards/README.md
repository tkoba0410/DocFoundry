
# 📘 Exchange API Library — 標準文書体系（現行版）
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
