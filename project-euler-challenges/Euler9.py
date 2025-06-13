# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

# -----------------

# Assumindo que a != 0 e b != 0, o o maior valor possível para c é 997 (1 + 2 + 997 = 1000).
# Uma vez que (a < b < c) e (a + b + c = 1000), o menor valor possível para c é 335 (331 + 334 + 335 = 1000).

# Assim, dados os valores de a e b,  c = 1000 - (a + b).
# O valor de a deve variar, portanto, entre 1 [997 = 1000 - (1 + 2)] e 332 [335 = 1000 - (332 + 333)].
# O valor de b deve variar, portanto, entre 2 [997 = 1000 - (1 + 2)] e 499 [335 = 1000 - (1 + 499)].

def py_triplet():
    
    for b in range(2,499):                  # Testa todos os valores possíveis de b.
        for a in range(1,332):              # Testa todos os valores possíveis de a.
            c = 1000 - (a+b)                # Determina o valor de c, dados os valores de a e b.
            
            if c**2 == a**2 + b**2:         # Como há exatamente uma pythagorean triplet, quando a equação for válidoa a função retornará o resultado.
                return a*b*c

print(py_triplet())