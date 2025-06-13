# Diz se número é um palíndromo.
def palindromo(num):
  
  # Converte para string para podermos acessar os dígitos via índices.
  num_str = str(num)     

  for digito_direita in range(len(num_str)//2): # Percorre até a metade do número.

    # Estabelece o índice do dígito da esquerda.
    digito_esquerda = (len(num_str)) - digito_direita - 1

    # Caso os valores dos dígitos não sejam o mesmo, não é um palíndromo.
    if num_str[digito_direita] != num_str[digito_esquerda]: 
      return False

  # Caso os valores sejam os mesmos para todos os dígitos, é um palíndromo.
  return True


def maior_palindromo_por_digito(n):
  
  maior_palindromo = 0

  # Estabele o maior e o menor número de n dígitos.
  maior_num = (10 ** n) - 1
  menor_num = (10 ** (n-1))

  # Percorre do maior ao menor número, testando seus produtos.
  for i in range(maior_num, menor_num, -1):
    
    # Se o produto for menor do que o palíndromo atual, ignoramos.
    if maior_palindromo >= (i * maior_num):
      break

    # Caso o contrário, testamos o produto do número atual com todos os outros números de 3 dígitos menores.
    for j in range(i, menor_num, -1):
      produto = i * j
      
      # Se o produto for maior que o maior atual e também for um palíndromo, atualizamos.
      if produto > maior_palindromo:
        if palindromo(produto):
          maior_palindromo = produto
  
  return maior_palindromo

print(maior_palindromo_por_digito(4))

# Resultado = 99000099