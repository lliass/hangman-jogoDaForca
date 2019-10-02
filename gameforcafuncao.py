import random


def troca_letra(palavraaux, indice, letra):
    m1 = palavraaux[:indice] + letra + palavraaux[indice+1:]
    return m1


def forca(erros):
    f1 = '    ________'
    f2 = '   |        |'
    f3 = '   |'
    f4 = '   |'
    f5 = '   |'
    f6 = '   |'
    f7 = '   |'
    f8 = '__/|\__'
    if erros >= 1:
        f3 = '   |        o'
    if erros == 2:
        f4 = '   |        |'
    if erros == 3:
        f4 = '   |       /|'
    if erros >= 4:
        f4 = '   |       /|\ '
    if erros >= 5:
        f5 = '   |        |'
    if erros == 6:
        f6 = '   |       /'
    if erros == 7:
        f6 = '   |       / \ '
    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7)
    print(f8)


def palavras_erradas(erros, letraerrada, palv, palvoct):

    print('A palavra é:', palvoct)

    if erros >= 1:
        print('Letras erradas:', letraerrada)

    if erros == 7:
        print('A palavra era: ', palv)


def jogo_completo_forca():
    while True:
        aux_final = False
        cont_erro = 0
        aux1 = ''
        word_aux = ''
        leterro1 = ''
        aj = 1
        flag_palv = False
        flag_win = True
        qntdlet = 0
        qntd_acr = 0
        contlet = 0
        listalet = ['PORTA', 'DEAD-POOL', 'HULK', 'HOMEM-ARANHA', 'MORANGO', 'JUMENTO', 'CARRO', 'VIUVA-NEGRA', 'HOMEM-DE-FERRO', 'MACACO']
        word = random.choice(listalet)
        while cont_erro <= 7 and flag_win:

            forca(cont_erro)
            if aj == 1:
                for x in range(len(word)):
                    word_aux += word[x]+' '
                    aux1 += '_ '
                    qntdlet += 1
                aj += 1

            palavras_erradas(cont_erro, leterro1, word, aux1)

            if qntd_acr == qntdlet:
                print('Parabéns você acertou a palavra.')
                flag_win = False

            if cont_erro <= 6 and flag_win:
                flag_letra = False
                while not flag_letra:
                    let = input('Digite uma letra:').upper()
                    if let in aux1 or let in leterro1:
                        print('Letra repetida.')
                    else:
                        flag_letra = True
            flag_palv = False

            for i in range(len(word_aux)):
                if let == word_aux[i]:
                    aux1 = troca_letra(aux1, i, let)
                    flag_palv = True
            contlet = word.count(let)
            if flag_palv and contlet == 1:
                qntd_acr += 1
            else:
                qntd_acr += contlet
            if flag_palv == aux_final:
                leterro1 += let+' '
                cont_erro += 1


jogo_completo_forca()
