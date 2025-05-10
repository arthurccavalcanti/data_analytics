' O código copia colunas e linhas à direita/abaixo da Coluna “cabeçalho_Coluna”.
' Resumo = nome da planilha para onde o resumo será copiado.
' Cada planilha deve ter uma coluna de ‘cabeçalho_Coluna’ para indicar de onde iniciar a extração.

Sub agregar()
    
    Application.ScreenUpdating = False ' Desativa atualização de tela

    Dim planilha As Worksheet
    Dim i As Integer
    Dim comcol As Integer ' Começo coluna
    Dim fimcol As Integer ' Fim coluna
    Dim comlinha As Integer ' Começo linha
    Dim fimlinha As Integer ' Fim linha
    Dim colrng As Range ' Range da coluna extraída
    Dim totlinha As Integer ' Total de linhas
    Dim j As Integer ' Contador de linhas para planilha Resumo
    Dim itm As Range ' Range da linha atual a ser copiada
   
    ' Inicializa contador de linha
    j = 1

    For Each planilha In Worksheets
        If planilha.Name = "Resumo" Then GoTo Nextplanilha: ' Pula planilha Resumo.
         
        comcol = 1 ' Inicializa primeira coluna para extração.

        Set colrng = planilha.Cells.Find("cabeçalho_Coluna", LookAt:=xlPart, MatchCase:=False)
        ' Inicia contagem de linhas

        If Not colrng Is Nothing Then
          comlinha = colrng.Row
          Else
          ' Se cabeçalho não for achado, pula pra próxima planilha.
          GoTo Nextplanilha:
        End If

        ' Última coluna usada
        fimcol = colrng.Offset(1, 0).End(xlToRight).Column
        ' Última linha usada
        fimlinha = planilha.Cells.SpecialCells(xlCellTypeLastCell).Row

        Set colrng = Nothing 'Limpa variável.
        totlinha = fimlinha - comlinha ' Número total de linhas.

        ' Loop itera cada linha da planilha atual para copiar.
        For i = 1 To totlinha
            Set itm = planilha.Range(planilha.Cells(comlinha + i, comcol), planilha.Cells(comlinha + i, fimcol))
            
            ' Copia linha atual para próxima linha de Resumo
            Worksheets("Resumo").Range(Worksheets("Resumo").Cells(j + 1, 1), Worksheets("Resumo").Cells(j + 1, fimcol)).Value = itm.Value
            
            j = j + 1
        Next i

    Next planilha

    Application.ScreenUpdating = True

End Sub