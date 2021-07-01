def cadastrarCompras(clientes, mulheres, listaHomens, listaQuantidades, listaProdutos):
    while (True):
        codigo = input('Digite aqui o código do cliente: ')
        nome = input('Digite aqui o nome do cliente: ')
        sexo = input('Digite aqui o sexo do cliente[M/F]: ')
        clientes += 1
        if sexo in 'Ff':
            mulheres += 1
        else:
            listaHomens.append(nome)
        while (True):
            produtos = []
            valor = float(input('Digite aqui o valor do produto: '))
            quantidade = int(input('Digite aqui a quantidade do produto: '))
            listaQuantidades.append(quantidade)
            produto = valor * quantidade
            if sexo in 'Mm':
                produtos.append(produto)
            continuar = input('Deseja adicionar mais produtos?[S/N] ')
            if continuar in 'Nn':
                listaProdutos.append(sum(produtos))
                produtos.clear()
                break
        cont = input('Deseja adicionar outro cliente?[S/N] ')
        if cont in 'Nn':
            break

def calcularVendas(listaQuantidades):
    print(f'A quantidade de produtos vendidos no dia foi de {sum(listaQuantidades)}')

def calcularMedia(listaQuantidades):
    print(f'A média da quantidade de produtos em cada compra foi de {sum(listaQuantidades)/len(listaQuantidades)}')

def calcularMenorcompra(listaProdutos, listaHomens):
    menor = min(listaProdutos)
    auxiliar = listaProdutos.index(menor)
    homem = listaHomens[auxiliar]
    print(f'O homem com o menor valor de compra foi {homem}')

def calcularPercentual(mulheres, clientes):
    print(f'O percentual de mulheres que fez compras no dia foi de {(mulheres/clientes)*100}%')
