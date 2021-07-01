def cadastrarGabaritoprofessor(contador, tupla, listaGabarito):
    while contador < 6:
        questoes = input(f'Digite o gabarito da {contador + 1}º questão: ')
        questoes.upper()
        #roda novamente quantas vezes forem necessárias
        while questoes not in tupla:
            print('Sua resposta foi inválida! Digite apenas A,B,C,D ou E')
            questoes = input(f'Digite o gabarito da {contador + 1}º questão: ')
            questoes.upper()

        listaGabarito.append(questoes)
        contador += 1

def cadastrarGabaritoalunos(cont, alunos, listaMatriculas, listaNomes, listaRespostas_alunos, listaGabarito, listaNotas):
    while cont < alunos:
        matricula = input(f'Digite a matrícula do {cont + 1}º aluno: ')
        listaMatriculas.append(matricula)
        nome = input(f'Digite o nome do {cont + 1}º aluno: ')
        listaNomes.append(nome)
        for i in range(6):
            respostas = input(f'Digite a resposta da {i + 1}º questão: ')
            respostas.upper()
            # roda novamente quantas vezes forem necessárias
            while respostas not in tupla:
                print('Sua resposta foi inválida! Digite apenas A,B,C,D ou E')
                respostas = input(f'Digite a resposta da {i + 1}º questão: ')
                respostas.upper()

            listaRespostas_alunos.append(respostas)

        nota = 0
        if listaGabarito[0] == listaRespostas_alunos[0]:
            nota += 1.5
        if listaGabarito[1] == listaRespostas_alunos[1]:
            nota += 1.5
        if listaGabarito[2] == listaRespostas_alunos[2]:
            nota += 1.5
        if listaGabarito[3] == listaRespostas_alunos[3]:
            nota += 1.5
        if listaGabarito[4] == listaRespostas_alunos[4]:
            nota += 2
        if listaGabarito[5] == listaRespostas_alunos[5]:
            nota += 2

        listaNotas.append(nota)

        nota = 0
        cont += 1

def calcularNotas(listaGabarito, listaNotas, listaNomes, listaMatriculas):
    print(f'Gabarito da prova: {listaGabarito}')
    for chave, valor in enumerate(listaNotas):
        print('\nRelátorio das Notas:'
              f'\nAluno {listaNomes[chave]}'
              f'\nMatrícula {listaMatriculas[chave]}'
              f'\nNota: {listaNotas[chave]}')

def calcularMaiornota(listaNotas, listaNomes):
    maior = max(listaNotas)
    auxiliar = listaNotas.index(maior)
    aluno = listaNomes[auxiliar]
    print(f'O(s) aluno(s) {listaNomes} obtiveram a maior nota da turma: {maior} pontos')

def calcularMedia(listaNotas, alunos):
    media = sum(listaNotas)/alunos
    print(f'A média das notas da turma foi de {media}')


def calcularPercentualnotas(listaNotas, contad, media, maiores_notas, alunos):
    if listaNotas[contad] > media:
        maiores_notas += 1
        contad += 1
    else:
        contad += 1

    print(f'O percentual de alunos que obtiveram nota acima da média foi de {(maiores_notas/alunos)*100 :.2f}%')
