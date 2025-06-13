# By listing the first six prime numbers: 2, 3, 5, 7, 111 and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# --------------

from math import isqrt

n1 = 6
n2 = 10001

def ultimo_primo(n):
    if n == 2:                  # Lida com casos triviais.
        return 2
    elif n == 1:
        return None
    
    num_teste = 3               # Possível número primo. 
    lista_primos = [2]          # Lista de números primos.

    while len(lista_primos) < n:
        # O número será primo se não for divisível por nenhum outro primo menor do que ele.
        # Testamos a divisão até a raiz quadrada do possível número primo (uma vez que a raiz quadrada do número é o maior fator possível do número).

        if all(num_teste % primo for primo in lista_primos[:(int(isqrt(num_teste)))]):
            lista_primos.append(num_teste)                                                   
        num_teste += 2                                                                                    
    
    return lista_primos[-1]


          
print(ultimo_primo(n2))