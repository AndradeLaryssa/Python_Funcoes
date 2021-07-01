import random
import Lotofacil_funcoes

tupla = (15,16,17,18)
tupla2 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
listaNumeros = []

#cadastrar dezenas
funcoes.cadastrarDezenas(tupla, tupla2, listaNumeros)

#gerar surpresinhas e resultado
surpresinha1 = random.sample(range(1,25),18)
surpresinha2 = random.sample(range(1,25),18)
resultado = random.sample(range(1,25),15)

#mostrar os resultados 
funcoes.mostrarResultado(listaNumeros, surpresinha1, surpresinha2, resultado)
