# YAML活用方針書（SCD Framework準拠）

## 1. 目的
本方針は、プロジェクト開発全体における  
**仕様・設計・生成・検証の基盤を YAML に統一**し、  
「**SCD（Spec–Conformance Development Cycle）**」を芯とした  
仕様中心開発を長期的かつ自動的に維持することを目的とする。

---

## 2. 基本理念

| 原則 | 内容 |
|------|------|
| **SCD中核主義（SCD-Centric Principle）** | すべての生成・検証は SCD モデル（Spec–Conformance–Cycle）に従う。YAML はその表現手段である。 |
| **唯一の正（Single Source of Truth）** | `/specs/**/*.yaml` を唯一の正（ソース・オブ・トゥルース）とし、仕様の源泉とする。 |
| **自動生成主義** | コード・テスト・ドキュメント・評価指標はすべて YAML から自動生成する。 |
| **人機両可読性** | YAMLは人間可読・機械可読の両立を目指し、SCD構造の意味が失われないようにする。 |
| **追跡可能性（Traceability）** | YAML内の `doc_id`, `goal_id`, `req_id` を生成物に必ず埋め込み、SCDトレーサビリティを維持する。 |

---

## 3. 運用原則

### 3.1 標準フロー（SCDサイクル準拠）
```
人間可読文書（Markdown/Word）
          │ （構造抽出・意味付与）
          ▼
YAML仕様（唯一の正 / SCD Spec）
          │ （テンプレート／生成基盤）
          ├─→ コード生成（.g.cs 等）
          ├─→ テスト生成（Conformance層）
          ├─→ ドキュメント生成（Cycle層）
          └─→ 評価・CI整合性検証（Feedback）
```

### 3.2 編集責務
- **編集対象**：`/specs/**/*.yaml` のみ（唯一の正）  
- **生成物の直接編集**：禁止（CIが検出してFail）  
- **人間可読文書からのYAML化**：初期導入・再構成時のみ許可  
- **以降の更新**：YAML → 生成の一方向フローを厳守（SCDのCycleを保持）

---

## 4. 人間可読文書との関係

### 4.1 導入期の活用
- 既存の要件定義書・議事録などを **YAML化（SCD Spec化）** して初期仕様とする。  
- YAML化後は、人間可読文書（Prose）は生成物扱いとし、**直接修正を禁止**する。  

### 4.2 例外的利用
- 教育・説明・外部公開目的で一時的に Prose→YAML の逆変換を許可する。  
- 修正が発生した場合は：  
  **Prose修正 → YAMLパッチ提案 → YAML更新 → 自動再生成** の手順を取る。

---

## 5. YAML構文規約（原子ルール）

| 項目 | 規則 |
|------|------|
| エンコード | UTF-8 (BOMなし) |
| インデント | 半角スペース2 |
| 改行 | LF固定 |
| 真偽値 | `true` / `false` のみ許可 |
| 日付 | ISO-8601形式 `"2025-11-03T00:00:00+09:00"` |
| コメント | `# ` で開始、内容保持 |
| ファイル命名 | `lower-kebab-case.yaml` |
| 必須構造 | `meta`, `goal`, `pipeline`, `links`, `lifecycle` など SCD Schemaで定義 |
| 禁止事項 | タブ / 重複キー / 曖昧ブール（`yes`, `no`, `on`, `off`） |

---

## 6. ディレクトリ構成モデル（SCD準拠）

```
/specs
  /foundation     ← 共通語彙・列挙・基礎定義（SCD Meta）
  /domains        ← ドメイン別仕様・API定義・要件群（SCD Spec）
  /runtime        ← 運用パラメータ・閾値・制約
  /goals          ← 評価・KPI・CI目標（SCD Conformance）
/schemas          ← JSON Schema / tYAML（構文・意味検証）
/templates        ← 生成テンプレート（Scriban / NSwag 等）
/docs             ← 自動生成ドキュメント（Cycle層）
```

---

## 7. CI・品質保証（SCD Conformanceの一部）

| 検証項目 | 方法 | 成否条件 |
|-----------|------|----------|
| 構文検証 | `yamllint`, `jsonschema` | Lint/Schemaエラーがない |
| 意味検証 | `scd-validate.py`（AI/Schema併用） | 意味的整合性（Spec↔Test）が取れている |
| 差分検証 | `git diff --exit-code` | 差分ゼロ（生成物不改変） |
| トレース | `doc_id`, `goal_id`, `req_id` | 全生成物に埋め込み必須 |
| 生成物改変検知 | ヘッダチェック | `AUTO-GENERATED` 改変時にFail |
| Prose編集検知 | CI検出 | 直編集を禁止（Fail） |

---

## 8. 拡張・派生（SCDの拡張実装）

- **tYAML（Typed YAML）** による SCD仕様の宣言化を推奨。  
  目的・制約・適合基準を YAMLで宣言し、AI/CIが解釈・実行可能な状態にする。  
- **拡張DSL（Domain DSL / Eval DSL）** は YAMLを基底構文として設計する。  
- **AI支援**：YAMLに含まれる `ai_meta` 情報を用い、  
  AIが要件補完・テスト生成・仕様整合性提案を行う。  
- **将来拡張**：YAML → Graph/Model変換により、  
  ドキュメント・コード・テストを完全自動連携（SCD Cycleの完全自動化）。

---

## 9. 運用体制（SCD Framework管理下）

| 区分 | 内容 |
|------|------|
| 責任範囲 | 各ドメイン所有者（CODEOWNERS指定） |
| 更新単位 | 「1仕様 = 1PR」原則 |
| 承認 | レビュー＋CI成功をもって確定 |
| 廃止 | `lifecycle: deprecated` 指定＋CI警告表示 |
| バージョン | SemVer形式（`version: 1.0.0`） |
| 上位準拠 | `SCD Framework` に準拠し、`SCDAY` 実装群と互換を保つ。 |

---

## 10. まとめ（SCDを芯とするYAML活用）

- YAMLは**SCDの実体化フォーマット**であり、形式が目的ではなく**SCDを支える器**である。  
- 開発全体は、**SCD（思想）→ YAML（構造）→ AI/CI（知能と検証）**の連鎖で運用する。  
- **「SCDが芯」**という原則を軸に、  
  YAMLは仕様の形を保ち、AIは仕様の意味を拡張し、  
  CIがその整合性を常時保証する。  
- この三位一体の体制により、プロジェクトは「仕様で動く開発（Spec-Driven System）」を継続的に実現する。

---

### ✅ 推奨文書名：
`YAML-Usage-Policy(SCD-Framework-Edition).md`
