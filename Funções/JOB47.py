from datetime import datetime
def voto(ano_nascimento):
    idade= datetime.now().year - ano
    if idade >= 18:
        return(f'Você tem já tem {idade} anos, Voto obrigatório!')
    elif idade <= 15:
        return(f'Você tem {idade} anos, você é menor de idade. Voto negado!')
    else:
        return(f'Você tem {idade} anos, Voto opcional!')
    
    
ano=int(input('Data de nascimento:'))
resultado=voto(ano)
print(resultado)