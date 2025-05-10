# README - Limpeza Dados
Este documento descreve as atividades realizadas para o aprimoramento do dataset Company.

_(Ajustes de tipo de dados, análise de nulos, criação de novas visualizações e consultas SQL.)_

# Atividades Realizadas
## 1. Verificação de Cabeçalhos e Tipos de Dados

Revisar os cabeçalhos das tabelas e confirmar que os tipos de dados correspondem às necessidades dos dados armazenados.

## 2. Modificação dos Valores Monetários

Modificar a coluna Salary e outras colunas monetárias de DECIMAL para DOUBLE com precisão necessária.

## 3. Verificação e Análise de Nulos

Verificar a existência de valores nulos e determinar se devem ser removidos ou substituídos.


## 4. Identificação de Colaboradores sem Gerente

Identificar colaboradores cujo Super_ssn está nulo e analisar se eles são gerentes.

## 5. Verificação de Departamentos sem Gerente

Verificar se há departamentos sem um gerente associado.

  
## 6. Preenchimento de Departamentos sem Gerente

Atualizar a tabela departament com os dados necessários para preencher as lacunas.


## 7. Verificação do Número de Horas dos Projetos

Consultar a tabela works_on para obter a soma das horas trabalhadas por projeto.


## 8. Separação de Colunas Complexas

Criar novas colunas para armazenar dados que eram combinados em uma única coluna.


## 9. Mesclagem de Consultas entre employee e departament

Realizar uma junção entre employee e departament.


## 10. Eliminação de Colunas Desnecessárias

Eliminar colunas desnecessárias de cada tabela.


## 11. Junção dos Colaboradores com Nomes dos Gerentes

Associar os nomes dos colaboradores com seus respectivos gerentes.


## 12. Mesclagem dos Nomes e Sobrenomes dos Colaboradores

 Mesclar as colunas Fname e Lname.


## 13. Mesclagem dos Nomes de Departamentos e Localizações

Concatenar Dname e Dlocation.


 Justificativa para Mesclagem em vez de Atribuição:

> A mesclagem é usada para criar uma coluna que combina dados de duas colunas existentes, facilitando análises futuras e garantindo a unicidade. 
    
> A atribuição não é adequada porque não combina os dados em uma única coluna.

## 15. Agrupamento de Dados por Gerente

Agrupar os dados e contar o número de colaboradores para cada gerente.


----

## Mesclar Colunas

Mesclar colunas refere-se ao processo de combinar o conteúdo de duas ou mais colunas em uma nova coluna única. 

    Quando você deseja combinar valores de várias colunas em uma coluna única.

    Quando você precisa criar uma coluna de chave composta ou concatenar informações para análise.


No Power Query Editor:
- Selecionar Colunas: Escolha as colunas que você deseja mesclar.
- Mesclar Colunas: Vá para a guia "Transformar" e selecione "Mesclar Colunas".
- Definir Delimitador: Escolha um delimitador, como um espaço ou hífen, para separar os valores combinados.
- Aplicar: A nova coluna será criada contendo os valores mesclados.

Exemplo:
- Se você tem colunas FirstName e LastName e deseja criar uma coluna FullName, você pode mesclar essas colunas.


FirstName | LastName | FullName
----------|----------|----------
John      | Doe      | John Doe
Jane      | Smith    | Jane Smith

**No DAX**:

Criar Coluna Calculada: Use a função CONCATENATE ou o operador & para criar uma nova coluna.

> DAX
>
> FullName = [FirstName] & " " & [LastName]



## Query SQL utilizada:

    SELECT e.Fname AS Employee_First_Name,
    e.Lname AS Employee_Last_Name,
    m.Fname AS Manager_First_Name,
    m.Lname AS Manager_Last_Name
    FROM employee e
    LEFT JOIN employee m ON e.Super_ssn = m.Ssn