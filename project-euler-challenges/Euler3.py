import math

def maior_fator_primo(n): 
  
    maior_primo = 0
 
    # Dividimo n por 2 até eliminarmos todos os fatores não primos pares.
    while n % 2 == 0: 
        maior_primo = 2
        n = n // 2
 
  # Este loop passa por todos os possíveis fatores ímpares de n até a raiz de n.
    for i in range(3, int(math.sqrt(n)) + 1, 2): 

        while n % i == 0: 
            maior_primo = i   # Atualizamos para o maior primo até o momento.
            n = n // i 
 
    # Se a esta altura n ainda for maior que 2, então n deve ser primo.
    # Caso contrário, o maior primo está em maior_primo
    return n if n > 2 else maior_primo

print(maior_fator_primo(600851475143))