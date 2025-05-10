# README: Construção de um Diagrama Star Schema no Power BI

Este documento descreve o processo de construção de um diagrama Star Schema no Power BI.
O modelo contém tabelas de dimensão e uma tabela fato, com detalhes sobre a criação de uma tabela de calendário usando DAX e a agregação de dados nas tabelas de dimensão.

## Estrutura do Modelo

### Tabelas de Dimensão
1. **D_Produtos**
   - **ID_produto**: Identificador único do produto.
   - **Produto**: Nome do produto.
   - **Média de Unidades Vendidas**: Média de unidades vendidas.
   - **Médias do valor de vendas**: Média dos valores de vendas.
   - **Mediana do valor de vendas**: Mediana dos valores de vendas.
   - **Valor máximo de Venda**: Valor máximo registrado de venda.
   - **Valor mínimo de Venda**: Valor mínimo registrado de venda.

2. **D_Produtos_Detalhes**
   - **ID_produto**: Identificador do produto (chave estrangeira).
   - **Discount Band**: Faixa de desconto.
   - **Sale Price**: Preço de venda.
   - **Units Sold**: Unidades vendidas.
   - **Manufactoring Price**: Preço de fabricação.

3. **D_Descontos**
   - **ID_produto**: Identificador do produto (chave estrangeira).
   - **Discount**: Valor do desconto.
   - **Discount Band**: Faixa de desconto.

4. **D_Calendário**
   - Criada através da função DAX `CALENDAR()`.

### Tabela Fato
1. **F_Vendas**
   - **SK_ID**: Identificador único da venda.
   - **ID_Produto**: Identificador do produto (chave estrangeira).
   - **Produto**: Nome do produto.
   - **Units Sold**: Unidades vendidas.
   - **Sales Price**: Preço de venda.
   - **Discount Band**: Faixa de desconto.
   - **Segment**: Segmento de mercado.
   - **Country**: País.
   - **Salers**: Vendedor.
   - **Profit**: Lucro.
   - **Date**: Data da venda.

## Etapas para Construir o Diagrama Star Schema

### 1. Criação da Tabela Calendário

Para criar uma tabela Calendário com um intervalo de datas usando DAX:

1. **Criação de uma nova tabela**:
   - Na aba "Modelagem" -> "Nova Tabela".

2. **Fórmula DAX**:
   - Função `CALENDAR()` para criar uma tabela de datas contínuas. 

     ```DAX
     D_Calendário = CALENDAR(DATE(yyyy, mm, dd), DATE(yyyy, mm, dd))
     ```

3. **Colunas Adicionais**:
   - Para facilitar análises temporais, colunas de Ano, Mês, e Dia da Semana:

     ```DAX
     Ano = YEAR(D_Calendário[Date])
     Mês = FORMAT(D_Calendário[Date], "MMMM")
     Dia_da_Semana = FORMAT(D_Calendário[Date], "dddd")
     ```

### 2. Criação e Agregação de Dados nas Tabelas de Dimensão

1. **Tabela D_Produtos**:
   - **Média de Unidades Vendidas**:
     ```DAX
     Média_Unidades_Vendidas = AVERAGE(F_Vendas[Units Sold])
     ```

   - **Médias do Valor de Vendas**:
     ```DAX
     Média_Valor_Vendas = AVERAGE(F_Vendas[Sales Price])
     ```

   - **Mediana do Valor de Vendas**:
     ```DAX
     Mediana_Valor_Vendas = MEDIAN(F_Vendas[Sales Price])
     ```

   - **Valor Máximo de Venda**:
     ```DAX
     Valor_Maximo_Venda = MAX(F_Vendas[Sales Price])
     ```

   - **Valor Mínimo de Venda**:
     ```DAX
     Valor_Minimo_Venda = MIN(F_Vendas[Sales Price])
     ```

2. **Tabela D_Produtos_Detalhes**:
   - Colunas de agregação similares ou detalhes específicos.

3. **Tabela D_Descontos**:
   - Colunas que sintetizem as informações de desconto e faixa de desconto.

### 3. Estabelecimento dos Relacionamentos

1. **Relacionamento entre `F_Vendas` e `D_Produtos`**:
   - **Relacionamento**: `F_Vendas[ID_Produto]` → `D_Produtos[ID_produto]`
   - Tipo de Relacionamento: Muitos para Um (M:N) com `D_Produtos` sendo a tabela de dimensão.

2. **Relacionamento entre `F_Vendas` e `D_Calendário`**:
   - **Relacionamento**: `F_Vendas[Date]` → `D_Calendário[Date]`
   - Tipo de Relacionamento: Muitos para Um (M:N) com `D_Calendário` sendo a tabela de dimensão.

3. **Relacionamento entre `D_Produtos` e `D_Produtos_Detalhes`**:
   - **Relacionamento**: `D_Produtos[ID_produto]` → `D_Produtos_Detalhes[ID_produto]`
   - Tipo de Relacionamento: Um para Muitos (1:N) com `D_Produtos` sendo a tabela de dimensão.

4. **Relacionamento entre `D_Produtos` e `D_Descontos`**:
   - **Relacionamento**: `D_Produtos[ID_produto]` → `D_Descontos[ID_produto]`
   - Tipo de Relacionamento: Um para Muitos (1:N) com `D_Produtos` sendo a tabela de dimensão.