# define a função coloca os parametros com nome=desconhecido(caso o nome não seja fornecidos e gols como 0 caso também não seja fornecidos)
def ficha(nome='<Desconhecido>',gols=0):
    # Coloca um retorno com uma f'string personalizada, retornando o nome e o numero de golsdo jogador.
        return f'O jogador {nome} fez {gols} no campeonato.'    
    #declara as variaveis para receber as informações 
Nome_jogador=input('Nome do Jogador:')
Numero_gols=input('Numero de Gols:')
# utiliza as funções if e not para verificar se as variaveis estão vazias.
if not Nome_jogador:
    Nome_jogador = '<Desconhecido>'
if not Numero_gols.isdigit():
    Numero_gols = 0
else:
    Numero_gols = int(Numero_gols)
# chama a função atribuindo a elas os valores das variaveis
resposta=ficha(Nome_jogador,Numero_gols)
# print na função
print(resposta)

    