---
schema: "https://schema.org/CreativeWork"
doc_id: "G0300-STD-COD0"
title: "Coding Standard – Core (Language-Agnostic)"
version: "1.0.0"
date: "2025-10-27"
status: "Approved"
owner: "Documentation Team"
reviewers: ["Architecture Review Board", "QA Lead"]
confidentiality: "Public"
scope: "Generic (Organization-wide)"
lifecycle: "Canonical"
description: "本書は言語に依存しないコーディング規範を定め、設計・運用・アーキテクチャ仕様には踏み込まない。言語別標準（COD1+）および設計標準（ARC系）と補完関係にあり、コードそのものの品質・一貫性・検証可能性を目的とする。"
related_docs:
  - "G0100-STD-DOC0-DocumentPolicy"
  - "G0101-STD-DOC1-CompliancePack"
  - "G0200-STD-SCD0-CycleOverview"
  - "A0200-ARC-OVRV-Overview"
---

# 1. 目的 / 適用範囲
本標準は、**プログラミング言語に依存しないコーディング行為の原則**を定める。  
対象はアプリケーション、ライブラリ、ツールを問わず、**コード記述そのもの**に適用する。  
設計仕様（アーキテクチャ構成、API契約、性能指標、運用設定等）は対象外とし、  
それらは ARC 系・REQ 系・OPS 系標準で定義する。

# 2. 規範レベル
RFC 2119 に準拠し、**MUST / SHOULD / MAY / MUST NOT / SHOULD NOT** を用いる。  
逸脱は「#13 逸脱管理」に従って管理する。

# 3. 記法・可読性
- **可読性優先（MUST）**: 一読で意図が分かる命名・短い関数・略語乱用禁止。  
- **自己記述性（MUST）**: 名称・構造・コメントが仕様意図を説明。魔法値は禁止し定数化。  
- **一貫性（MUST）**: 同一概念には同一語彙を用いる。  
- **最小公開（MUST）**: 公開範囲は必要最小限。内部実装は隠蔽する。  
- **副作用の局所化（MUST）**: 状態変更やI/Oを限定的に扱う。  
- **早期失敗（MUST）**: 無効入力は即時に明示的失敗。  
- **コメントは理由を説明（SHOULD）**: 「なぜその実装か」を明示。

# 4. 依存とモジュール境界（Coding View）
- **循環依存の禁止（MUST NOT）**。  
- **依存方向の単調性（SHOULD）**: 上位モジュールが下位内部へ直接依存しない。  
- **暫定的な跨ぎ参照**は T4-Deviation で期限付き是正計画を記録。  
（具体的レイヤ構成や命名は ARC 系文書に委譲。）

# 5. エラー処理 / 例外
- **空 catch 禁止（MUST NOT）**。  
- **契約違反を区別（MUST）**: 入力検証エラー／環境障害／業務例外を分離。  
- **再スロー時に文脈付与（MUST）**: 原因・影響を保持して再スロー。  
- **冪等操作のみ再試行（SHOULD）**。  
（エラーコード体系やHTTP マップは API 標準に委譲。）

# 6. 並行性 / リソース管理
- **共有可変状態を最小化（MUST）**。  
- **キャンセル伝播（MUST）**: 処理中断を上位から下位へ適切に伝える。  
- **決定的解放（MUST）**: finally/using 等でリソースを確実に開放。

# 7. 設定・シークレット
- **設定の外在化（MUST）**: 環境変数や設定ファイルを利用し、ハードコード禁止。  
- **秘密情報の保護（MUST）**: コード・リポジトリに資格情報を含めない。  
- **既定値検証（SHOULD）**: 起動時に欠落・型不一致を検出。

# 8. ログ / 計測（Coding View）
- **PII禁止（MUST）**: 個人特定情報をログに出力しない。  
- **構造化ログ推奨（SHOULD）**: 機械可読形式を推奨。  
- **ログ・メトリクスのキー構成**は運用標準（OPS）に委譲。

# 9. テスト規約
- **層別（MUST）**: ユニット／統合／回帰を区別。  
- **カバレッジ閾値（MUST）**: 全体 ≥ 0.80、重要経路 ≥ 0.90。  
- **決定的テスト（MUST）**: 擬似乱数固定・時間抽象化・外部依存をダブル化。  
- **プロパティベーステスト（SHOULD）**: 不変条件の自動探索を推奨。

# 10. セキュリティと依存
- **最小権限で動作（MUST）**。  
- **依存性の衛生（MUST）**: 署名・ハッシュ検証、SCA、ライセンス確認。  
- **入力検証（MUST）**: 外部境界でのサニタイズ・正規化・検証を実装。

# 11. ドキュメント / コメント
- **公開APIのDoc必須（MUST）**: 概要・引数・戻り・例外・使用例。  
- **コメントは設計の反復ではなく理由説明（SHOULD）**。  
（設計決定記録 ADR は ARC 文書に所在。）

# 12. 禁止 / 非推奨パターン
- グローバル可変状態／シングルトン乱用（MUST NOT）  
- 循環依存／層逆参照（MUST NOT）  
- 空 catch／無視される戻り値（MUST NOT）  
- マジックナンバー／資格情報ハードコード（MUST NOT）  
- PII ログ出力（MUST NOT）

# 13. 逸脱管理
- 逸脱は `T4-Deviation` で管理し、**期限・是正計画**を設定（MUST）。  
- 是正期限切れはCIでFail（SHOULD）。  
- 承認プロセス・台帳運用は DOC 標準に従う。

# 14. 測定可能キー（Coding Metrics YAML）
```yaml
version: 1
rules:
  cod.core:
    naming.abbrev.allowlist: []
    func.max_lines: 50
    cyclomatic.max: 10
    magic_numbers.forbid: true
    logging.pii.forbid: true
    test.coverage.min: 0.80
    test.coverage.critical.min: 0.90
    flaky_tests.forbid: true
    input.validation.required: true
    error.empty_catch.forbid: true
    dispose.required: true
valid_until: "2026-10-31"
```

# 15. CI適合性（Verification View）
- **静的解析**: 命名・複雑度・空catch・マジックナンバーを検査。  
- **テストゲート**: カバレッジ閾値未達でFail。  
- **依存衛生**: SCAとライセンス検査を実施。  
- **シークレットスキャン**: 資格情報の混入をFail。  
- **逸脱検査**: 期限超過の逸脱をFail。

# 16. 用語集（抜粋）
- **PII** : 個人を特定可能な情報。  
- **ADR** : Architectural Decision Record（設計上の意思決定記録、別文書扱い）。  
- **SCD モデル** : 本組織の開発ライフサイクル定義。  

# 17. 導入チェックリスト
- [ ] 循環依存禁止を静的解析で検証  
- [ ] 空catch検出ルールを設定  
- [ ] カバレッジ閾値 0.80 / 0.90 をCIゲート化  
- [ ] PII禁止ルールをテスト  
- [ ] シークレットスキャン導入  
- [ ] T4-Deviation 期限チェック設定  

# 18. 改版履歴
- **1.0.0 (2025-10-27)** : 正式採用版。Draft 0.9.1 から内容変更なし。  
- **0.9.1-draft (2025-10-27)** : 設計・運用仕様を排除し純粋なコーディング規範化。  
- **0.9.0-draft (2025-10-27)** : 初版ドラフト。
