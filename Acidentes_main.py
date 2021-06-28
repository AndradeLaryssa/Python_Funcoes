import Acidentes_funcoes

listaAcidentes = []
listaAcidentes_2000 = []
listaAcidentes_1000 = []
listaCidades = []
listaCarros = []
listaMotocicletas = []

#cadastrar cidades
while(True):
  funcoes.cadastrarCidade(listaCidades,listaCarros,listaMotocicletas,listaAcidentes,listaAcidentes_2000,listaAcidentes_1000)
  continuar = input('Deseja adicionar outra cidade?[S/N] ' )
  if continuar in 'Nn':
    break

#maior e menor índice de acidentes e a cidade que pertence
funcoes.calcularIndices(listaAcidentes,listaCidades)

#media de carros nas cidades
funcoes.calcularMediacarros(listaCarros,listaCidades)

#media de motocicletas nas cidades
funcoes.calcularMediamotos(listaMotocicletas,listaCidades)

#media de acidentes em cidades nas cidades com mais de 2000 carros
funcoes.calcularMedia2000carros(listaAcidentes_2000)

#media de acidentes em cidades nas cidades com mais de 1000 motos
funcoes.calcularMedia1000carros(listaAcidentes_1000)
