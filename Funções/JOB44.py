from time import sleep

def maior(*num):
    # verificar qual o maior numero dentre varios
    print("-=" * 20)
    print(f'Analisando os valores fornecidos...')
    for n in num:
        print(f'{n} ', end='', flush=True)
        sleep(0.5)
    print(f'\nForam fornecidos {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')

# Chamando a função com números fornecidos
maior(2, 9, 5, 3, 7, 1)