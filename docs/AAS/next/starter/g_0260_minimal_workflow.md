# G0260 Minimal Document Workflow

SCAI を記憶ゼロから再開しても安定した文書生成ができるようにするための **最小ワークフロー規範**。

---

## 1. Purpose（目的）

文書の作成・修正・確認を、短い指示で効率的かつ揺らぎなく行うための **最小工程** を定義する。
本書は A 層に属し、G0001（判断モデル）および G0250（構造規範）と連携して使用される。

---

## 2. Scope（適用範囲）

* 新規文書作成
* 既存文書の修正
* 文書の確認・評価
* サマリー／変換
* AI と人間の協働工程全般

---

## 3. Minimal Workflow（最小工程）

文書生成は次の 6 ステップのみで行う。

### 3.1 Step 1：Intent の提示

人間が Goal / Scope / Output を明確に提示する。
AI は推測してはならず、不明点があれば質問する。

---

### 3.2 Step 2：AI の初期判断（G0001 の適用）

AI は Intent を受けて、G0001 の判断4層（Intent / Principles / Constraints / Self-Monitoring）を内部適用し、生成方針を決定する。

---

### 3.3 Step 3：Draft の生成（最小構造）

AI は G0250 にしたがって文書の Draft を生成。

* 最小限の情報のみ
* 不明点は質問
* 禁止事項は遵守

---

### 3.4 Step 4：AI による Self-Monitoring

Draft 出力前に、G0001 の Self-Monitoring を内部実行し、

* Intent との齟齬
* 制約違反
* 原則との矛盾
* 推測の混入
  をチェックし、必要なら修正または質問を行う。

---

### 3.5 Step 5：人間によるレビュー

人間は Draft を評価し、次のいずれかを返す：

* 修正点（具体的に）
* このまま採用
* 範囲変更（Intent の更新）

---

### 3.6 Step 6：AI による最終反映

AI はレビューを反映し、必要なら再度 Self-Monitoring を実行して完成版を提示する。

---

## 4. Repetition（反復）

Step 3〜6 を繰り返す。ただし以下の終了条件を満たした時点でループを終了する：

* Intent（Goal / Scope / Output）が完全に達成されている
* Self-Monitoring により矛盾・不足・制約違反が検出されない
* 推測の混入がない

AI は各サイクルで G0001 の判断4層を必ず再適用する。

---

## 4.1 Question Triggers（質問が必須となるタイミング）

AI は次のいずれかに該当する場合、必ず質問を行う：

* Step 1：Intent（Goal / Scope / Output）が曖昧・不足している
* Step 3：Draft 生成時に不明点がある
* Step 5：人間レビュー後に曖昧さ・矛盾・不足を検出した

---

必要に応じて Step 3〜6 を繰り返すが、**毎サイクルで G0001 の判断4層を適用すること**が必須。

---

## 5. Human Review Criteria（人間によるレビュー基準）

人間は次の観点で Draft を評価する：

* Intent の達成度（Goal / Scope / Output が満たされているか）
* 構造（G0250）の遵守
* 不要な推測が混入していないか
* Principles（Minimality / Consistency / Interpretability）に沿っているか

---

## 6. 禁止事項

* Intent を AI が勝手に補完・改変すること
* 誤った構造・見出し階層の生成
* 生成過程での推測
* G0250 の構造違反
* 人間の指示を無視した再生成

---

## 6. Final Output（最終出力の基準）

最終出力は次をすべて満たす：

* Intent の Goal / Scope / Output を完全充足
* G0250 の構造規範を遵守
* G0001 の原則・制約に反しない
* Self-Monitoring による内部整合性チェック済み

---

(End of G0260 Minimal Workflow)
