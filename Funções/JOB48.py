def fatorial(numero, show=True):
    if numero <= 0:
        return 1
    f=1
    for i in range(numero,0,-1):
        f*=i
    if 
        show= True
        print(f'{i}', end='')
    if escolha in 'Nn':
        show = False
        return f

n=int(input('Digite um numero inteiro:'))
escolha=input('Deseja que o calculo do fatorial apareca? [sim/não]:')
fatorial(n, escolha)