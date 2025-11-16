---
schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0120-STD-DOC2-DocumentOperation"
name: "ドキュメント運用標準（構造・検証・不整合管理指針）"
version: "v1.4.0"
datePublished: "2025-11-12"
inLanguage: ["ja"]
creator:
  "@type": "Person"
  name: "Individual Developer"
description: >
  DocFoundary 標準群における文書構成・検証仕様・不整合管理の運用方式を定義する標準文書。
  docs／checklist／report の三層構造に共通階層（00-ovr／01-doc）を導入し、
  他階層（02-scd 以降）への拡張性を確保する。
---

# [STD-DOC2] ドキュメント運用標準（構造・検証・不整合管理指針）

## 目次（Table of Contents）

* [1. 目的（Purpose）](#1)
* [2. 構成原則（Principles）](#2)
* [3. ディレクトリ構成（Directory-Structure）](#3)
* [4. チェック運用サイクル（Operation-Cycle）](#4)
* [5. 出力ポリシー（Error-Output-Policy）](#5)
* [6. 整合保証（Alignment-Assurance）](#6)
* [7. 改訂履歴（Revision-Management）](#7)
* [8. 拡張構想（Extension-Outlook）](#8)
* [9. 推奨拡張（Recommended-Extensions）](#9)
* [10. ログ層の追加（work/log）](#10)

  * [10.1 目的（Purpose）](#10-1)
  * [10.2 ディレクトリ構成（Structure）](#10-2)
  * [10.3 ファイル命名規則（Naming-Rule）](#10-3)
  * [10.4 推奨ログ形式（YAML）](#10-4)
  * [10.5 設計意図（Design-Intent）](#10-5)
  * [10.6 ログローテーション方針（Rotation-Policy）](#10-6)
  * [10.7 他形式との比較（Format-Comparison）](#10-7)
  * [10.8 結論（Conclusion）](#10-8)

---

## 1. 目的（Purpose）

DocFoundary 標準群における文書（`docs/`）、検証仕様（`checklist/`）、検証結果（`report/`）の構成および運用方法を統一し、
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
├─ docs/
│  ├─ 00-ovr/               # 概要・理念
│  │      G0000-STD-OVRV-OverView.md
│  │
│  ├─ 01-doc/               # 文書標準群
│  │      G0100-STD-DOC0-FormatPolicy/ ...
│  │      G0110-STD-DOC1-AuthoringGuideline.md
│  │      G0120-STD-DOC2-DocumentOperation.md
│  │
│  └─ (02-scd/ ... )        # ← 拡張層例示のみ
│
├─ checklist/
│  ├─ 00-ovr/
│  │      G0000-STD-OVRV-OverView.yml
│  │
│  ├─ 01-doc/
│  │      G0100-STD-DOC0-FormatPolicy.yml
│  │      G0110-STD-DOC1-AuthoringGuideline.yml
│  │      G0120-STD-DOC2-DocumentOperation.yml
│  │
│  └─ (02-scd/ ... )        # ← 拡張層例示のみ
│
└─ report/
   ├─ 00-ovr/
   │      G0000-STD-OVRV@G0110-STD-DOC1.yml
   │
   ├─ 01-doc/
   │      G0100-STD-DOC0@G0110-STD-DOC1.yml
   │      G0110-STD-DOC1@G0120-STD-DOC2.yml
   │
   └─ (02-scd/ ... )        # ← 拡張層例示のみ
```

| 層                    | 内容             | 更新主体     | 対象      | 出力形式          |
| -------------------- | -------------- | -------- | ------- | ------------- |
| `docs/<layer>/`      | 正本文書（標準・設計・理念） | 人間       | 00-ovr〜 | Markdown, PDF |
| `checklist/<layer>/` | チェック仕様定義       | 人間＋AI    | 同上      | YAML          |
| `report/<layer>/`    | 不整合報告          | AI／CI/CD | 同上      | YAML（最小構造）    |

---

## 4. チェック運用サイクル（Operation Cycle）

| フェーズ | 実施者      | 対象例                                                     | 成果物                      |
| ---- | -------- | ------------------------------------------------------- | ------------------------ |
| 定義   | 開発者      | `checklist/01-doc/G0120-STD-DOC2-DocumentOperation.yml` | チェック仕様                   |
| 検証   | AI／スクリプト | `docs/01-doc/G0120-STD-DOC2-DocumentOperation.md`       | `report/01-doc/…` に不整合出力 |
| レビュー | 人間       | `report/` の指摘を確認・修正                                     | 改訂済 `docs/`              |
| 再検証  | AI       | 再チェックし報告空判定                                             | 整合完了                     |

---

## 5. 出力ポリシー（Error Output Policy）

```yaml
meta:
  target: "G0110-STD-DOC1-AuthoringGuideline"
  target_version: "v1.2.0"
  checklist: "G0120-STD-DOC2-DocumentOperation"
  executed_by: "ai"
  executed_at: "2025-11-12T10:30:00+09:00"
issues:
  - id: "CHK-001"
    severity: "medium"
    status: "missing"
    message: "目的節に具体的対象文書の明記が不足"
    location: "1. 目的"
    suggestion: "対象範囲に 'STD-DOC 系列' を明記すること"
summary:
  total_issues: 1
```

---

## 6. 整合保証（Alignment Assurance）

* 各階層（00-ovr／01-doc）は `docs`／`checklist`／`report` の3層で完全対応する。
* ファイル識別子（`Gxxxx-STD-****`）は階層間で完全一致させる。
* `report` は不整合のみ記録し、空であることが最終整合の証とする。
* `02-scd` 以降の階層も同構造で追加可能（拡張保証）。

---

## 7. 改訂履歴（Revision Management）

| 版      | 日付         | 内容                                         |
| ------ | ---------- | ------------------------------------------ |
| v1.4.0 | 2025-11-12 | `00-ovr／01-doc` を例示対象として構造確定。他階層は拡張例として明記。 |
| v1.3.0 | 2025-11-12 | 共通ドメイン構成（std／arc／req／imp）案を試行。             |
| v1.2.0 | 2025-11-11 | `work/` 構成を `checklist／report` に統一。        |
| v1.1.0 | 2025-11-11 | フォルダ名称を `docs/checklist/report` に改訂。       |
| v1.0.0 | 2025-11-11 | 初版：3層構造による運用方式を定義。                         |

---

## 8. 拡張構想（Extension Outlook）

| 階層候補    | 用途             | 想定標準群例      |
| ------- | -------------- | ----------- |
| 02-scd  | SCDモデル標準       | G0200〜G0220 |
| 03-cod  | コーディング標準       | G0300〜G0310 |
| 04-yaml | YAML構造標準       | G0400〜G0420 |
| 05-tst〜 | 試験・運用・セキュリティ標準 | （将来追加予定）    |

---

## 9. 推奨拡張（Recommended Extensions）

* `meta/structure.yml` に階層設定（00〜04）を定義し、自動検証基盤に反映する。
* CI/CD パイプラインで `report` 出力が空かどうかを整合条件として評価する。
* `report` 履歴を蓄積し、文書品質改善トレーサビリティを確保する。

---

## 10. ログ層の追加（work/log）

### 10.1 目的（Purpose）

* 検証サイクルの**実行履歴**（成功・不整合・実行環境）を長期保存し、再現性・監査性を高める。
* `report/` は常に最新の不整合結果、`work/log/` は**時系列履歴**を保持する。

### 10.2 ディレクトリ構成（Structure）

```plaintext
project-root/
└─ work/
   └─ log/
      ├─ 2025-11-12T1030Z_G0100-STD-DOC0@G0110-STD-DOC1.yml
      ├─ 2025-11-12T1135Z_G0110-STD-DOC1@G0120-STD-DOC2.yml
      └─ latest.yml → シンボリックリンク（最新実行）
```

### 10.3 ファイル命名規則（Naming Rule）

**形式：**

```
YYYY-MM-DDThhmmZ_<target>@<checklist>.yml
```

**例：**

```
2025-11-12T1030Z_G0100-STD-DOC0@G0110-STD-DOC1.yml
```

| 要素                 | 内容                | 備考               |
| ------------------ | ----------------- | ---------------- |
| `YYYY-MM-DDThhmmZ` | 実行日時（ISO8601・UTC） | 時系列ソート容易         |
| `<target>`         | 検証対象文書            | 例：G0100-STD-DOC0 |
| `<checklist>`      | チェック仕様文書          | 例：G0110-STD-DOC1 |
| `.yml`             | 拡張子               | 構造化ログ            |

### 10.4 推奨ログ形式（YAML）

```yaml
meta:
  log_id: "2025-11-12T1030Z_G0100-STD-DOC0@G0110-STD-DOC1"
  target: "G0100-STD-DOC0-FormatPolicy"
  checklist: "G0110-STD-DOC1-AuthoringGuideline"
  executed_by: "ai"
  executed_at: "2025-11-12T10:30:00+09:00"
  duration_sec: 4.23
  environment:
    platform: "local"
    version: "v1.4.0"
    runner: "manual-or-ci"
    commit_hash: "abc1234"
summary:
  total_checks: 25
  total_issues: 1
  total_passed: 24
  severity_summary:
    high: 0
    medium: 1
    low: 0
issues:
  - id: "DOC-002"
    section: "6. 改訂履歴"
    status: "missing"
    message: "日付の欠落"
    suggestion: "全ての改訂項目に日付を追加"
execution_log:
  steps:
    - step: "load-checklist"
      status: "ok"
      details: "25項目を読み込み"
    - step: "parse-document"
      status: "ok"
      details: "セクション12件解析"
    - step: "validate"
      status: "warning"
      details: "DOC-002不整合を検出"
  completed: true
```

### 10.5 設計意図（Design Intent）

| セクション           | 意味               | 運用上の利点               |
| --------------- | ---------------- | -------------------- |
| `meta`          | 実行メタ情報（ID・環境・時間） | 再現性確保、トレーサビリティ強化     |
| `summary`       | 検証集計             | 変化点分析、品質指標化に有用       |
| `issues`        | 不整合詳細            | `report/` と同期可能な最小集合 |
| `execution_log` | 実行過程記録           | デバッグ・再実行補助           |

### 10.6 ログローテーション方針（Rotation Policy）

| 項目    | 推奨設定                           |
| ----- | ------------------------------ |
| 保存期間  | 最新N件（例：10件）を残し古いものはアーカイブ／削除    |
| 保存先   | `work/log/archive/YYYY/` に年別格納 |
| 最新リンク | `latest.yml` を更新し常に最新へリンク      |
| 監査用途  | 長期保存が必要な実行はリリースタグと併せて保全        |

### 10.7 他形式との比較（Format Comparison）

| 形式           | 長所                                   | 短所           |
| ------------ | ------------------------------------ | ------------ |
| **YAML（推奨）** | 人間可読＋構造化しやすい。既存 checklist/report と統一 | 大量データ時にサイズ増  |
| JSON         | 機械可読性が高い                             | 手動レビューはやや不向き |
| Markdown     | 人が直接読むのに最適                           | 構造化検証には不向き   |
| CSV          | 集計に便利                                | 階層情報を保持できない  |

### 10.8 結論（Conclusion）

* `work/log/` は **「検証履歴の恒久保管層」**として追加する。
* ファイル命名は **`<timestamp>_<target>@<checklist>.yml`** を準拠規約とする。
* ログ内容は **`meta / summary / issues / execution_log`** の4部構成を標準とする。
* `report/` は最新の不整合のみ保持、`work/log/` は時系列履歴を保持する。
