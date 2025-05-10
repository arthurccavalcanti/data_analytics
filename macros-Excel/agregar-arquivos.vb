'Macro para agregar dados de diferentes arquivos num só arquivo:

'Crie arquivo final. Exemplo: ‘Arquivofinal.xls’.
'Coloque caminho da pasta com os arquivos a serem manipulados numa célula. Exemplo: B2 = PastaCompartilhada\Recurso.

Sub CombinarArquivos()

  Dim ArquivoNome as String, ArquivoPath As String
  Dim Planilha as Worksheet
  
  Application.ScreenUpdating = False
  
  ArquivoPath = Worksheets("Arquivo final".cells(2,2).VALUE
  ArquivoNome = Dire(ArquivoPath &"\*.xls*")                                ' Restringe para arquivos .xls
  
  Do While ArquivoNome <> ""
    Workbooks.Open filename:=ArquivoPath & "\"&AquivoNome, Readonly:=True
    For Each Sheet in ActiveWorkbook.Sheets
      Sheet.Copy After:=ThisWorkbook.Sheets(1)
    Next Sheet
    
    Workbooks(ArquivoNome).Close
    ArquivoNome = Dir()
  Loop
  
  Application.ScreenUpdating=True

End Sub