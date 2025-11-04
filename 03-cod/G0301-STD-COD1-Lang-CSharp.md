---
schema: "https://schema.org/CreativeWork"
doc_id: "G0301-STD-COD1"
title: "Coding Standard – C# (Project‑Agnostic)"
version: "v1.0.0"
date: "2025-10-28"
status: "Approved"
owner: "Documentation Team"
reviewers: ["Architecture Review Board", "QA Lead"]
confidentiality: "Public"
scope: "Generic"
lifecycle: "Stable"
description: "本書はプロジェクトに依存しないC#のコーディング規範を定義する。設計仕様（アーキ構成、API契約、SLO値等）は扱わず、G0300-STD-COD0（コア）を言語観点で具体化する。"
related_docs:
  - "G0300-STD-COD0"
  - "G0100-STD-DOC0"
  - "G0101-STD-DOC1"
inherit_from: ["G0100-STD-DOC0"]
x-schema: "/schemas/dcmm.cod.schema.json"
---

# [STD-COD1] Coding Standard – C# (Project‑Agnostic)

## 1. 表紙情報
- 文書番号: `G0301-STD-COD1`
- バージョン: **v1.0.0**
- 日付: 2025-10-28
- 状態: Approved (Stable)

---

> **適用範囲**：C# 10 以降（最新推奨）を前提とし、上位互換を意図する。プロジェクトに依存する命名・設計・ログ項目・タイムアウト値等は扱わない。

## 2. 原則（COD0の言語具体化）
- **可読性優先（MUST）**：意図が伝わる命名・短いメソッド・副作用の局所化。
- **自己記述性（MUST）**：魔法値の定数化、明確な前提/事後条件。
- **最小公開（MUST）**：`internal`/`private` を既定、`public` は必要最小限。
- **循環依存禁止（MUST NOT）**：部分クラスや`InternalsVisibleTo`の濫用で境界を崩さない。
- **空catch禁止（MUST NOT）**：例外は文脈を付与して再スロー。

## 3. 言語機能の既定（Language Defaults）
- **nullable 参照型を有効化（MUST）**：`<Nullable>enable</Nullable>`。`?`/`!`の使用を明示的に。
- **file-scoped namespace（SHOULD）**：名前空間はファイル先頭で `namespace X;`。
- **`var`の使用（SHOULD）**：初期化式から型が明白な場合に限定。**公開APIの戻り値/引数/プロパティでは使用禁止（MUST NOT）**。
- **式本体メンバー（MAY）**：短小メソッド／プロパティで可。
- **`record`/`record struct`（SHOULD）**：値オブジェクト・DTOは不変モデルを既定。
- **`readonly struct`（SHOULD）**：軽量値型は読み取り専用で防御的コピー削減。
- **パターンマッチング（SHOULD）**：`switch`式やガードで分岐の明示性を高める。
- **`async`/`await`（MUST）**：非同期は TAP 準拠。`async void`は**イベントハンドラ以外禁止**。

## 4. 命名規約（Naming）
- **型/メソッド/プロパティ/イベント**：`PascalCase`（MUST）。
- **ローカル変数/パラメータ/フィールド**：`camelCase`（MUST）。
- **定数**：`PascalCase`（MUST）。
- **インターフェイス**：`I`接頭（MUST）。例：`IOrderRepository`。
- **非公開フィールド命名**は組織プロファイル（ARC-PRF）で `_camelCase` または `camelCase+this.` のいずれかに統一（MUST）。本標準は両方式を許容（MAY）。
- **混在禁止（MUST）**：`_camelCase` と `camelCase+this.` は同一リポジトリで混在させない。採用方式は ARC-PRF で定める。
- **略語**：承認済みのみ（COD0の `naming.abbrev.allowlist` に準拠）。
- **非同期メソッド**：`Async` 接尾（MUST）。例：`FetchAsync`。

## 5. ファイル/型の配置（Layout）
- **単一責務（MUST）**：1ファイル1トップレベル型を原則。小規模な`enum`/`record`の補助定義のみ同居可。
- **順序（SHOULD）**：`usings` → `namespace` → `type`。メンバー順は `const/fields/ctors/properties/methods/nested types`。
- **`partial`**：自動生成物との分離目的のみ使用（SHOULD）。設計都合の分割は避ける。

## 6. 例外・エラー（Exceptions）
- **基本方針（MUST）**：例外は例外的事象に限定。フロー制御に使わない。
- **ガード節（MUST）**：早期失敗。`ArgumentNullException.ThrowIfNull(x);` 等を使用。
  **例**：`ArgumentOutOfRangeException.ThrowIfNegative(value);`
- **例外型（SHOULD）**：ドメイン/契約/環境に応じた独自例外を `Exception` 直系で定義。`ApplicationException` は使用しない。
- **再スロー（MUST）**：`throw;` でスタックを保持。ラップ時は `innerException` を設定し、意味のあるメッセージとコンテキスト（識別子）を含む。
- **空catch禁止（MUST NOT）**。必要なら `catch (SpecificEx ex) { Log(...); throw; }`。

## 7. 非同期/並行（Async/Concurrency）
- **キャンセル（MUST）**：公開非同期APIには `CancellationToken` を受け渡す。
- **ConfigureAwait（SHOULD）**：ライブラリでは `ConfigureAwait(false)` を既定。アプリUIでは既定不要。
- **ブロッキング禁止（MUST NOT）**：`.Result`/`.Wait()`/`.GetAwaiter().GetResult()` は禁止（デッドロック回避）。
- **同期ブロック禁止の自動検査（SHOULD）**：これらを検出する静的解析ルール（Roslynカスタム or CIソーススキャン）を適用。
- **スレッド安全性（SHOULD）**：共有可変を避け、`Immutable*` コレクションや `Channel`/`SemaphoreSlim` 等で調停。

## 8. リソース管理（IDisposable ほか）
- **`IDisposable`（MUST）**：`using`/`await using` で決定的解放。`IAsyncDisposable` に対応。
- **`HttpClient`（SHOULD）**：再利用/ファクトリ管理。短命インスタンス生成を避ける。
- **ファイル/ストリーム（MUST）**：`Async` APIの使用と適切なバッファ管理。

## 9. コレクション/Null/引数
- **戻り値（MUST）**：空集合は `Array.Empty<T>()` / 空リスト返却。`null`コレクションは返さない。
- **可変コレクションの公開禁止（MUST NOT）**：公開面は`IReadOnlyList<T>` 等で防御的コピー。
- **`Try`パターン（SHOULD）**：`bool TryX(out T value)` を採用し、例外コストを避ける。

## 10. LINQ/式/パフォーマンス
- **LINQ（SHOULD）**：可読性優先。Hot pathではループ最適化や`Span<T>`/`Memory<T>`の検討（MAY）。
- **割り当て抑制（MAY）**：`struct enumerator`、`ValueTask`、`ref struct` 等を状況に応じて。過剰最適化は避ける。
- **checked/unchecked（SHOULD）**：数値演算は過剰/境界で `checked` を明示。

## 11. 属性/アノテーション
- **`[Obsolete]`（MUST）**：代替APIと期限をメッセージで明記。
- **`[NotNull]`/`[DisallowNull]` 等のnullable注釈（SHOULD）**：契約の明示。
- **`[DebuggerDisplay]`（MAY）**：複雑型のデバッグ容易性向上。

## 12. ドキュメント（XML Doc）
- **公開API Doc必須（MUST）**：`<summary>`, `<param>`, `<returns>`, `<exception>`, `<remarks>`, `<example>`。
- **品質要件（SHOULD）**：要約は1文で明確、例外は契約に基づき網羅、例は**可動コード**を意識。
- **非公開API（MAY）**：必要時のみDoc。コメントは「何を/なぜ」中心。
- **null許容の整合（SHOULD）**：公開APIでは、戻り値や引数の null 許容は XML Doc と属性（例：`[NotNull]`, `[MaybeNull]`）で一貫して表明する。
  ※属性は `System.Diagnostics.CodeAnalysis` 名前空間のものを指す。

## 13. スタイル/フォーマット（.editorconfig）
- **タブ/スペース**：スペース2〜4（組織既定に合わせる）。
- **改行**：LF。最終行改行あり。
- **`using`**：ソート＋未使用削除（MUST）。
- **スコープ**：ブレースは常に使用（MUST）。
- **命名**：`_`フィールド接頭は**原則不使用**。

**例：最小 .editorconfig（抜粋）**
```ini
root = true

[*.cs]
end_of_line = lf
insert_final_newline = true
charset = utf-8

# indentation
indent_style = space
indent_size = 4
trim_trailing_whitespace = true

# dotnet analyzers
dotnet_analyzer_diagnostic.severity = warning
dotnet_diagnostic.CA1305.severity = warning
dotnet_diagnostic.IDE0040.severity = warning
dotnet_diagnostic.IDE0005.severity = warning
dotnet_diagnostic.IDE0051.severity = warning
dotnet_diagnostic.IDE0060.severity = warning
dotnet_diagnostic.IDE0063.severity = warning
dotnet_diagnostic.IDE0041.severity = suggestion
dotnet_diagnostic.IDE0052.severity = warning

# language style
csharp_style_var_for_built_in_types = true:suggestion
csharp_style_var_when_type_is_apparent = true:suggestion
csharp_style_var_elsewhere = false:suggestion
csharp_prefer_braces = true:warning
csharp_new_line_before_open_brace = all:warning
dotnet_style_qualification_for_field = true:suggestion
```

## 14. アナライザ/ビルド規約
- **.NET Roslyn アナライザ（MUST）**：既定（CA/IDE）を有効化。新規警告は抑止せず修正を原則。
- **Microsoft.CodeAnalysis.NetAnalyzers** を既定とし、**独自禁止ルール**（同期ブロック検出など）はカスタムまたはCIソーススキャンで補う。
- **警告をエラー扱い（SHOULD）**：`TreatWarningsAsErrors=true`。段階的導入可。
- **スタイル逸脱の抑止**：`#pragma`/`SuppressMessage` は最小限、根拠をコメント。

**例：最小 Directory.Build.props（抜粋）**
```xml
<Project>
  <PropertyGroup>
    <Nullable>enable</Nullable>
    <TreatWarningsAsErrors>true</TreatWarningsAsErrors>
    <AnalysisLevel>latest-recommended</AnalysisLevel>
    <WarningsNotAsErrors>CS1591</WarningsNotAsErrors>
  </PropertyGroup>
</Project>
```

## 15. 禁止/非推奨パターン（C#）
- **`async void`**（イベント以外）/ **同期ブロック**（`.Result`/`.Wait()`）— **禁止**。
- **空catch／`catch (Exception) {}`** — **禁止**。
- **`dynamic`濫用** — ランタイムエラー誘発のため**非推奨**（MAY、根拠付きで許容）。
- **可変静的状態** — **禁止**。`static`は不変/スレッドセーフに。
- **可視性過多** — **禁止**。`public`は最小限。
- **戻り値で `null` コレクション** — **禁止**。空集合を返却。

## 16. 測定可能キー（YAML; cod.lang.csharp）
```yaml
version: 1
rules:
  cod.lang.csharp:
    nullable.enabled: true
    treat_warnings_as_errors: true
    editorconfig.required: true
    analyzers.analysis_level: "latest-recommended"
    async.avoid_blocking_calls: true
    async.void.forbid: true
    api.docs.public.required: true
    style.usings.remove_unused: true
    style.file_scoped_namespace: true
    naming.interface.prefix_I: true
    return.collection.never_null: true
    dispose.required: true
    empty_catch.forbid: true
    var.disallow_in_public_api: true
    await.configureawait.library_default_false: true
    xml_doc.coverage.public.min: 1.00
    using.directives.sorted: true
    private.members.unused.forbid: true
    parameters.unused.forbid: true
    nameof.prefer: true
    numeric.checked.arithmetic.prefer: true
valid_until: "2026-10-31"
```

## 17. CI適合性（Verification）
- **ビルド**：`Nullable=enable`/`TreatWarningsAsErrors=true` の確認。
- **静的解析**：Roslyn アナライザの結果が**0エラー**であること。
- **スタイル**：`.editorconfig` 準拠（未使用 using 削除、ブレース必須）。
- **非同期**：同期ブロック検査（`.Result`/`.Wait()` の禁止リスト）。
  ※検査は Roslyn カスタムルールまたは CI ソーススキャンにより実施（運用ドキュメント参照）。
- **Doc**：公開APIのXML Docカバレッジしきい値（組織既定）。


## 18. サンプル（良い/悪い）
**良い**
```csharp
public sealed record Money(decimal Amount, string Currency);

public interface IClock { DateTimeOffset Now { get; } }

public sealed class PaymentService
{
    private readonly IClock clock;

    public PaymentService(IClock clock) => this.clock = clock;

    public async Task<bool> CaptureAsync(Guid paymentId, CancellationToken ct)
    {
        ArgumentNullException.ThrowIfNull(paymentId);
        using var scope = Telemetry.Start("capture", paymentId);
        ct.ThrowIfCancellationRequested();

        var ok = await AuthorizeAsync(paymentId, ct).ConfigureAwait(false);
        if (!ok) return false;

        return await SettleAsync(paymentId, clock.Now, ct).ConfigureAwait(false);
    }
}
```

**悪い**
```csharp
public class PaymentService
{
    public bool Capture(Guid id)
    {
        try
        {
            var ok = Authorize(id).Result; // 同期ブロック
            if (!ok) return false;
            return Settle(id);
        }
        catch (Exception) { } // 空catch
        return true;
    }
}
```

## 19. 改版履歴
- **v1.0.0 (2025-10-28)** : DocFoundry 初版FIXとしてC#言語規約を確定。
- **v0.2.2-draft (2025-10-27)** : XML Doc属性明記、同期ブロック検査方法を追記。
- **v0.2.1-draft (2025-10-27)** : Doc整合性・アナライザ明記・YAMLキー強化。
- **v0.2.0-draft (2025-10-27)** : 命名・非同期・YAMLキーを強化し、CI適合性を明確化。
- **v0.1.0-draft (2025-10-27)** : 初版ドラフト。
