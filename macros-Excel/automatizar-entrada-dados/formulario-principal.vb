'Formulário principal:

' Botão fechar
Private Sub botao_fechar()
  Unload Me
End Sub

' Obs. Propriedade Cancel do botão = True => Pressionar Esc roda código do botão.

' Botão ok
Sub botao_ok()
  ActiveCell.Value = ListBox1.Value
  Unload Me
End Sub

' Botão inserir nova linha
Private Sub buttonNovo_Click()
  Dim formlr as New Formulario_Novo
  formlr.Show vbModal
  Call AddDadosListBox ' Atualiza listbox com linhas recém inseridas.
End Sub

' Obs. Formulario_Novo = nome do formulário para inserir linha.

' Botão editar
Private Sub buttonEditar_Click()
  Call EditarLinha
End Sub

' Botão deletar linha
Sub deletar_Click()
  call DeletarLinha(nome_listbox.ListIndex)
End Sub

' Preenche formulário principal com dados
Private Sub Formulario_Inicializar()
  Call AddDadosListBox
End Sub

' Adiciona ao ListBox
Private Sub AddDadosListBox()

  Dim rng As Range
  Set rng = GetSelecao()
  ' Conecta dados com listBox do formulário.

  With nome_listbox
    .RowSource = rng.Address(external:=True)  ' external = True => Referência de planilha externa
    .ColumnCount = rng.Columns.Count          ' Para exbir nº de colunas
    .ColumnsWidths = "30;85;85;150;150;100"   ' Define largura das colunas
    .ColumnHeads = True                       ' Para exibir cabeçalho
    .ListIndex = 0                            ' Para selecionar 1º item
  End With
End Sub

' Obs. nome_listbox = nome da listbox que exibe dados no formulário principal.

' Edita linha
Private Sub EditarLinha()
  Dim formlr As New Formulario_Editar

  formlr.LinhaAtual = listboxNome_Planilha.ListIndex
  ' Atribui valor selecionado na listabox à propriedade linhaAtual.
  formlr.Show vbModal
End Sub

' Obs. Formulario_Editar = nome do formulário para editar uma linha.