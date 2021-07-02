import Sistemas_funcoes

tupla = (0,1,2,3,4)
listaVotos = []
listaWindows = []
listaLinux = []
listaMac = []
listaOutro = []

#cadastro do votos
funcoes.cadastrarVoto(listaWindows, listaLinux, listaMac, listaOutro, listaVotos, tupla)
#calcular votos 
funcoes.calcularVotos(listaVotos, listaWindows, listaLinux, listaMac, listaOutro)
#calcular o sistema mais votado
funcoes.calcularMaisvotado(listaWindows, listaLinux, listaMac, listaOutro)
