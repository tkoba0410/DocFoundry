# 3-cod – Coding Standards
本ディレクトリは **コーディング標準** の独立セクションです。  
- **G0300-STD-COD0**: 言語非依存コア規範（MUST/SHOULD/MAY）  
- **G0301-STD-COD1**: C# 言語モジュール（Coreの具体化）

> 参照優先度: COD Core (G0300) ＞ 言語モジュール (G0301) ＞ プロジェクト差異 (project-coding-overrides.yml)

移行ガイド（概要）:
1) 旧 `G0103-STD-DOC3` → 本 `G0300-STD-COD0` へ置換  
2) 旧 `G0104-STD-LANG-CS` → 本 `G0301-STD-COD1-Lang-CSharp` へ置換  
3) CI の参照パスと override キーを `cod.core` / `cod.lang.csharp` に更新
