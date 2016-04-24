# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:43:25 2016

@author: Eduardo Prawita
"""
import numpy as np

class jogo:
    matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
    rodadas=0
    def __init__(self,matriz,rodadas):
        self.matriz=matriz
        self.rodadas=rodadas
        
    def recebe_jogadas(self,linha,coluna):
        if self.rodadas%2==0:
            self.matriz[linha][coluna]==0
            self.rodadas+=1
        else:
            self.matriz[linha][coluna]==1
            self.rodadas+=1
                        
    def verifica_ganhador(self,rodadas):
        if self.rodadas>=4:#primeira oportunidade de acabar o jogo
            #quando X eh vencedor
            if self.matriz[0][0]=="X" and self.matriz[0][1]=="X" and self.matriz[0][2]=="X":
                return 2
            elif self.matriz[1][0]=="X" and self.matriz[1][1]=="X" and self.matriz[1][2]=="X":
                return 2
            elif self.matriz[2][0]=="X" and self.matriz[2][1]=="X" and self.matriz[2][2]=="X":
                return 2
            elif self.matriz[0][0]=="X" and self.matriz[1][0]=="X" and self.matriz[2][0]=="X":
                return 2
            elif self.matriz[0][1]=="X" and self.matriz[1][1]=="X" and self.matriz[2][1]=="X":
                return 2
            elif self.matriz[0][2]=="X" and self.matriz[1][2]=="X" and self.matriz[2][2]=="X":
                return 2
            elif self.matriz[0][0]=="X" and self.matriz[1][1]=="X" and self.matriz[2][2]=="X":
                return 2
            elif self.matriz[0][2]=="X" and self.matriz[1][1]=="X" and self.matriz[2][0]=="X":
                return 2
            # quando O eh vencedor
            elif self.matriz[0][0]=="O" and self.matriz[0][1]=="O" and self.matriz[0][2]=="O":
                return 1
            elif self.matriz[1][0]=="O" and self.matriz[1][1]=="O" and self.matriz[1][2]=="O":
                return 1
            elif self.matriz[2][0]=="O" and self.matriz[2][1]=="O" and self.matriz[2][2]=="O":
                return 1
            elif self.matriz[0][0]=="O" and self.matriz[1][0]=="O" and self.matriz[2][0]=="O":
                return 1
            elif self.matriz[0][1]=="O" and self.matriz[1][1]=="O" and self.matriz[2][1]=="O":
                return 1
            elif self.matriz[0][2]=="O" and self.matriz[1][2]=="O" and self.matriz[2][2]=="O":
                return 1
            elif self.matriz[0][0]=="O" and self.matriz[1][1]=="O" and self.matriz[2][2]=="O":
                return 1
            elif self.matriz[0][2]=="O" and self.matriz[1][1]=="O" and self.matriz[2][0]=="O":
                return 1   
            #para as jogadas emmpatadas deve estar na 9,8 no caso por comecar no 0 rodada e nao pode ter 
            elif self.rodadas==8:
                return 0
            #dispensei o -1 ja que as unicaas possibilidades de jogo eh ganhar, perder ou ematar
    def limpa_jogadas(self):
        if self.verifica_ganhador(jogo,jogo.rodadas)==0:
            print ('empatou')
            self.matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
        elif self.verifica_ganhador(jogo,jogo.rodadas)==1:
            print('jogador O ganhou')
            self.matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
        elif self.verifica_ganhador(jogo,jogo.rodadas)==2:
            print('jogador X ganhou')
            self.matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
        return self.matriz
        if jogo.rodadas%2==0:
            jogo.rodadas=1
        if jogo.rodadas%2!=0:
            jogo.rodadas=0
            
"""fazendo o teste se as funcoes estao funcionando, corretamente para os casos"""
print (jogo.matriz)
jogo.recebe_jogadas(jogo,0,0)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,1,0)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,0,1)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,1,2)
print(jogo.rodadas)
print(jogo.matriz)
jogo.recebe_jogadas(jogo,0,2)
print(jogo.rodadas)
print(jogo.matriz)
print (jogo.verifica_ganhador(jogo,jogo.rodadas))
if jogo.verifica_ganhador(jogo,jogo.rodadas)== 0 or 1 or 2:
    jogo.limpa_jogadas(jogo)
