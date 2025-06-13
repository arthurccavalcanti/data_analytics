# EULER 6
 
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025. 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# ---------------------

# A soma dos quadrados é 1^2 + 2^2 + 3^2 + ... + 100^2 = 1 + 4 + 9 + ... + 10000
# A diferença entre os termos da sequência forma uma PA (3,5,7,...)

# Estabelece 1 como primeiro termo.
termo_atual = 1

# Estabelece 3 como diferença entre primeiro termo e segundo termo (4 - 1 = 3).
diferenca = 3

# Armazena a soma dos quadrados.
soma_quadrados = 0

# Soma os termos da sequência (1, 4, 9, ..., 10000).
for i in range(100):
  soma_quadrados = soma_quadrados + termo_atual
  termo_atual = termo_atual + diferenca
  diferenca += 2

# O quadrado da soma é (1 + 2 + 3 + ... + 100)^2
# O número a ser elevado ao quadrado é o somatório de uma PA de 100 termos, com razão 1
# A soma de uma PA pode ser encontrado por ((a1+an)*n)/2
# Em que a1 = primeiro termo, an = enésimo termo e n = número de termos


soma_PA_1 = (((1+100)*100)/2)

quadrado_soma = soma_PA_1 ** 2

print(quadrado_soma - soma_quadrados)

