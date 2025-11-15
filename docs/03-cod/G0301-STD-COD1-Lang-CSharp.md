---
schema: "https://schema.org/CreativeWork"
"@type": "CreativeWork"
identifier: "G0301-STD-COD1-Lang-CSharp"
name: "Coding Standard – C#"
version: "v1.1.0"
datePublished: "2025-11-14"
inLanguage: ["ja"]
creator:
  "@type": "Person"
  name: "Individual Developer"
description: >
  本書はプロジェクトに依存しないC#のコーディング規範を定義する。
  運用・CI・逸脱管理要素を除外し、純粋な言語規範層（L4: Coding Core）として整備したStar5準拠版。
---

# [STD-COD1] Coding Standard – C# (Project-Agnostic / Language Core Edition)

## 目次

* [1. 適用範囲](#1-適用範囲)
* [2. 原則（COD0準拠）](#2-原則cod0準拠)
* [3. 言語既定](#3-言語既定language-defaults)
* [4. 命名規約](#4-命名規約naming)
* [5. 例外処理](#5-例外処理exceptions)
* [6. 非同期と並行性](#6-非同期と並行性asyncconcurrency)
* [7. リソース管理](#7-リソース管理disposables)
* [8. コレクション・Null扱い](#8-コレクションnull扱い)
* [9. XMLドキュメントコメント](#9-xmlドキュメントコメント)
* [10. スタイル/フォーマット](#10-スタイルフォーマットeditorconfig)
* [11. 測定キー（YAML）](#11-測定キーヤムル-codlangcsharp)
* [12. 改版履歴](#12-改版履歴)

---

## 1. 適用範囲

* 対象：C# 10 以降。上位互換性を前提とし、下位互換は保証しない。
* 設計・API契約・SLO値などは含まない（COD0範囲外）。
* 運用・検証・CI関連は別規約（G0110-STD-DOCO）に委譲。

---

## 2. 原則（COD0準拠）

* **可読性優先（MUST）**
* **自己記述性（MUST）**
* **最小公開（MUST）**
* **循環依存禁止（MUST NOT）**
* **空catch禁止（MUST NOT）**
* **再スローは `throw;`（MUST）**
* **副作用の局所化（SHOULD）**

---

## 3. 言語既定（Language Defaults）

| 項目              | 規範                                  | 備考                    |
| --------------- | ----------------------------------- | --------------------- |
| nullable参照型     | `<Nullable>enable</Nullable>`（MUST） | 明示的`?`/`!`使用          |
| namespace       | file-scoped形式（SHOULD）               | `namespace X;`        |
| var             | 初期化式から型が明白な場合のみ（SHOULD）             | 公開APIでは禁止（MUST NOT）   |
| async/await     | TAP準拠（MUST）                         | `async void`はイベント以外禁止 |
| record          | 不変モデル用途（SHOULD）                     | DTO, VOに適用            |
| readonly struct | 軽量値型に適用（SHOULD）                     | 防御的コピー削減              |
| ConfigureAwait  | ライブラリでは `false`（SHOULD）             | UIでは不要                |

---

## 4. 命名規約（Naming）

| 対象           | 規則                              | 例                |
| ------------ | ------------------------------- | ---------------- |
| 型・メソッド・プロパティ | PascalCase（MUST）                | `PaymentService` |
| 変数・引数・フィールド  | camelCase（MUST）                 | `paymentId`      |
| 定数           | PascalCase（MUST）                | `DefaultTimeout` |
| インターフェイス     | `I`接頭（MUST）                     | `IClock`         |
| 非同期メソッド      | `Async`接尾（MUST）                 | `FetchAsync`     |
| 非公開フィールド     | `_camelCase` または `this.`形式（MAY） | 同一リポジトリで混在禁止     |

---

## 5. 例外処理（Exceptions）

* **例外は制御フローに使用しない（MUST）**
* **空catch禁止（MUST NOT）**
* **ArgumentNullException.ThrowIfNull(x);** を利用
* **再スローは `throw;` でスタック保持（MUST）**
* **innerException** を常に設定（SHOULD）
* **例外型**：`ApplicationException`禁止、独自例外を定義（SHOULD）

---

## 6. 非同期と並行性（Async/Concurrency）

* **CancellationToken受け渡し（MUST）**
* **同期ブロッキング禁止（MUST NOT）**：`.Result` / `.Wait()` / `.GetAwaiter()`
* **スレッド安全性（SHOULD）**：`Immutable*`, `SemaphoreSlim` など使用。

---

## 7. リソース管理（Disposables）

* `IDisposable`/`IAsyncDisposable` 対応必須（MUST）
* `HttpClient` 再利用（SHOULD）
* `using` / `await using` による決定的解放（MUST）

---

## 8. コレクション・Null扱い

* **戻り値でnull禁止（MUST）**：空集合を返す。
* **公開面では `IReadOnlyList<T>` 使用（SHOULD）**
* **Tryパターン採用（SHOULD）**：`bool TryX(out T value)`

---

## 9. XMLドキュメントコメント

* **公開API必須（MUST）**：`<summary>`, `<param>`, `<returns>` 等。
* **要約は1文明確（SHOULD）**
* **例は可動コード意識（SHOULD）**
* **null許容整合**：属性（`[NotNull]` 等）＋XML Doc両方で一致（SHOULD）
* **非公開API Doc**：必要時のみ（MAY）

---

## 10. スタイル/フォーマット（.editorconfig）

* スペース4／LF改行（MUST）
* 最終行改行あり（MUST）
* `using`整列・未使用削除（MUST）
* ブレース常時使用（MUST）
* `TreatWarningsAsErrors=true`（SHOULD）

---

## 11. 測定キー（YAML; cod.lang.csharp）

```yaml
version: 1
rules:
  cod_lang_csharp:
    nullable_enabled: true
    treat_warnings_as_errors: true
    editorconfig_required: true
    async_void_forbid: true
    async_blocking_forbid: true
    xml_doc_public_required: true
    style_usings_sorted: true
    naming_interface_prefix_i: true
    return_collection_never_null: true
    dispose_required: true
    empty_catch_forbid: true
    var_disallow_in_public_api: true
    await_configureawait_library_default_false: true
    xml_doc_coverage_public_min: 1.00
    using_directives_sorted: true
    private_members_unused_forbid: true
    parameters_unused_forbid: true
    nameof_prefer: true
    numeric_checked_arithmetic_prefer: true
valid_until: "2026-11-30"
```

---

## 12. 改版履歴

| 版      | 日付           | 内容                                                         |
| ------ | ------------ | ---------------------------------------------------------- |
| v1.1.1 | "2025-11-09" | 運用・CI・逸脱管理要素を除外し、純粋な言語規範版に改訂。Front MatterとTOCをDOC0準拠化      |
| v1.1.0 | "2025-11-09" | Star5整合改訂：Front Matter統一、YAML snake_case化、T4-Deviation参照追加 |
| v1.0.0 | "2025-10-28" | 初版（DocFoundary準拠）                                          |

---
