'Macro para iterar número desconhecido de linhas

'Obs. Para funcionar, coluna selecionada não pode ter células vazias.

Sub Linhas()

  ' Seleciona primeira célula com conteúdo da coluna A.
  Range("A2").Select 
  Do Until IsEmpty(ActiveCell)
    ' Insira aqui ocódigo a ser executado em cada linha.
      ActiveCell.Offset(1, 0).Select
  Loop

End Sub