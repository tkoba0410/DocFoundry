---
schema: "https://schema.org/CreativeWork"
doc_id: "P0000-STD-PJX-Index"
title: "Project Documentation Index"
version: "0.1.0"
date: "2025-10-26"
status: "Draft"
owner: "Project Maintainer"
reviewers: ["Documentation Review Team"]
confidentiality: "Internal"
scope: "Project"
lifecycle: "Draft"
description: "プロジェクト文書（P0100〜P0800）および関連標準文書（G0100〜G0210）の参照一覧。"
---

# [PJX-INDEX] プロジェクト文書索引

## 1. 概要
本ファイルは `project-template/docs/` 以下に配置される全P文書の索引であり、  
各文書と対応する標準文書（Gシリーズ）を一覧で示す。

---

## 2. 文書一覧

| 文書ID | カテゴリ | タイトル | 対応標準 | 状態 |
|:--|:--|:--|:--|:--|
| P0100-OVR-OVRV | OVR | プロジェクト概要 | G0200-STD-SCD0 | Draft |
| P0200-REQ-OVRV | REQ | 要求概要 | G0201-STD-SCD1 | Draft |
| P0300-ARC-OVRV | ARC | 構成概要 | G0202-STD-SCD2 | Draft |
| P0400-IMP-OVRV | IMP | 実装概要 | G0204-STD-SCD4 | Draft |
| P0500-TST-OVRV | TST | テスト概要 | G0203-STD-SCD3 | Draft |
| P0600-OPS-OVRV | OPS | 運用概要 | G0206-STD-SCD6 | Draft |
| P0700-SEC-OVRV | SEC | セキュリティ概要 | G0103-STD-DOC3 | Draft |
| P0800-STD-OVRV | STD | プロジェクト標準概要 | G0101-STD-DOC1 | Draft |

---

## 3. 標準文書との対応（related_docs）

```mermaid
flowchart TD
  subgraph G[汎用標準文書群 (standards)]
    G0100["G0100 DocumentPolicy"]
    G0101["G0101 CompliancePack"]
    G0102["G0102 ProjectAdaptationGuide"]
    G0103["G0103 CodingStandard"]
    G0104["G0104 LANG-CS"]
    G0200["G0200 CycleOverview"]
    G0201["G0201 SpecPhase"]
    G0202["G0202 ContractPhase"]
    G0203["G0203 TestPhase"]
    G0204["G0204 ImplPhase"]
    G0205["G0205 ConformancePhase"]
    G0206["G0206 FeedbackPhase"]
  end

  subgraph P[プロジェクト文書群 (docs)]
    P0100["P0100 OVR Overview"]
    P0200["P0200 REQ Overview"]
    P0300["P0300 ARC Overview"]
    P0400["P0400 IMP Overview"]
    P0500["P0500 TST Overview"]
    P0600["P0600 OPS Overview"]
    P0700["P0700 SEC Overview"]
    P0800["P0800 STD Overview"]
  end

  P0100 --> G0200
  P0200 --> G0201
  P0300 --> G0202
  P0400 --> G0204
  P0500 --> G0203
  P0600 --> G0206
  P0700 --> G0103
  P0800 --> G0101
```

---

## 4. 改訂履歴

| 版 | 日付 | 内容 |
|----|------|------|
| 0.1.0 | 2025-10-26 | 初版（自動生成）。P0100〜P0800文書の索引を作成。 |
