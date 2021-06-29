import Covid_funcoes

listaObitos = []
listaPositivos = []
listaCidades = []

#cadastrar cidades
funcoes.cadastrarCidade(listaCidades,listaPositivos,listaObitos)
#calcular média de óbitos
funcoes.calcularMedia(listaObitos)
#calcular cidade com o maior número de óbitos
funcoes.calcularMaior(listaPositivos,listaCidades)
#calcular percentual de óbitos
funcoes.calcularPercentual(listaObitos)
