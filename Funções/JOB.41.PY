def área(largura,comprimento):
    return f'A área um terreno de largura={largura} e comprimento={comprimento} é igual a {area:.2f}m²'

largura=float(input('Largura (m):'))
comprimento=float(input('Comprimento (m):'))
area=resposta=largura*comprimento
print(área(largura,comprimento))