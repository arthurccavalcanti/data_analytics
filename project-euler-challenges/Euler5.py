# Euler 5:
# 2520 is the smallest number that can be divided by each of the numbers form 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# ---------

# Encontramos o MMC de 1-20
# Usamos a propriedade associativa do MMC para encontrar o MMC do conjunto
# mmc(a,b,c) = mmc(a,mmc(b,c))
# mmc(a,b) = |a|*(|b|/mdc(a,b))

from functools import reduce
 
# Baseado no algoritmo de Euclid, retorna o MDC de dois números.
def mdc(x, y):
    while y:
        x, y = y, x % y
    return x

# Retorna o MMC de dois números.
def mmc(a, b):
    return a * (b / mdc(a, b))

# Repetidamente chama mmc(a, b) para cada par de números de 1-20.
def mmc_range(range_num):
    return reduce(mmc, range_num)

solution = mmc_range((range(1,21)))

print(solution)

# Resultado = 232792560.0



