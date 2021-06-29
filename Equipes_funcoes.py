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

def listarEquipeA(listaEstudantes):
    print(f'Equipe A: Nome:{listaEstudantes[0][0]}, Idade: {listaEstudantes[0][1]}, Ano:{listaEstudantes[0][2]}'
          f'\nNome:{listaEstudantes[1][0]}, Idade: {listaEstudantes[1][1]}, Ano:{listaEstudantes[1][2]}'
          f'\nNome:{listaEstudantes[2][0]}, Idade: {listaEstudantes[2][1]}, Ano:{listaEstudantes[2][2]}')

def calcularMediaA(listaEstudantes):
    mediaA = (listaEstudantes[0][1] + listaEstudantes[1][1] + listaEstudantes[2][1]) / 3
    print(f'Média de idade entre os estudantes da Equipe A: {mediaA :.2f}')

def calcularEstudantes3A(listaEstudantes, terceiroA):
    if listaEstudantes[0][2] == 3:
        terceiroA += 1
    if listaEstudantes[1][2] == 3:
        terceiroA += 1
    if listaEstudantes[2][2] == 3:
        terceiroA += 1
    print(f'Quantidade de estudantes do 3º ano na Equipe A: {terceiroA}')

def listarEquipeB(listaEstudantes):
    print(f'Equipe B: Nome:{listaEstudantes[3][0]}, Idade: {listaEstudantes[3][1]}, Ano:{listaEstudantes[3][2]}'
          f'\nNome:{listaEstudantes[4][0]}, Idade: {listaEstudantes[4][1]}, Ano:{listaEstudantes[4][2]}'
          f'\nNome:{listaEstudantes[5][0]}, Idade: {listaEstudantes[5][1]}, Ano:{listaEstudantes[5][2]}')

def calcularMediaB(listaEstudantes):
    mediaB = (listaEstudantes[3][1] + listaEstudantes[4][1] + listaEstudantes[5][1]) / 3
    print(f'Média de idade entre os estudantes da Equipe B: {mediaB :.2f}')

def calcularEstudantes3B(listaEstudantes, terceiroB):
    if listaEstudantes[3][2] == 3:
        terceiroB += 1
    if listaEstudantes[4][2] == 3:
        terceiroB += 1
    if listaEstudantes[5][2] == 3:
        terceiroB += 1
    print(f'Quantidade de estudantes do 3º ano na Equipe B: {terceiroB}')

def listarEquipeC(listaEstudantes):
    print(f'Equipe C: Nome:{listaEstudantes[6][0]}, Idade: {listaEstudantes[6][1]}, Ano:{listaEstudantes[6][2]}'
          f'\nNome:{listaEstudantes[7][0]}, Idade: {listaEstudantes[7][1]}, Ano:{listaEstudantes[7][2]}'
          f'\nNome:{listaEstudantes[8][0]}, Idade: {listaEstudantes[8][1]}, Ano:{listaEstudantes[8][2]}')

def calcularMediaC(listaEstudantes):
    mediaC = (listaEstudantes[6][1] + listaEstudantes[7][1] + listaEstudantes[8][1]) / 3
    print(f'Média de idade entre os estudantes da Equipe C: {mediaC :.2f}')

def calcularEstudantes3C(listaEstudantes, terceiroC):
    if listaEstudantes[6][2] == 3:
        terceiroC += 1
    if listaEstudantes[7][2] == 3:
        terceiroC += 1
    if listaEstudantes[8][2] == 3:
        terceiroC += 1
    print(f'Quantidade de estudantes do 3º ano na Equipe C: {terceiroC}')

def listarEquipeD(listaEstudantes):
    print(f'Equipe D: Nome:{listaEstudantes[9][0]}, Idade: {listaEstudantes[9][1]}, Ano:{listaEstudantes[9][2]}'
          f'\nNome:{listaEstudantes[10][0]}, Idade: {listaEstudantes[10][1]}, Ano:{listaEstudantes[10][2]}'
          f'\nNome:{listaEstudantes[11][0]}, Idade: {listaEstudantes[11][1]}, Ano:{listaEstudantes[11][2]}')

def calcularMediaD(listaEstudantes):
    mediaD = (listaEstudantes[9][1] + listaEstudantes[10][1] + listaEstudantes[11][1]) / 3
    print(f'Média de idade entre os estudantes da Equipe D: {mediaD :.2f}')

def calcularEstudantes3D(listaEstudantes, terceiroD):
    if listaEstudantes[9][2] == 3:
        terceiroD += 1
    if listaEstudantes[10][2] == 3:
        terceiroD += 1
    if listaEstudantes[11][2] == 3:
        terceiroD += 1
    print(f'Quantidade de estudantes do 3º ano na Equipe D: {terceiroD}')

def calcularPercentual1(primeiro_ano):
    print(f'Percentual de alunos do Primeiro Ano: {(primeiro_ano / 12) * 100 :.2f}%')
