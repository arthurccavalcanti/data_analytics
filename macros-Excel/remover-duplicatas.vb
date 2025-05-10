' Macro para remover duplicatas da primeira coluna de múltiplos arquivos

Sub RemoverDupli()

Dim planilha As Worksheet
Dim rng As Range
Dim txto As String
Dim T As String ' Guarda temporariamente célula atual
Dim ultimaLinha As Long

For Each planilha In ThisWorkbook.Worksheets
    txto = ""
    With planilha
      ultimaLinha = .Cells(Rows.Count, 1).End(xlUp).Row

      For Each rng In planilha.Cells(1, 1).Resize(LstRw, 1)
        T = rng.Value
        
        ' Checa se célula atual está em txto
        If InStr(1, txto, "|" & T, vbTextCompare) <> 0 Then
          ' Limpa célula se for uma duplicata
          rng.ClearContents
        End If
        
        ' Juntar valor atual com texto usando "|" como separador
        txto = txto & "|" & T
      Next
    End With
  Next

End Sub