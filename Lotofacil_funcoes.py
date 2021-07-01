def cadastrarDezenas(tupla, tupla2, listaNumeros):
    dezenas = int(input('Digite a quantidade de dezenas que deseja marcar na primeira aposta[15 a 18 números]: '))

    while dezenas not in tupla:
        print('Por favor, digite um número dentro do intervalo[15 a 18 números]!')
        dezenas = int(input('Digite a quantidade de dezenas que deseja marcar na primeira aposta[15 a 18 números]: '))

    for i in range(dezenas):
        numero = int(input(f'Digite o {i + 1}º número [1 a 25, sem repetição]: '))

        while numero not in tupla2:
            print('Por favor, digite um número dentro do intervalo[1 a 25]!')
            numero = int(input(f'Digite o {i + 1}º número [1 a 25]: '))
        while numero in listaNumeros:
            print('Você já escolheu esse número, por favor digite outro!')
            numero = int(input(f'Digite o {i + 1}º número [1 a 25]: '))

        listaNumeros.append(numero)

def mostrarResultado(listaNumeros, surpresinha1, surpresinha2, resultado):
    print(f'Sua aposta: {sorted(listaNumeros)}')
    print(f'Surpresinha 1: {sorted(surpresinha1)}')
    print(f'Surpresinha 2: {sorted(surpresinha2)}')
    print(f'Resultado: {sorted(resultado)}')
