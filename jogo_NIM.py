print('Bem-vindo ao jogo do NIM! Escolha: ')
print('')
    
def computador_escolhe_jogada(n,m):
    #x=peças q o computador vai pegar
    x=0
    x=n-(m+1)
    if n%m==1:
        x=1
        return x
    if x>0 and x<m:
        return x
    if x<0:
        return n
    if n%m==0:
        x=1
        return x        
    else:
        return m
    
def usuario_escolhe_jogada(n,m):
    y=int(input('Quantas peças você vai tirar? '))
    if y>=1 and y<=m:
        return y  
    else:
        while y<1 or y>m:
            print('')
            print('Oops! Jogada inválida! Tente de novo. ')
            y=int(input('Quantas peças você vai tirar? '))
        return y
          
def partida():
    n=int(input('Quantas peças? '))
    m=int(input('Limite de peças por jogada? '))
    while n<m:
        print('numeros invalidos, tente novamente!')
        n=int(input('Quantas peças? '))
        m=int(input('Limite de peças por jogada? '))    
    usuario_joga=False 
    if n%(m+1)==0:
        usuario_joga=True
        print('')
        print('Voce começa!')
    else:
        print('')
        print('Computador começa!')
    
    while n>0:
        if usuario_joga==True:
            y=usuario_escolhe_jogada(n,m)
            n=n-y
            if y==1 and n>1:
                print('\nVoce tirou uma peça.')
                print('Agora restam {} peças no tabuleiro.'.format(n))          
            if y==1 and n==1:
                print('\nVoce tirou uma peça')
                print('Agora resta uma peça no tabuleiro.')
            if y>1:
                if n>1:
                    print('\nVoce tirou {} peças'.format(y))
                    print('Agora restam {} peças no tabuleiro'.format(n))
                else:
                    print('\nVoce tirou {} peças'.format(y))
                    print('Agora resta apenas uma peça no tabuleiro')
                    
            usuario_joga=False
            
        else:
            x=computador_escolhe_jogada(n, m)
            n=n-x
            if x==1 and n==0:
                print('\nO computador tirou uma peça.')
                print('Fim do jogo! O computador ganhou!')  
            if x==n and n==0:
                print('\nO computador tirou {} peças.'.format(x))
                print('Fim do jogo! O computador ganhou!')                 
            if x==1 and n>1:
                print('\nO computador tirou uma peça.')
                print('Agora restam {} peças no tabuleiro.'.format(n))
            if x==1 and n==1:
                print('\nO computador tirou uma peça.')
                print('Agora resta {} peça no tabuleiro.'.format(n))                 
            if x>1:
                if n==0:
                    print('\nO computador tirou {} peças.'.format(x))
                    print('Fim do jogo! O computador ganhou!')
                else: 
                    print('\nO computador tirou {} peças'.format(x))
                    print('Agora restam {} peças no tabuleiro'.format(n))     

            usuario_joga=True  

def campeonato():
    rodada=1
    while rodada<=3:
        print('')
        print('**** Rodada {} ****'.format(rodada))
        print('')
        partida()
        rodada=rodada+1
    print('')
    print('**** Final do campeonato! ****')
    print('')
    print('Placar: Você 0 X 3 Computador')

def main():
    print('1 - para jogar uma partida isolada' )
    escolha=int(input('2 - para jogar um campeonato '))   
    if escolha==1:
        print('Voce escolheu uma partida isolada!')
        partida()
    if escolha==2:
        print('\nVoce escolheu um campeonato!')
        campeonato()
    else:
        while escolha!=1 and escolha!=2:
            print('\nNumero invalido! Tente novamente.\n')
            print('1 - para jogar uma partida isolada' )
            escolha=int(input('2 - para jogar um campeonato '))   
            if escolha==1:
                print('\nVoce escolheu uma partida isolada!')
                partida()
            if escolha==2:
                print('\nVoce escolheu um campeonato!')
                campeonato()

         
print(main())