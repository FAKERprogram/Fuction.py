from time import sleep
def contador(i,f,p):
    print("-="* 20)
    print(f'A contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if p < 0:
        p*=-1
    if p == 0:
        p == 1
    if i < f:
        cont=i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.4)
            cont +=p
        print('Fim!')
    else:
        cont=i
        while cont >=f:
            print(f'{cont}', end=' ')
            sleep(0.4)
            cont-=p
        print('Fim!')
            
contador(1,10,1)
contador(10,0,-2)
print('\nAgora é a sua vez de personalizar a contagem:')
inic=int(input('Inicio:'))
fim=int(input('Fim:'))
pas=int(input('Passos:')) 
contador(inic,fim,pas)           