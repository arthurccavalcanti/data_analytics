'Macro para automatizar backup

' Crie uma pasta com o arquivo .xls e uma pasta nomeada ‘backup’.

Sub SaveWorkbookBackup()

Dim folderPath As String
Dim bckup As String
Dim timeStamp As String

  folderPath = ActiveWorkbook.Path & "\backup\"

  If Dir(folderPath, vbDirectory) = "" Then
    MkDir folderPath
  End If

  timeStamp = Format(Now, "ddmmyyy_HHmmss")

  ' Para outros tipos de arquivo, mudar extensão .xlsm
  bckup = folderPath & ActiveWorkbook.Name & "_" & timeStamp & ".xlsm"

  ActiveWorkbook.SaveCopyAs bckup

  MsgBox "Backup salvo: " & bckup, vbInformation, "Backup Feito"
  ActiveWorkbook.Close

End Sub