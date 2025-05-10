' Exibe formulário
Public Sub Main()
  Dim frm As New Formulario_principal
  frm.Show vbModal ' vbModal => usuário é obrigado a fechar formulário para realizar um ação no Excel.
  set frm = Nothing
End Sub

' Obs. Formulario_princial = nome do formulário principal.