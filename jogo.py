# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:43:25 2016

@author: Eduardo Prawita
"""
import numpy as np

class jogo:
    
    def __init__(self,matriz,rodadas):
        self.matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
        self.rodadas=0
        
    def recebe_jogadas(self,linha,coluna):
        if self.rodadas==0 or 2 or 4 or 6 or 8:
            self.matriz[(linha)][(coluna)]="X"
            self.rodadas+=1
            
        else:
            self.matriz[(linha)][(coluna)]="O"
            self.rodadas+=1
                        
    def verifica_ganhador(self):
        if self.rodadas>=4:
            #quando X eh vencedor
            if self.matriz[0][0]=="X" and self.matriz[0][1]=="X" and self.matriz[0][2]=="X":
                return 1
            elif self.matriz[1][0]=="X" and self.matriz[1][1]=="X" and self.matriz[1][2]=="X":
                return 1
            elif self.matriz[2][0]=="X" and self.matriz[2][1]=="X" and self.matriz[2][2]=="X":
                return 1
            elif self.matriz[0][0]=="X" and self.matriz[1][0]=="X" and self.matriz[2][0]=="X":
                return 1
            elif self.matriz[0][1]=="X" and self.matriz[1][1]=="X" and self.matriz[2][1]=="X":
                return 1
            elif self.matriz[0][2]=="X" and self.matriz[1][2]=="X" and self.matriz[2][2]=="X":
                return 1
            elif self.matriz[0][0]=="X" and self.matriz[1][1]=="X" and self.matriz[2][2]=="X":
                return 1
            elif self.matriz[0][2]=="X" and self.matriz[1][1]=="X" and self.matriz[2][0]=="X":
                return 1
            # quando O eh vencedor
            elif self.matriz[0][0]=="O" and self.matriz[0][1]=="O" and self.matriz[0][2]=="O":
                return 2
            elif self.matriz[1][0]=="O" and self.matriz[1][1]=="O" and self.matriz[1][2]=="O":
                return 2
            elif self.matriz[2][0]=="O" and self.matriz[2][1]=="O" and self.matriz[2][2]=="O":
                return 2
            elif self.matriz[0][0]=="O" and self.matriz[1][0]=="O" and self.matriz[2][0]=="O":
                return 2
            elif self.matriz[0][1]=="O" and self.matriz[1][1]=="O" and self.matriz[2][1]=="O":
                return 2
            elif self.matriz[0][2]=="O" and self.matriz[1][2]=="O" and self.matriz[2][2]=="O":
                return 2
            elif self.matriz[0][0]=="O" and self.matriz[1][1]=="O" and self.matriz[2][2]=="O":
                return 2
            elif self.matriz[0][2]=="O" and self.matriz[1][1]=="O" and self.matriz[2][0]=="O":
                return 2   
            elif self.rodadas==8:
                return 0
    def limpa_jogadas(self):
        if self.verifica_ganhador()==0:
            print ('empatou')
            self.matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
        elif self.verifica_ganhador()==1:
            print('jogador X ganhou')
            self.matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
        else:
            print('jogador O ganhou')
            self.matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
        return self.matriz
for i in range (0,3):
    for j in range (0,3):
        jogo.recebe_jogadas(i,j)
        jogo.verifica_ganhador()
print (jogo.matriz)

