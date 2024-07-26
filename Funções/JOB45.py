import random as rd
from time import sleep
num_aleatorios=[]
def sorteia(numbers):
    print('Os valores sorteados foram:')
    global num_aletorios
    numeros_aletorios=rd.sample(range(1,100), 5)
    num_aleatorios.extend(numeros_aletorios)
    for numero in numeros_aletorios:
        print(f'{numero}', end=' ')
        sleep(0.5)
    print('PRONTO!')
    print()
sorteia(num_aleatorios)

def somapar():
    global num_aleatorios
    soma=0
    for n in num_aleatorios:
        if n % 2 == 0:
            soma += n
    return soma
resultado=somapar()
if resultado == 0:
    print('Não há números pares no sorteio.')
    exit()
else:
    print(f'Somando os valores PARES de {num_aleatorios}, temos {resultado}')        