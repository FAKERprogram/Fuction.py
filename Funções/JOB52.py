import io
from contextlib import redirect_stdout

def cor_amarela(texto):
    return f'\033[1;43m{texto}\033[0m'

def cor_azul(texto):
    return f'\033[1;44m{texto}\033[0m'

def cor_branca(texto):
    return f'\033[1;37;40m{texto}\033[0m'

# Função que simula o interactive help do Python
def help_python(comando):
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        help(comando)
    return cor_branca(buffer.getvalue())

while True:
    print(cor_amarela('  help      - Exibe este manual.'))
    print(cor_azul('Que informação de qual função você deseja visualizar:'))
    pergunta = input()
    if pergunta.lower() == 'fim':
        break
    print(help_python(pergunta))
    print('"fim" caso queira sair')
