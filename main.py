
'''
teste = '"icaro";"joao";537176;18;"joaoicaro@gmail.com";3;"M"'

with open('Cadastro-De-Alunos-Liceu/alunos.csv','a') as arq:
    arq.write(teste)
    arq.write('\n')

dataset = pd.read_csv('Cadastro-De-Alunos-Liceu/alunos.csv',delimiter=';')

dataset.plot.bar(color = 'gray')
alunos = dataset.groupby(['primeiro_nome']).size()
dataset.plot.bar(color='gray')
'''

lista_de_alunos = []

def abrir_arquivo():
    with open('Cadastro-De-Alunos-Liceu/alunos.txt','a') as arq:
        return arq

def ler_arquivo():
    with open('Cadastro-De-Alunos-Liceu/alunos.txt','r') as arq:
        dados = arq.readlines()
        return dados

def escrever_arquivo(item):
    with open('Cadastro-De-Alunos-Liceu/alunos.txt','a') as arq:
        arq.write(item)

def adicionar_na_lista():
    lista_de_alunos.clear()
    abrir_arquivo()
    linhas = ler_arquivo()
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

def conferir_matricula(matricula):
    #verificar se as matriculas ja existem
    for cada_aluno in lista_de_alunos:
        if str(matricula) == cada_aluno['matricula']:
            print('MATRICULA EXISTENTE! FECHANDO!')
            return False          
    return True

def cadastrar_aluno():
    matricula = int(input('Qual a sua matricula? '))
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

        escrever_arquivo(conteudo)

        print("\nALUNO CADASTRADO COM SUCESSO!!")

def relatorio_de_alunos():

    adicionar_na_lista()

    print('\n' + 12*'   ' + 'LISTA DE ALUNOS MATRICULADOS NO CURSO '+ '\n'+ 113*'_'+ '\n')
    print('{:15s} | {:20s} | {:6s} | {:5s} | {:34s} | {:3s} | {:3s}\n'.format('Primeiro Nome','Segundo Nome','Matricula','Idade','Email','Serie','Genero') + 113*'_' + '\n')
    #para cada dicionario da lista, printe as seguintes informações deles:
    for cada_aluno in lista_de_alunos:
        print("{:15} | {:20} |  {:6}   |   {:4}|  {:30}    | {:3}   | {:3}".format(cada_aluno['primeiro_nome'],cada_aluno['segundo_nome'],cada_aluno['matricula'],cada_aluno['idade'],cada_aluno['email'],cada_aluno['serie'],cada_aluno['genero']))

def menuPrincipal():
    while True:
        adicionar_na_lista()

        print('''\nPython para Ciencia de Dados\n''')
        opcao = input("""Escolha uma opcao 
        
1 - Cadastrar Aluno✅ 
2 - Listar cadastrados👀 
3 - Remover Aluno❌ 
0 - Sair🏃💭

--> """)

        if opcao == '1':
            cadastrar_aluno()
            input('\nAperte ENTER para retornar ao menu!')
        elif opcao == '2':
            relatorio_de_alunos()
            input('\nAperte ENTER para retornar ao menu!')
        elif opcao == '0':   
            print('Obrigado por usar nosso programa!👋')
            quit()
        elif opcao == '3':
            pass

menuPrincipal() 