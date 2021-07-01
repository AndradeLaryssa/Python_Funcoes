import Mercado_funcoes

clientes = 0
listaQuantidades = []
listaHomens = []
mulheres = 0
listaProdutos = []

#cadastrar clientes e produtos
funcoes.cadastrarCompras(clientes, mulheres, listaHomens, listaQuantidades, listaProdutos)

#calcular a quantidade de produtos vendidos
funcoes.calcularVendas(listaQuantidades)

#calcular a média de quantidade de produtos
funcoes.calcularMedia(listaQuantidades)

#calcular o homem com a menor compra
funcoes.calcularMenorcompra(listaProdutos, listaHomens)

#calcular o percentual de mulheres entre os clientes 
funcoes.calcularPercentual(mulheres, clientes)
