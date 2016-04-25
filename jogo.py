# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:43:25 2016

@author: Eduardo Prawita
"""
import numpy as np

class jogo:
    matriz=np.array([[0,0,0],[0,0,0],[0,0,0]])
    rodadas=0
    def __init__(self,matriz,rodadas):
        self.matriz=matriz
        self.rodadas=rodadas
        
    def recebe_jogadas(self,linha,coluna):
        if self.rodadas%2==0:
        #o numero 1 representa o X enquanto o 2 seria o O
            self.matriz[linha][coluna]=1
            self.rodadas+=1
        else:
            self.matriz[linha][coluna]=2
            self.rodadas+=1
                        
    def verifica_ganhador(self,rodadas):
        if self.rodadas>=4:#primeira oportunidade de acabar o jogo
            #quando X eh vencedor
            if self.matriz[0][0]==1 and self.matriz[0][1]==1 and self.matriz[0][2]==1:
                return 2
            elif self.matriz[1][0]==1 and self.matriz[1][1]==1 and self.matriz[1][2]==1:
                return 2
            elif self.matriz[2][0]==1 and self.matriz[2][1]==1 and self.matriz[2][2]==1:
                return 2
            elif self.matriz[0][0]==1 and self.matriz[1][0]==1 and self.matriz[2][0]==1:
                return 2
            elif self.matriz[0][1]==1 and self.matriz[1][1]==1 and self.matriz[2][1]==1:
                return 2
            elif self.matriz[0][2]==1 and self.matriz[1][2]==1 and self.matriz[2][2]==1:
                return 2
            elif self.matriz[0][0]==1 and self.matriz[1][1]==1 and self.matriz[2][2]==1:
                return 2
            elif self.matriz[0][2]==1 and self.matriz[1][1]==1 and self.matriz[2][0]==1:
                return 2
            # quando O eh vencedor
            elif self.matriz[0][0]==2 and self.matriz[0][1]==2 and self.matriz[0][2]==2:
                return 1
            elif self.matriz[1][0]==2 and self.matriz[1][1]==2 and self.matriz[1][2]==2:
                return 1
            elif self.matriz[2][0]==2 and self.matriz[2][1]==2 and self.matriz[2][2]==2:
                return 1
            elif self.matriz[0][0]==2 and self.matriz[1][0]==2 and self.matriz[2][0]==2:
                return 1
            elif self.matriz[0][1]==2 and self.matriz[1][1]==2 and self.matriz[2][1]==2:
                return 1
            elif self.matriz[0][2]==2 and self.matriz[1][2]==2 and self.matriz[2][2]==2:
                return 1
            elif self.matriz[0][0]==2 and self.matriz[1][1]==2 and self.matriz[2][2]==2:
                return 1
            elif self.matriz[0][2]==2 and self.matriz[1][1]==2 and self.matriz[2][0]==2:
                return 1   
            #para as jogadas emmpatadas deve estar na 9,8 no caso por comecar no 0 rodada e nao pode ter 
            elif self.rodadas==9:
                return 0
            #dispensei o -1 ja que as unicaas possibilidades de jogo eh ganhar, perder ou ematar
    def limpa_jogadas(self):
       
        if self.verifica_ganhador(jogo,jogo.rodadas)==0:
            print ('empatou')
            self.matriz=np.array([[0,0,0],[0,0,0],[0,0,0]])
        if self.verifica_ganhador(jogo,jogo.rodadas)==1:
            print('jogador O ganhou')
            self.matriz=np.array([[0,0,0],[0,0,0],[0,0,0]])
        if self.verifica_ganhador(jogo,jogo.rodadas)==2:
            print('jogador X ganhou')
            self.matriz=np.array([[0,0,0],[0,0,0],[0,0,0]])
        if jogo.rodadas%2!=0:
            jogo.rodadas=1
        if jogo.rodadas%2==0:
            jogo.rodadas=0
        return self.matriz
        

"""fazendo o teste se as funcoes estao funcionando, corretamente para os casos, testei 10 vezes,
 dois empates, 4 vitorias de X e 4 Vitorias de O
 O teste mostrou inicialmente os problemas de cada parte do jogo, imprimindo as matrizes pude
 ver onde inseria as posicoes e como ia as rodadas
 """
print (jogo.matriz)
jogo.recebe_jogadas(jogo,0,0)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,1,1)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,0,1)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,0,2)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,1,0)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,2,0)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,1,2)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,2,2)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,2,1)
print(jogo.rodadas)
print(jogo.matriz)

if jogo.verifica_ganhador(jogo,jogo.rodadas)== 0 or 1 or 2:
    jogo.limpa_jogadas(jogo)
print(jogo.rodadas)
print(jogo.matriz) 