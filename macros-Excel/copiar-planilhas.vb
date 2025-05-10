'Macro para copiar planilhas de um arquivo numa nova planilha:

' Resumo = nome da planilha destino.

Sub Agregar()

  Dim totalPlanilhas As Long
  Dim fimLinha As Integer
  Dim ultimaLinha As Integer

  totalPlanilhas = Worksheets.Count

  For i = 1 To totalPlanilhas
    If Worksheets(i).Name <> "Resumo" Then
      fimLinha = Worksheets(i).Cells(Rows.Count,1).End.(xlUp).Row
      
      For j = 1 To fimLinha
        Worksheets(i).Activate
        Worksheets(i).Rows(j).Select
        Selection.Copy
        Worksheets("Resumo").Activate
        ultimaLinha = Worksheets("Resumo").Cells(Rows.Count,1).End.(xlUp).Row
        Worksheets("Resumo").Cells(ultimaLinha + 1,1).Select
        ActiveSheet.Paste
      Next
    
    End If
  Next

End Sub