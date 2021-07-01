import Prova_funcoes

tupla = ('A', 'B', 'C', 'D', 'E', 'a', 'b', 'c', 'd', 'e')
listaGabarito = []
listaRespostas_alunos = []
listaNotas = []
listaNomes = []
listaMatriculas = []
contador = 0
cont = 0
contad = 0
maiores_notas = 0

#cadastrar gabarito do professor
funcoes.cadastrarGabaritoprofessor(contador, tupla, listaGabarito)

#quantidade de alunos
alunos = int(input('Qual a quantidade de alunos que realizaram a prova? '))

#cadastrar respostas dos alunos
funcoes.cadastrarGabaritoalunos(cont, alunos, listaMatriculas, listaNomes, listaRespostas_alunos, listaGabarito, listaNotas)

#calcular notas dos alunos
funcoes.calcularNotas(listaGabarito, listaNotas, listaNomes, listaMatriculas)

#calcular as maiores notas
funcoes.calcularMaiornota(listaNotas, listaNomes)

#calcular a média dos alunos
funcoes.calcularMedia(listaNotas, alunos)

#calcular o percentual de alunos acima da média
funcoes.calcularPercentualnotas(listaNotas, contad, media, maiores_notas, alunos)
