def cadastrarAtiradores(listaNomes, listaSexos, listaDistancias, listaAtiradores, listaDistancias_F, listaAcertos_M):
    nome = input('Digite aqui o nome do policial: ')
    listaNomes.append(nome)

    sexo = input('Digite aqui o sexo do policial[M/F]: ')
    listaSexos.append(sexo)

    distancia = float(input('Digite aqui a distância(em centímetros) em relação ao alvo: '))
    listaDistancias.append(distancia)

    if distancia < 1:
        listaAtiradores.append(distancia)

    if sexo in 'Ff':
        listaDistancias_F.append(distancia)

    if sexo in 'Mm':
        if distancia == 0:
            listaAcertos_M.append(distancia)


def melhorAtirador(listaDistancias, listaNomes, listaSexos):
    melhor = min(listaDistancias)
    auxiliar_1 = listaDistancias.index(melhor)
    policial_1 = listaNomes[auxiliar_1]
    sexo_1 = listaSexos[auxiliar_1]

    print(f'O melhor atirador foi {policial_1}, do sexo {sexo_1}, com a distância de {melhor} em relação ao alvo')


def piorAtirador(listaDistancias, listaNomes, listaSexos):
    pior = max(listaDistancias)
    auxiliar_2 = listaDistancias.index(pior)
    policial_2 = listaNomes[auxiliar_2]
    sexo_2 = listaSexos[auxiliar_2]

    print(f'O pior atirador foi {policial_2}, do sexo {sexo_2}, com a distância de {pior} em relação ao alvo')


def quantidadeAtiradoreselite(listaAtiradores, listaNomes):
    print(
        f'O percentual de policiais que alcançaram o título de atiradores de elite foi de {(len(listaAtiradores) / len(listaNomes)) * 100 :.2f}%')


def acertosMasculino(listaAcertos_M):
    print(f'A quantidade de homens que acertou o alvo foi de {len(listaAcertos_M)}')


def distanciaFeminina(listaDistancias_F):
    if len(listaDistancias_F) != 0:
        print(
            f'A média da distância ao alvo obtida pelas atiradoras foi de {sum(listaDistancias_F) / len(listaDistancias_F)}')
