# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# -----

# Usando a Sieve of Erathostenes (Peneira de Erasthostenes), achamos todos os primos abaixo de n ao marcar como falso todos os múltiplos de números primos abaixo de n.

from math import sqrt

n = 2*10**6

def primos_menores(n):

    if n == 2:
        return [2]
    if n < 2:
        return []

    primos = [True] * n     # Cria lista com n membros. Se o boolean for True, o número do índice é primo.
    
    primos[0] = False       # Lida com casos triviais, já que 0 e 1 não são primos.
    primos[1] = False

    for i in range(2, int((sqrt(n)+1))):    # Como o maior fator de um número é a raiz quadrade dele, não há necessidade de testar os números maiores.
        if primos[i]:                       # Se o número tiver marcado como verdadeiro, ele é primo.
            for j in range(i**2,n, i):      # Percorre todos os múltiplos de i, começando com seu quadrado (já que seus múltiplos menores já foram marcados pelos primos anteriores).
                primos[j] = False

    return [i for i in range(n) if primos[i]]

def somar_lista(lista):
    soma = 0
    lista = primos_menores(n)

    for i in range(len(lista)):
        soma += lista[i]

    print(soma)

somar_lista(n)