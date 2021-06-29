import random
import funcoes

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

#informações equipe A
funcoes.listarEquipeA(listaEstudantes)
funcoes.calcularMediaA(listaEstudantes)
funcoes.calcularEstudantes3A(listaEstudantes, terceiroA)

#informações equipe B
funcoes.listarEquipeB(listaEstudantes)
funcoes.calcularMediaB(listaEstudantes)
funcoes.calcularEstudantes3B(listaEstudantes, terceiroB)

#informações equipe C
funcoes.listarEquipeC(listaEstudantes)
funcoes.calcularMediaC(listaEstudantes)
funcoes.calcularEstudantes3C(listaEstudantes, terceiroC)

#informações equipe D
funcoes.listarEquipeD(listaEstudantes)
funcoes.calcularMediaD(listaEstudantes)
funcoes.calcularEstudantes3D(listaEstudantes, terceiroD)

#percentual alunos primeiro ano
funcoes.calcularPercentual1(primeiro_ano)

