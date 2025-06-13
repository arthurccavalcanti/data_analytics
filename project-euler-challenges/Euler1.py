# Retorna a soma de todos os fatores de x menores que n.
def soma_fatores_x_menores_n(x, n):
  
  num_multiplos = (n-1) // x           # Guarda quantidade de múltiplos de x menores do que n.
  
  enesimo_termo = num_multiplos * x    # Guarda o maior múltiplo de x menor do que n.
  
  soma = num_multiplos * (x + enesimo_termo)/2

  return soma

res = soma_fatores_x_menores_n(3, 1000) + soma_fatores_x_menores_n(5, 1000) - soma_fatores_x_menores_n(15, 1000)

print(res)