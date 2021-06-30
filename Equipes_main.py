import random
import Equipes_funcoes

listaEstudantes = []
listaDados = []
primeiro_ano = 0
terceiroA = 0
terceiroB = 0
terceiroC = 0
terceiroD = 0
contador = 0

#cadastrar estudantes
funcoes.cadastrarEstudantes(contador, listaDados, primeiro_ano, listaEstudantes)

#misturar lista
random.shuffle(listaEstudantes)

#informações equipes
funcoes.listarEquipes(listaEstudantes)
funcoes.calcularMedia(listaEstudantes)
funcoes.calcularEstudantes3(listaEstudantes, terceiroA, terceiroB, terceiroC, terceiroD)

#percentual alunos primeiro ano
funcoes.calcularPercentual1(primeiro_ano)
