import Habitantes_funcoes

listaNomes = []
listaSalarios = []
listaSexos = []
listaIdades = []
listaHabitantes = []
mulheres = 0
contador = 0

#cadastrar habitantes
while (True):
    funcoes.cadastrarHabitantes(listaNomes, listaSalarios, listaSexos, mulheres, listaIdades, listaHabitantes)
    continuar = input('Deseja adicionar outro responsável[S/N]? ')
    if continuar in 'Nn':
        break

#listar habitantes com sálario maior que 1500
funcoes.listarHabitantes1500(listaSalarios, contador, listaNomes, listaSexos, listaIdades, listaHabitantes)
#calcular média do salário
funcoes.calcularMediasalario(listaSalarios)
#calcular percentual de mulheres
funcoes.calcularPercentual(mulheres, listaNomes)
#calcular o maior salário
funcoes.calcularMaiorsalario(listaSalarios, listaNomes)
