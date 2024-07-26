    

def cadastro_usuario():
    nome=input('Nome:')
    email=input('Email:')
    senha=input('Senha:')
    try:
        with open('usuarios.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Usuário:{nome}; Email:{email}; Senha:{senha}\n')
    except FileNotFoundError:
        print('Arquivo não encontrado.')
        open ('usuarios.txt', 'w').close()
    return arquivo
def login(username,email,password):
    try:
        with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
            for line in arquivo:
                usuario, email_pass, senha = line.strip().split(';')
                if username == usuario and email == email_pass and password == senha:
                    return print('Login successful')
    except FileNotFoundError:
        print('Arquivo não encontrado.')
    return False
def menu():
    print('1 - Cadastrar')
    print('2 - Login')
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        cadastro_usuario()
    
    elif escolha == 2:
        username = input('Username: ')
        email = input('Email: ')
        password = input('Senha: ')
        login(username, email, password)
    else:
        print('Opção inválida.')
    return

if __name__ == '__main__':
    menu()