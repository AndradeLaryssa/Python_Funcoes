def cadastrarEstudantes(contador, listaDados, primeiro_ano, listaEstudantes):
    while contador < 12:
        nome = input(f'Digite o nome do {contador+1}º estudante: ')
        listaDados.append(nome)
        idade = int(input(f'Digite a idade do {contador+1}º estudante: '))
        listaDados.append(idade)
        ano = int(input('Digite o ano que o mesmo está cursando [1 a 3]: '))
        if ano == 1:
            primeiro_ano += 1
        listaDados.append(ano)
        listaEstudantes.append(listaDados[:])
        listaDados.clear()
        contador += 1

def listarEquipes(listaEstudantes):
    for i in range(len(listaEstudantes)):
        if (i == 0 or i == 1 or i == 2):  # Equipe A
            print(f'Equipe A - Nome: {listaEstudantes[i][0]} Idade: {listaEstudantes[i][1]} Ano: {listaEstudantes[i][2]}')
        if (i == 3 or i == 4 or i == 5):  # Equipe B
            print(f'Equipe B - Nome: {listaEstudantes[i][0]} Idade: {listaEstudantes[i][1]} Ano: {listaEstudantes[i][2]}')
        if (i == 6 or i == 7 or i == 8):  # Equipe C
            print(f'Equipe C - Nome: {listaEstudantes[i][0]} Idade: {listaEstudantes[i][1]} Ano: {listaEstudantes[i][2]}')
        if (i == 9 or i == 10 or i == 11):  # Equipe D
            print(f'Equipe D - Nome: {listaEstudantes[i][0]} Idade: {listaEstudantes[i][1]} Ano: {listaEstudantes[i][2]}')

def calcularMedia(listaEstudantes):
    for i in range(len(listaEstudantes)):
        if (i == 0 or i == 1 or i == 2): # Equipe A
            mediaA = (listaEstudantes[i][1] + listaEstudantes[i][1] + listaEstudantes[i][1]) / 3
            print(f'Média de idade entre os estudantes da Equipe A: {mediaA :.2f}')
        if (i == 3 or i == 4 or i == 5):  # Equipe B
            mediaB = (listaEstudantes[i][1] + listaEstudantes[i][1] + listaEstudantes[i][1]) / 3
            print(f'Média de idade entre os estudantes da Equipe B: {mediaB :.2f}')
        if (i == 6 or i == 7 or i == 8):  # Equipe C
            mediaC = (listaEstudantes[i][1] + listaEstudantes[i][1] + listaEstudantes[i][1]) / 3
            print(f'Média de idade entre os estudantes da Equipe C: {mediaC :.2f}')
        if (i == 9 or i == 10 or i == 11):  # Equipe D
            mediaD = (listaEstudantes[i][1] + listaEstudantes[i][1] + listaEstudantes[i][1]) / 3
            print(f'Média de idade entre os estudantes da Equipe D: {mediaD :.2f}')

def calcularEstudantes3(listaEstudantes, terceiroA, terceiroB, terceiroC, terceiroD):
    for i in range(len(listaEstudantes)):
        if (i == 0 or i == 1 or i == 2):
             if listaEstudantes[i][2] == 3:
                terceiroA += 1
                print(f'Quantidade de estudantes do 3º ano na Equipe A: {terceiroA}')
        if (i == 3 or i == 4 or i == 5):
            if listaEstudantes[i][2] == 3:
                terceiroB += 1
                print(f'Quantidade de estudantes do 3º ano na Equipe A: {terceiroB}')
        if (i == 0 or i == 1 or i == 2):
            if listaEstudantes[i][2] == 3:
                terceiroC += 1
                print(f'Quantidade de estudantes do 3º ano na Equipe A: {terceiroC}')
        if (i == 0 or i == 1 or i == 2):
            if listaEstudantes[i][2] == 3:
                terceiroD += 1
                print(f'Quantidade de estudantes do 3º ano na Equipe A: {terceiroD}')

def calcularPercentual1(primeiro_ano):
    print(f'Percentual de alunos do Primeiro Ano: {(primeiro_ano / 12) * 100 :.2f}%')
