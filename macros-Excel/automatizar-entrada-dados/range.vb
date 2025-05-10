' Retorna seleção
Public Function GetSelecao() As Range
  Set GetSelecao = shNome_Planilha.Range("A1").CurrentRegion
  Set GetSelecao = GetSelecao.Offset(1).Resize(GetSelecao.Rows.Count - 1)
  ' Exclui primeira linha (cabeçalho)
End Function

' Obs. Subtende-se que a primeira linha é cabeçalho e dados começam em A2.
' A = coluna de ID, 2 = primeira linha com dados.
' Nome_Planilha = nome da planilha no workbook.

' Deletar linha
Public Sub DeletarLinha(ByVal linha As Long)
  shNome_Planilha.Range("A2").Offset(linha).EntireRow.Delete
End Sub

' Se linha = 0, Range = A2; se linha = 1, range = A3; etc.

' Retorna lista de itens das colunas
Public Funtion GetColuna1() As Variant
  GetColuna1 = shPlanilha_Aux.ListObjects("Coluna1").DataBodyRange.Value
End Function

Public Funtion GetColuna2() As Variant
  GetColuna2 = shPlanilha_Aux.ListObjects("Coluna2").DataBodyRange.Value
End Function

' Obs. Planilha_Aux = nome da planilha que tem tabelas com dados das listas suspensas.
' Tabelas com dados das listas devem estar formatadas com cabeçalho (caso contrário, a linha do cabeçalho aparecerá como opção).
' Primeira coluna (Coluna0) contém ID da linha. Segunda coluna (Coluna1) contém Campo1, etc. 

' Cria número de ID para novos registros
Public Sub Function GetNovoID() As Long
  GetNovoID = 1 + WorsheetFunction.Max(shNome_Planilha.Range("A2").CurrentRegion.Columns(1))
End Function

' Obs. Subtende-se que coluna de ID é a primeira coluna.