---
schema: STD-SCHEMA
doc_id: "SCHEMA-INDEX"
title: Schema Directory Guide
version: "v1.0.0"
date: "2025-10-31"
status: "Approved"
---

# 🗂️ Schema Directory Guide

このディレクトリは、標準文書やCI検証で利用するスキーマ定義を管理する。

---

## 1. 表紙情報
- 文書番号: `SCHEMA-INDEX`
- バージョン: **v1.0.0**
- 日付: 2025-10-31
- 状態: Approved

---

## 2. ファイル一覧

| ファイル | 用途 |
|-----------|------|
| `dcmm.doc.schema.json` | Document Conformance Metadata Model（DOC層向け） |
| `dcmm.scd.schema.json` | SCDフェーズ文書向けメタデータスキーマ |
| `dcmm.cod.schema.json` | COD層文書向けメタデータスキーマ |
| `dcmm.schema.json` | 旧DCMMスキーマ（互換性維持用、今後はDoc/SCD/COD別を使用） |
| `ruleset.json` | 自動検証ルールセット |

---

## 3. Checklist
| No | 確認項目 | 判定 |
|----|------------|------|
| 1 | 全スキーマに対応するSTD文書が存在 |  |
| 2 | JSON構造がCI検証に組み込まれている |  |
