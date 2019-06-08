import random
def troca_letra(palavraAux,indice, letra):
    m1 = palavraAux[:indice] + letra + palavraAux[indice+1:]
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


def palavras_erradas(erros,letraerrada,palv,palvoct):

    print('A palavra é:',palvoct)

    if erros >= 1:
        print('Letras erradas:',letraerrada)

    if erros == 7:
        print('A palavra era: ',palv)

def jogo_completo_forca():
    while True:
        contErro = 0  
        aux1 = ''      
        wordAux = ''
        leterro1 = ''  
        aj = 1        
        flagPalv = False  
        flagWin = True
        
        qntdlet = 0
        qntdAcr = 0
        contlet = 0
        listalet = ['PORTA','DEAD-POOL','HULK','HOMEM-ARANHA','MORANGO','JUMENTO','CARRO','VIUVA-NEGRA','HOMEM-DE-FERRO','MACACO']
        word = random.choice(listalet)
        while contErro<=7 and flagWin:             

            forca(contErro)
            
            if aj == 1:
                for x in range(len(word)):
                    wordAux += word[x]+' '
                    aux1 +='_ '
                    qntdlet +=1 
                aj+=1

            palavras_erradas(contErro,leterro1,word,aux1)

            if qntdAcr==qntdlet: 
                print('Parabéns você acertou a palavra.')
                flagWin = False

            if contErro <=6 and flagWin: 
                flag_letra = False
                while not flag_letra:
                    let = input('Digite uma letra:').upper()
                    if let in aux1 or let in leterro1:
                        print('Letra repetida.')
                    else:
                        flag_letra = True
                
            flagPalv = False

            for i in range(len(wordAux)): 
                if let == wordAux[i]:
                    aux1 = troca_letra(aux1, i, let)
                    flagPalv = True 
            contlet = word.count(let)
            if flagPalv==True and contlet == 1:
                qntdAcr=qntdAcr+1
            else:
                qntdAcr=qntdAcr+contlet
                
            if flagPalv == False:
                leterro1 += let+' '
                contErro+=1

jogo_completo_forca()

