'Formulário editar linha:

Private m_linhaAtual As Long  ' Variável de membro para linha atual

' Passa valor de uma nova linha para linhaAtual
Public Property Let LinhaAtual(ByVal novaLinhaAtual As Long)
  m_linhaAtual = novaLinhaAtual
End Property

' Carrega dados na lista (após quaisquer edições)
Private Sub Formulario_Ativar()
  Call PreencherListas
  Call CarregarDados  
End Sub

' Botão fechar
Private Sub buttonFechar_Click()
    Unload Me
End Sub

' Botão atualizar
Private Sub buttonAtualizar_Click()
  Call SalvarDadosPlanilha()
End Sub

' Preenche lista
Public Sub PreencherListas()  
  Me.ComboColuna1.List = GetColuna1()
  Me.ComboColuna2.List = GetColuna2()
End Sub

' Carrega dados para controles
Public Sub CarregarDados()

  With shNome_Planilha.Range("A2").Offset(m_linhaAtual)
    textboxCampo1.Value = .Cells(1,1).Value
    textboxCampo2.Value = .Cells(1,2).Value
    ' etc.
    OptionOpcao1.Value = iif(.Cells(1,3).Value="Opção1",True,False)
    OptionOpcao2.Value = iif(.Cells(1,3).Value="Opção2",True,False)
    ComboColuna1.Value = .Cells(1,4).Value
  End With

End Sub

' Obs. Se m_linhaAtual = 0, Range = A2; se m_linhaAtual = 1, range = A3; etc.

' Salva dados dos controles na planilha
Public Function SalvarDadosPlanilha()

  If MSGbox("Você quer atualizar?", vbYesNo, "Atualizar") = vbYes Then
      With shNome_Planilha.Range("A2").Offset(m_linhaAtual)
        Cells(1,1).Value = textboxCampo1.Value
        .Cells(1,2).Value = textboxCampo2.Value
        ' etc.
        .Cells(1,3).Value = iif(OptionOpcaoo1.Value = True, "Opção1", "Opção2")
        .Cells(1,4).Value = ComboColuna1.Value
      End With
  End If

End Function