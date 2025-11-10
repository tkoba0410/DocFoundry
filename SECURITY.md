---
schema: DOC0-SEC
title: DocFoundry Security Policy
version: 1.0.0
---

# 🔒 Security Policy

本方針は、DocFoundry リポジトリの情報セキュリティ運用を定義する。

## 1. 基本原則
- 脆弱性報告は `security@org.example` に送付。
- 秘匿情報（APIキー、資格情報など）はリポジトリに含めない。
- 自動検証（CI）で `.env`, `.pfx`, `.key` の登録を禁止。

## 2. 脆弱性対応プロセス
1. 受付 → QAによる初期評価（24h以内）
2. 深刻度判定（CVSS準拠）
3. 修正コミット → タグ発行 → 公開報告

## 3. Checklist
| No | 確認項目 | 判定 |
|----|------------|------|
| 1 | 秘匿情報がコミットに含まれていない |  |
| 2 | 脆弱性報告窓口がREADME等に明記 |  |
| 3 | CVSS評価が記録されている |  |
