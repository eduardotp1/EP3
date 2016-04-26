# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:43:25 2016

@author: Eduardo Prawita
"""
import numpy as np

class jogo:
    def __init__(self):
        self.matriz=[[0,0,0],[0,0,0],[0,0,0]]
        self.rodadas=0
        
    def recebe_jogadas(self,linha,coluna):
        if self.matriz[linha][coluna]==0:
            if self.rodadas%2==0:
                #o numero 1 representa o X enquanto o 2 seria o O
                self.matriz[linha][coluna]=1
                self.rodadas+=1
            else:
                self.matriz[linha][coluna]=2
                self.rodadas+=1
        print(self.matriz)
        print(self.rodadas)
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
            #dispensei o -1 ja que as unicas possibilidades de jogo eh ganhar, perder ou empatar
    def limpa_jogadas(self):
       
        if self.verifica_ganhador(self.rodadas)==0:
            self.matriz=np.array([[0,0,0],[0,0,0],[0,0,0]])
        if self.verifica_ganhador(self.rodadas)==1:
            self.matriz=np.array([[0,0,0],[0,0,0],[0,0,0]])
        if self.verifica_ganhador(self.rodadas)==2:
            self.matriz=np.array([[0,0,0],[0,0,0],[0,0,0]])
        if self.rodadas%2!=0:
            self.rodadas=1
        if self.rodadas%2==0:
            self.rodadas=0
        return self.matriz