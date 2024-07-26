def notas(*notas, sit=False):
    # Calcular a média
    media = sum(notas) / len(notas)
    
    # Montar o dicionário com as informações
    alunos = {
        'Quantidade_de_notas': len(notas),
        'Media': media,
        'Maior_nota': max(notas),
        'Menor_nota': min(notas)
    }
    
    # Verificar a situação se solicitado
    if sit:
        if media <= 5:
            alunos['Situação'] = "Ruim"
        elif media <= 6.9:
            alunos['Situação'] = "Instável"
        else:
            alunos['Situação'] = "Boa"
    
    return alunos

quantidade_notas = int(input('Quantos alunos você deseja adicionar: '))
notas_alunos = []

for _ in range(quantidade_notas):
    nota = float(input('Digite a nota: '))
    notas_alunos.append(nota)

# Verificar se a situação deve ser incluída
situacao = input('Gostaria de ver a situação? (S/N) ').strip().lower() in ('s', 'sim')

# Chamar a função com as notas e a situação (se aplicável)
resultado = notas(*notas_alunos, sit=situacao)

# Exibir o resultado
print(resultado)
