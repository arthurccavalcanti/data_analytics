# Recebe dois últimos termos de uma sequência de Fibonacci.
def fib(penultimo, ultimo):

    sum = 0                            # Armazena soma total.
  
    while penultimo <= 4000000:
        if penultimo % 2 == 0:          
            sum += penultimo
        temp = penultimo               # Armazena valor do penúltimo termo.
        penultimo = ultimo             # Atualiza a variável do penúltimo termo.
        ultimo += temp                 # Soma valores do penúltimo e do último termo.
   

    return sum

print(fib(1,2))