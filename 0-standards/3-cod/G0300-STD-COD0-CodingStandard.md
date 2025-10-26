---
schema: "https://schema.org/CreativeWork"
doc_id: "G0300-STD-COD0"
title: "Coding Standard – Core (Language-Agnostic)"
version: "1.0.0"
date: "2025-10-26"
status: "Approved"
owner: "Documentation Team"
reviewers: ["Architecture Review Board", "QA Lead"]
confidentiality: "Public"
scope: "Generic"
lifecycle: "Canonical"
description: "言語に依存しないコーディング規範のコア。SCDモデルと整合し、プロジェクト差異はYAMLで限定的に許容。"
related_docs: ["G0200-STD-SCD0-CycleOverview","G0101-STD-DOC1-CompliancePack"]
---

# [COD0] Coding Standard – Core

## 1. 位置づけ
- 本規範は **全言語共通**の原則を定義する。  
- 具体的な言語規則は COD1 以降（例: C# は G0301）で補完する。
- 参照順: **COD0 ＞ CODn（言語）＞ プロジェクト差異**。

## 2. 規範の強度（RFC2119）
- **MUST**: 例外不可（差異は ADR と期限付き例外でのみ許容）。
- **SHOULD**: 合理的理由があれば差異可（要 ADR）。
- **MAY**: 任意。

## 3. 共通原則（抜粋）
1) **命名**（MUST）：意図明確、略語乱用禁止、ドメイン語彙の一貫性。  
2) **責務分離**（MUST）：関数1責務、循環依存禁止、SOLID尊重。  
3) **契約尊重**（MUST）：Null/境界/例外契約を明示（機械可読Doc）。  
4) **テスト先行**（SHOULD）：Red→Green→Refactor、Conformance対象は100%。  
5) **ログ/監査**（MUST）：PII禁止、構造化ログ、相関ID。  
6) **Secrets**（MUST）：ソースに含めない（Vault/CI管理）。  
7) **依存/ライセンス**（MUST）：SCA/ライセンス検査合格。  
8) **国際化**（SHOULD）：ユーザー文字列は外部化。  
9) **セキュリティ**（MUST）：入力検証・出力エスケープ・最小権限。

## 4. Git/CI ゲート
- PRレビュー必須、ビルド＋フォーマット＋静的解析＋テスト＋SCA＋ライセンスの順で**Fail Fast**。

## 5. プロジェクト差異（YAML鍵）
例（`project-coding-overrides.yml`）:
```yaml
version: 1
project: EXA
rules:
  cod.core:
    test.coverage.min: 0.80
  cod.lang.csharp:
    analyzer.stylecop: warning
valid_until: "2026-03-31"
adr: "ADR-0123"
```
