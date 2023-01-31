'''
PROGRAMA DESENVOLVIDO PARA FINS EDUCACIONAIS
CURSO DE PYTHON PARA ANALISE DE DADOS - 2023.1
INSTITUICAO LICEU DO CONJUNTO CEARA - FORTALEZA
SOFTWARE DE APOIO A VISUALIZACAO DA SITUACAO DE CADA ALUNO
'''

import os

lista_de_alunos = []
lista_admin = []

def abrir_arquivo_alunos():
    with open('Cadastro-De-Alunos-Liceu/alunos.txt','a') as arq:
        return arq

def abrir_arquivo_admin():
    with open('Cadastro-De-Alunos-Liceu/alunos_admin.txt','a') as arq:
        return arq

def ler_arquivo_alunos():
    with open('Cadastro-De-Alunos-Liceu/alunos.txt','r') as arq:
        dados = arq.readlines()
        return dados

def ler_arquivo_admin():
    with open('Cadastro-De-Alunos-Liceu/alunos_admin.txt','r') as arq:
        dados = arq.readlines()
        return dados

def adicionar_arquivo_alunos(item):
    with open('Cadastro-De-Alunos-Liceu/alunos.txt','a') as arq:
        arq.write(item)

def adicionar_arquivo_admin(item):
    with open('Cadastro-De-Alunos-Liceu/alunos_admin.txt','a') as arq:
        arq.write(item)

def sobrescrever_arquivo_alunos():
    with open('Cadastro-De-Alunos-Liceu/alunos.txt','w') as arq:
        pass

def sobrescrever_arquivo_admin():
    with open('Cadastro-De-Alunos-Liceu/alunos_admin.txt','w') as arq:
        pass

def adicionar_na_lista_alunos():
    lista_de_alunos.clear()
    abrir_arquivo_alunos()
    linhas = ler_arquivo_alunos()
    for linha in linhas:
        dados = linha.split(' ; ')
        aluno = {
            'primeiro_nome':dados[0],
            'segundo_nome':dados[1],
            'matricula':dados[2],
            'idade':dados[3],
            'email':dados[4],
            'serie':dados[5],
            'genero':dados[6],
        }
        lista_de_alunos.append(aluno)

def adicionar_na_lista_admin():
    lista_admin.clear()
    abrir_arquivo_admin()
    linhas = ler_arquivo_admin()
    for linha in linhas:
        dados = linha.split(' ; ')
        dado = {
                'matricula':dados[0],
                'nota1':dados[1],
                'nota2':dados[2],
                'nota3':dados[3],
                'faltas':dados[4]
        }
        lista_admin.append(dado)

def conferir_matricula(matricula):
    #verificar se as matriculas ja existem
    for cada_aluno in lista_de_alunos:
        if str(matricula) == cada_aluno['matricula']:
            print('\nMATRICULA EXISTENTE!')
            return False          
    return True

def cadastrar_aluno():
    matricula = int(input('\nQual a sua matricula? '))    
    if conferir_matricula(matricula):

        primeiro_nome = str(input('\nInsira seu primeiro nome: ')).title()
        sobrenome = str(input('\nInsira seu sobrenome: ')).title()
        email = input('\nInsira seu email: ').lower()
        genero = input('''\n
Qual seu genero? 
\nMasculino = M
Feminino = F 
Outro = O
Prefiro não informar = P

Escolha --> ''').upper()
        serie = int(input('\nQual sua serie? 1, 2 ou 3?: '))
        idade = int(input('\nQual a sua idade? '))

        conteudo = f'{primeiro_nome} ; {sobrenome} ; {matricula} ; {idade} ; {email} ; {serie} ; {genero} ; \n'
        conteudo2 = f'{matricula} ; 0 ; 0 ; 0 ; 0 ; \n' 

        adicionar_arquivo_alunos(conteudo)
        adicionar_arquivo_admin(conteudo2)

        print("\nALUNO CADASTRADO COM SUCESSO!!")

def relatorio_de_alunos():

    adicionar_na_lista_alunos()

    print('\n' + 12*'   ' + 'LISTA DE ALUNOS MATRICULADOS NO CURSO '+ '\n'+ 113*'_'+ '\n')
    print('{:15s} | {:20s} | {:6s} | {:5s} | {:34s} | {:3s} | {:3s}\n'.format('Primeiro Nome','Segundo Nome','Matricula','Idade','Email','Serie','Genero') + 113 *'_' + '\n')
    #para cada dicionario da lista, printe as seguintes informações deles:
    for cada_aluno in lista_de_alunos:
        print("{:15} | {:20} |  {:6}   |   {:4}|  {:30}    | {:3}   | {:3}".format(cada_aluno['primeiro_nome'],cada_aluno['segundo_nome'],cada_aluno['matricula'],cada_aluno['idade'],cada_aluno['email'],cada_aluno['serie'],cada_aluno['genero']))

def remover_aluno():
    
    adicionar_na_lista_alunos()
    adicionar_na_lista_admin()

    matricula = int(input('Qual a matricula do aluno? '))

    if conferir_matricula(matricula) == False:
        for cada_aluno in lista_de_alunos:
            if cada_aluno['matricula'] == str(matricula):
                print('\n')
                for key in cada_aluno:
                    print(f'{key.title()} -> {cada_aluno[key]}')
                print('\n')
                escolha = input('esse é o aluno que voce deseja remover? S ou N: ').upper()
                if escolha == 'S':
                    nova_lista_de_alunos = [x for x in lista_de_alunos if x['matricula'] != str(matricula)]
                    
                    sobrescrever_arquivo_alunos()

                    for cada_aluno in nova_lista_de_alunos:
                        conteudo = f"{cada_aluno['primeiro_nome']} ; {cada_aluno['segundo_nome']} ; {cada_aluno['matricula']} ; {cada_aluno['idade']} ; {cada_aluno['email']} ; {cada_aluno['serie']} ; {cada_aluno['genero']} ; \n"
                        adicionar_arquivo_alunos(conteudo)

                    nova_lista_admin = [x for x in lista_admin if x['matricula'] != str(matricula)]
                    sobrescrever_arquivo_admin()

                    for i in nova_lista_admin:
                        cont = f"{i['matricula']} ; {i['nota1']} ; {i['nota2']} ; {i['nota3']} ; {i['faltas']} ; \n"
                        adicionar_arquivo_admin(cont)
                else:
                    print('\nEntendido!')
    else:
        print('\nMatricula nao encontrada!')

def atualizar_notas():

    adicionar_na_lista_admin()
    
    print(lista_admin)
    matricula = str(input('Qual a matricula do aluno? '))

    if conferir_matricula(matricula) == False:
        for cada_aluno in lista_admin:
            if cada_aluno['matricula'] == str(matricula):
                print('\nDados: \n')
                for key in cada_aluno:
                    print(f'{key.title()} -> {cada_aluno[key]}')
                print('\n')
                escolha = input('Esse é o aluno que você deseja alterar a nota? S ou N: ').upper()
                if escolha == 'S':
                    nota1 = input('Qual a nota 1? ')
                    nota2 = input('Qual a nota 2? ')
                    nota3 = input('Qual a nota 3? ')
                    novo_dicicionario_admin = {
                        'matricula':matricula,
                        'nota1':nota1,
                        'nota2':nota2,
                        'nota3':nota3,
                        'faltas': cada_aluno['faltas']
                    }
                    nova_lista_de_alunos = [x for x in lista_admin if x['matricula'] != str(matricula)]
                    nova_lista_de_alunos.append(novo_dicicionario_admin)

                    sobrescrever_arquivo_admin()

                    for cada_aluno in nova_lista_de_alunos:
                        conteudo = f"{cada_aluno['matricula']} ; {cada_aluno['nota1']} ; {cada_aluno['nota2']} ; {cada_aluno['nota3']} ; {cada_aluno['faltas']} ; \n"
                        adicionar_arquivo_admin(conteudo)
                    
                    print('Concluido!')
                    return nova_lista_de_alunos
                    
                print('Ok, voltando ao menu!')
        else:
            return lista_admin
    else:
        print('\nMatricula nao encontrada!')

def atualizar_faltas():

    adicionar_na_lista_admin()

    matricula = str(input('Qual a matricula do aluno? '))

    if conferir_matricula(matricula) == False:
        for cada_aluno in lista_admin:
            if cada_aluno['matricula'] == str(matricula):
                print('\nDados: \n')
                for key in cada_aluno:
                    print(f'{key.title()} -> {cada_aluno[key]}')
                print('\n')
                escolha = input('Esse é o aluno que você deseja alterar as faltas? S ou N: ').upper()
                if escolha == 'S':
                    falta = int(input('Qual a quantidade de faltas que o aluno tem? -> '))
                    novo_dicicionario_admin = {
                        'matricula':matricula,
                        'nota1':cada_aluno['nota1'],
                        'nota2':cada_aluno['nota2'],
                        'nota3':cada_aluno['nota3'],
                        'faltas': falta
                    }
                    nova_lista_de_alunos = [x for x in lista_admin if x['matricula'] != str(matricula)]
                    nova_lista_de_alunos.append(novo_dicicionario_admin)

                    sobrescrever_arquivo_admin()

                    for cada_aluno in nova_lista_de_alunos:
                        conteudo = f"{cada_aluno['matricula']} ; {cada_aluno['nota1']} ; {cada_aluno['nota2']} ; {cada_aluno['nota3']} ; {cada_aluno['faltas']} ; \n"
                        adicionar_arquivo_admin(conteudo)
                    
                    print('Concluido!')
                    return nova_lista_de_alunos
                else:
                    print('Ok, voltando ao menu!')
        else:
            return lista_admin
    else:
        print('\nMatricula nao encontrada!')

def mostrar_situacao():

    min_media = 7
    max_faltas = 6

    adicionar_na_lista_admin()

    print('\n' + 12*'   ' + 'LISTA DE ALUNOS MATRICULADOS NO CURSO '+ '\n'+ 113*'_'+ '\n')
    print('{:15s} | {:10s} | {:5s} | {:5s} | {:5s} | {:3s} | {:5s} | {:3s}\n'.format('Primeiro Nome','Matricula','Nota1','Nota2','Nota3','Faltas','Media','Situacao') + 113 *'_' + '\n')
    #para cada dicionario da lista, printe as seguintes informações deles:
    for cada_aluno in lista_de_alunos:
        for cada_aluno_admin in lista_admin:
            if cada_aluno['matricula'] == cada_aluno_admin['matricula']:
                media = ((int(cada_aluno_admin['nota1']) + int(cada_aluno_admin['nota2']) + int(cada_aluno_admin['nota3'])) / 3)
                if media >= min_media and int(cada_aluno_admin['faltas']) <= max_faltas:
                    print("{:15} | {:10} | {:5} | {:5} | {:5} | {:5}  | {:.2f}  | {:3} ".format(cada_aluno['primeiro_nome'],cada_aluno['matricula'],cada_aluno_admin['nota1'],cada_aluno_admin['nota2'],cada_aluno_admin['nota3'],cada_aluno_admin['faltas'],media,'APROVADO'))
                else:
                    print("{:15} | {:10} | {:5} | {:5} | {:5} | {:5}  | {:.2f}  | {:3} ".format(cada_aluno['primeiro_nome'],cada_aluno['matricula'],cada_aluno_admin['nota1'],cada_aluno_admin['nota2'],cada_aluno_admin['nota3'],cada_aluno_admin['faltas'],media,'RECUPERACAO'))
                
def menuPrincipal():
    while True:
        adicionar_na_lista_alunos()

        print('''\nPython para Ciencia de Dados\n''')
        opcao = input("""Escolha uma opcao 
        
1 - Cadastrar Aluno✅ 
2 - Listar cadastrados👀 
3 - Remover aluno❌ 
4 - Admin acess🔁
0 - Sair🏃💭

--> """)

        if opcao == '1':
            cadastrar_aluno()
            input('\nAperte ENTER para retornar ao menu!')
            clear_terminal()
        elif opcao == '2':
            relatorio_de_alunos()
            input('\nAperte ENTER para retornar ao menu!')
            clear_terminal()
        elif opcao == '0':   
            print('Obrigado por usar nosso programa!👋')
            quit()
        elif opcao == '3':
            remover_aluno()
            input('\nAperte ENTER para retornar ao menu!')
            clear_terminal()
        elif opcao == '4':
            login = input('\nlogin: ' )
            senha = input('senha: ' )
            if login == 'admin' and senha == 'admin':
                admin_acess()
            else:
                input('\nAperte ENTER para retornar ao menu!')
                clear_terminal()
        else:
            clear_terminal()

def clear_terminal():
    os.system('cls')

def admin_acess():
    while True:
        adicionar_na_lista_alunos()

        print('''\nPython para Ciencia de Dados\n''')
        opcao = input("""Escolha uma opcao 
        
1 - Atualizar - Notas 💵 
2 - Atualizar - Faltas ⭕
3 - Mostrar   - Relatorio! 🔁
0 - Sair 🏃💭

--> """)

        if opcao == '1':
            lista_admin = atualizar_notas()
            input('\nAperte ENTER para retornar ao menu!')
            clear_terminal()
        elif opcao == '2':
            atualizar_faltas()
            input('\nAperte ENTER para retornar ao menu!')
            clear_terminal()
        elif opcao == '0':   
            print('Obrigado por usar nosso programa!👋')
            quit()
        elif opcao == '3':
            mostrar_situacao()
            input('\nAperte ENTER para retornar ao menu!')
            clear_terminal()
        else:
            clear_terminal()

menuPrincipal() 
