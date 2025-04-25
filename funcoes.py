import random

def rolar_dados(n):
    i = 0 
    lista = []
    while i<n: 
        dado = random.randint(1,6)
        lista.append(dado)
        i += 1 
    return lista