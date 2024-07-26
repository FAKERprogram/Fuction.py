def Leiaint(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print('Valor inválido. Digite um número inteiro.')

# Exemplo de uso
numero = Leiaint('Digite um número: ')
print(f'Você digitou o número {numero}')
