import Rali_funcoes

#numero do carro, nome do piloto, tempo em segundos, número de punições
listaNumeros = []
listaNomes = []
listaTempos_competicao = [] 
listaTempos_provas = []
contador = 1

#cadastrar pilotos
funcoes.cadastrarPiloto(listaNumeros, listaNomes, listaTempos_provas, listaTempos_competicao)

#quantidade de carros participantes
funcoes.calcularCarros(listaNumeros)

#listar vencedores
funcoes.listarVencedores(listaTempos_competicao, contador, listaNumeros, listaNomes)
