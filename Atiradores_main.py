import Atiradores_funcoes

listaAtiradores = []
listaNomes = []
listaDistancias = []
listaSexos = []
listaAcertos_M = []
listaDistancias_F = []

# quantidade de participantes, nome, sexo, distância
quantidade = int(input('Digite aqui a quantidade de participantes: '))

while quantidade > 0:
    funcoes.cadastrarAtiradores(listaNomes,listaSexos,listaDistancias,listaAtiradores, listaDistancias_F, listaAcertos_M)
    quantidade -= 1

# melhor atirador/pior atirador
funcoes.melhorAtirador(listaDistancias,listaNomes,listaSexos)
funcoes.piorAtirador(listaDistancias,listaNomes,listaSexos)


funcoes.quantidadeAtiradoreselite(listaAtiradores,listaNomes)
funcoes.acertosMasculino(listaAcertos_M)
funcoes.distanciaFeminina(listaDistancias_F)
