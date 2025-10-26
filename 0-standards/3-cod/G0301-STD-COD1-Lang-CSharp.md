---
schema: "https://schema.org/CreativeWork"
doc_id: "G0301-STD-COD1-Lang-CSharp"
title: "Coding Standard – Language Module: C#"
version: "1.0.0"
date: "2025-10-26"
status: "Approved"
owner: "Documentation Team"
reviewers: ["Architecture Review Board", "QA Lead"]
confidentiality: "Public"
scope: "Generic"
lifecycle: "Stable"
description: "COD0を前提としたC#固有規範。Roslyn/StyleCop/Directory.Build.props/.editorconfigを通じてCIで検証可能。"
related_docs: ["G0300-STD-COD0-CodingStandard"]
---

# [COD1-CS] C# Coding Standard

## 1. 言語/コンパイラ
- `LangVersion` = `latest`（LTS追随可） **MUST**  
- `Nullable` = `enable` **MUST**  
- 警告→エラー扱い（`TreatWarningsAsErrors`） **SHOULD**（PJで一時緩和可）

## 2. 命名/スタイル
- 型/メソッド: PascalCase（MUST）  
- ローカル: camelCase（SHOULD）  
- private field: `_camelCase`（SHOULD）

## 3. 非同期/リソース
- 非同期API優先（`Task`/`ValueTask`） **MUST**  
- `CancellationToken` 受け入れ **MUST**  
- `IAsyncDisposable` 活用 **SHOULD**

## 4. 例外/エラー
- `throw;` で再スロー（スタック維持） **MUST**  
- 業務例外型でドメイン表現 **SHOULD**

## 5. アナライザ/リンタ
- Roslyn Analyzers 有効 **MUST**  
- StyleCop 有効 **SHOULD**（重大度調整可）  
- `fail_on_warning` **SHOULD** = true

## 6. 共通設定ファイル（推奨）
**Directory.Build.props**
```xml
<Project>
  <PropertyGroup>
    <Nullable>enable</Nullable>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
    <AnalysisLevel>latest</AnalysisLevel>
    <LangVersion>latest</LangVersion>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.CodeAnalysis.NetAnalyzers" Version="*" PrivateAssets="all" />
    <PackageReference Include="StyleCop.Analyzers" Version="*" PrivateAssets="all" />
  </ItemGroup>
</Project>
```

**.editorconfig（抜粋）**
```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 2
trim_trailing_whitespace = true

[*.cs]
indent_size = 4
csharp_style_var_for_built_in_types = true:caution
csharp_new_line_before_open_brace = all:warning
max_line_length = 120
```

## 7. Override キー例（PJ側）
```yaml
rules:
  cod.lang.csharp:
    analyzer.stylecop: warning
    warnings.as_errors: false
```
