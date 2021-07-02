def cadastrarPiloto(listaNumeros, listaNomes, listaTempos_provas, listaTempos_competicao):
    while(True):
        print('Para encerar a leitura digite um número negativo')
        numero_carro = int(input('Digite aqui o número do carro: '))
    
        if numero_carro < 0:
            break
        else:
            listaNumeros.append(numero_carro)

        nome_piloto = input('Digite aqui o nome do piloto: ')
        listaNomes.append(nome_piloto)
        tempo_prova = int(input('Digite aqui o tempo em que a prova foi realizada[Em segundos]: '))
        listaTempos_provas.append(tempo_prova)
        punicoes = int(input('Digite aqui o número de punições recebidas: '))
        
        if punicoes > 0:
            #punição = adiciona 5% no tempo de prova
            tempo_punicoes = tempo_prova + (tempo_prova * punicoes * (5/100))
            listaTempos_competicao.append(tempo_punicoes)
        else:
            listaTempos_competicao.append(tempo_prova)


def calcularCarros(listaNumeros):
    print(f'Quantidade de carros participantes: {len(listaNumeros)}')

def listarVencedores(listaTempos_competicao, contador, listaNumeros, listaNomes):
    #ordenar em ordem crescente 
    lista_ordenada = sorted(listaTempos_competicao)
    for chave, valor in enumerate(lista_ordenada):
        print(f'O {contador}ºLUGAR foi do CARRO {listaNumeros[chave]}, do(a) PILOTO {listaNomes[chave]}, com o TEMPO de {listaTempos_competicao[chave]}s')
        contador += 1
