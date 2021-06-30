def cadastrarHabitantes(listaNomes, listaSalarios, listaSexos, mulheres, listaIdades, listaHabitantes):
    nome = input('Digite o nome do habitante responsável: ')
    listaNomes.append(nome)
    salario = int(input('Digite o sálario do responsável: '))
    listaSalarios.append(salario)
    sexo = input('Digite o sexo do responsável[M/F]: ')
    listaSexos.append(sexo)
    if sexo in 'Ff':
        mulheres += 1
    idade = int(input('Digite a idade do reponsável: '))
    listaIdades.append(idade)
    habitantes = int(input('Digite o número de habitantes no lar: '))
    listaHabitantes.append(habitantes)

def listarHabitantes1500(listaSalarios, contador, listaNomes, listaSexos, listaIdades, listaHabitantes):
    if listaSalarios[contador] > 1500:
        print(f'Nome: {listaNomes[contador]}'
              f'\nSalário: {listaSalarios[contador]} reais'
              f'\nSexo: {listaSexos[contador]}'
              f'\nIdade: {listaIdades[contador]} anos'
              f'\nHabitantes no lar: {listaHabitantes[contador]}')

        contador += 1

def calcularMediasalario(listaSalarios):
    print(f'A média de salário nas residências foi de {sum(listaSalarios) / len(listaSalarios)}')

def calcularPercentual(mulheres, listaNomes):
    print(f'O percentual de mulheres que são responsáveis pelos seus lares foi de {(mulheres / len(listaNomes)) * 100 :.2f}%')

def calcularMaiorsalario(listaSalarios, listaNomes):
    maior = max(listaSalarios)
    auxiliar = listaSalarios.index(maior)
    responsavel = listaNomes[auxiliar]
    print(f'O(s) responsável(s) {responsavel} obtiveram o maior salário da pesquisa: {maior} reais')
