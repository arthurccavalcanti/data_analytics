'Formulário nova linha:

' Inicializa formulário
Private Sub Formulario_Inicializar()
  Call CriarNovoID
  Call InicializarControles
End Sub

' Botão fechar
Private Sub buttonFechar_Click()
    Unload Me
End Sub

' Botão para salvar dados da nova linha
Private Sub buttonSalvar_Click()
  If MSGbox("Você quer salvar uma nova linha?", vYesNo,"Salvar") = vsYes Then
    Call SalvarDadosPlanilha
    Call LimparCaixas
    Call CriarNovoID
  End If
End Sub

' Atribui novo ID ao textbox do formulário
Private Sub CriarNovoID()
  Me.textboxID.Value = GetNovoID()
End Sub

' textboxID = caixa de texto (label) com ID da linha.

' Salva nova linha
Private Function SalvarDadosPlanilha()
  Dim novaLinha As Long

  With shNome_Planilha
    novaLinha = 1 + .Cells(.Rows.Count,1).end(xlup).Row
    .Cells(novaLinha,1).Value = textboxCampo1.Value
    .Cells(novaLinha,2).Value = textboxCampo2.Value
    .Cells(novaLinha,3).Value = textboxCampo3.Value
    ' etc.
    .Cells(newRow, 4).Value = iif.(OptionOpcao1.Value = "True", "opção1", "opção2")
  End With

End Function

' Obs. Campo1, Campo2, etc são os nomes dos campos nas caixas de texto.
' Ex. Campo1 = Nome, Campo2 = Idade, etc.
' Os campos devem estar na ordem em que as colunas aparecem. Coluna1 => Campo1.

' Limpa dados
Private Sub LimparCaixas()
  Dim c As Control
  For Each c in Me.Controls
    If TypeName(c) = "TextBox" Then  ' Se o campo for uma caixa de texto,
      c.Value = ""                   ' limpa os dados.
    End If
  Next c
End Sub

' Inicializa e preenche listas suspensas e OptionButtons
Private Sub InicializarControles()

  Me.ComboColuna1.List = GetColuna1()   ' Atribui lista de itens da coluna1
                                        ' à lista suspensa da coluna1.

  Me.ComboColuna1.ListIndex = 0         ' Seleciona primeiro elemento da lista
                                        ' suspensa da coluna1.
  Me.ComboColuna2.List = GetColuna2()
  Me.ComboColuna2.ListIndex = 0
  ' etc.
  Me.OptionOpção1.Value = True

End Sub