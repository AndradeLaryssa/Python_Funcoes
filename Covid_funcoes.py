def cadastrarCidade(listaCidades, listaPositivos, listaObitos):
    while (True):
      print('\nPara interroper a leitura digite o código como -1')
      codigo = int(input('\nDigite o código do estado: '))
      if codigo == -1:
        break
      nome = input('Digite o nome do estado: ')
      listaCidades.append(nome)
      positivo = int(input('Digite a quantidade de pacientes do estado que testaram positivo: '))
      listaPositivos.append(positivo)
      mortes = int(input('Digite a quantidade de mortos decorrentes do COVID no estado: '))
      listaObitos.append(mortes)

def calcularMedia(listaObitos):
  print(f'A média de obitos nos estados cadastrados foi de {sum(listaObitos)/len(listaObitos)}')

def calcularMaior(listaPositivos, listaCidades):
  maior = max(listaPositivos)
  auxiliar = listaPositivos.index(maior)
  nomes = listaCidades[auxiliar]
  print(f'O cidade cadastrada com o maior número de óbitos foi {nomes}')

def calcularPercentual(listaObitos):
  print(f'O percentual de óbitos da primeira cidade cadastrada foi de {(listaObitos[0]/sum(listaObitos)*100)}%')

