def cadastrarCidade(listaCidades, listaCarros, listaMotocicletas, listaAcidentes, listaAcidentes_2000,
                    listaAcidentes_1000):
    cidade = input('Digite aqui o nome da cidade: ')
    listaCidades.append(cidade)

    carro = int(input('Digite aqui o número de carros de passeios da cidade: '))
    listaCarros.append(carro)

    motocicleta = int(input('Digite aqui o número de motocicletas da cidade: '))
    listaMotocicletas.append(motocicleta)

    acidente = int(input('Digite aqui o número de acidentes de trânsito em 2018: '))
    listaAcidentes.append(acidente)

    if carro >= 2000:
        listaAcidentes_2000.append(acidente)
    if motocicleta >= 1000:
        listaAcidentes_1000.append(acidente)


def calcularIndices(listaAcidentes, listaCidades):
    lista_ordenada = sorted(listaAcidentes)
    contador = 1

    for chave, valor in enumerate(lista_ordenada):
        print(f'A cidade {listaCidades[chave]} ficou no {contador}º lugar na lista de maior índice de acidentes')
        contador += 1


def calcularMediacarros(listaCarros, listaCidades):
    media_carros = sum(listaCarros) / len(listaCidades)
    print(f'A média de carros nas cidades foi de {media_carros}')


def calcularMediamotos(listaMotocicletas, listaCidades):
    media_motos = sum(listaMotocicletas) / len(listaCidades)
    print(f'A média de motocicletas nas cidades foi de {media_motos}')


def calcularMedia2000carros(listaAcidentes_2000):
    print(
        f'A média de acidentes nas cidades com mais de 2000 carros foi de {sum(listaAcidentes_2000) / len(listaAcidentes_2000)}')


def calcularMedia1000carros(listaAcidentes_1000):
    print(
        f'A média de acidentes nas cidades com mais de 1000 motos foi de {sum(listaAcidentes_1000) / len(listaAcidentes_1000)}')

