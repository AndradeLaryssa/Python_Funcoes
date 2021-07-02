def cadastrarVoto(listaWindows, listaLinux, listaMac, listaOutro, listaVotos, tupla):
    while(True):
        nome = input('Digite seu nome: ')
        print('Qual o melhor Sistema Operacional?'
            '\n1 - Windows'
            '\n2 - Linux'
            '\n3 - Mac'
            '\n4 - Outro')
        print('\nPara interromper a leitura, informe o voto 0')
        voto = int(input('Digite seu voto [0 a 4]: '))
        if voto == 0:
            break
        if voto == 1:
            listaWindows.append(voto)
        if voto == 2:
            listaLinux.append(voto)
        if voto == 3:
            listaMac.append(voto)
        if voto == 4:
            listaOutro.append(voto)
        elif voto not in tupla:
            print('Digite apenas números dentro do intervalo [0 a 4]')
        else:
            listaVotos.append(voto)

def calcularVotos(listaVotos, listaWindows, listaLinux, listaMac, listaOutro):
    print(f'O total de votos computados foi de {len(listaVotos)}')
    print(f'Windows = {len(listaWindows)} votos '
        f'\nLinux = {len(listaLinux)} votos '
        f'\nMac = {len(listaMac)} votos '
        f'\nOutro = {len(listaOutro)} votos')
    print(f'Windows = {len(listaWindows)/len(listaVotos)}% votos '
        f'\nLinux = {len(listaLinux)/len(listaVotos)}% votos '
        f'\nMac = {len(listaMac)/len(listaVotos)}% votos '
        f'\nOutro = {len(listaOutro)/len(listaVotos)}% votos')

def calcularMaisvotado(listaWindows, listaLinux, listaMac, listaOutro):
    if len(listaWindows) > len(listaLinux) and len(listaWindows) > len(listaMac) and len(listaWindows) > len(listaOutro):
        print('O sistema mais votado foi o Windows')
    if len(listaLinux) > len(listaWindows) and len(listaLinux) > len(listaMac) and len(listaLinux) > len(listaOutro):
        print('O sistema mais votado foi o Linux')
    if len(listaMac) > len(listaWindows) and len(listaMac) > len(listaLinux) and len(listaMac) > len(listaOutro):
        print('O sistema mais votado foi o Mac')
    if len(listaOutro) > len(listaWindows) and len(listaOutro) > len(listaLinux) and len(listaOutro) > len(listaMac):
        print('O sistema mais votado foi Outro')
