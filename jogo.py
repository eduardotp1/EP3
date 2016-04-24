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
            self.matriz[linha][coluna]=="X"
            self.rodadas+=1
            
        else:
            self.matriz[linha][coluna]=="O"
            self.rodadas+=1
                        
    def verifica_ganhador(self,rodadas):
        if self.rodadas>=4:#primeira oportunidade de acabar o jogo
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
            #para as jogadas emmpatadas deve estar na 9 rodada e nao pode ter 
            elif self.rodadas==8:
                return 0
    def limpa_jogadas(self):
        if self.verifica_ganhador()==0:
            print ('empatou')
            self.matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
            self.rodadas+=1
        elif self.verifica_ganhador()==1:
            print('jogador X ganhou')
            self.matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
        else:
            print('jogador O ganhou')
            self.matriz=np.array([[0,1,2],[10,11,12],[20,21,22]])
        return self.matriz

print (jogo.matriz)
#jogo.verifica_ganhador(jogo,jogo.rodadas)
jogo.recebe_jogadas(jogo,0,0)
#jogo.verifica_ganhador(jogo,jogo.rodadas)
jogo.recebe_jogadas(jogo,1,0)
#jogo.verifica_ganhador(jogo,jogo.rodadas)
jogo.recebe_jogadas(jogo,0,1)
#jogo.verifica_ganhador(jogo,jogo.rodadas)
jogo.recebe_jogadas(jogo,1,2)
#jogo.verifica_ganhador(jogo,jogo.rodadas)
jogo.recebe_jogadas(jogo,0,2)
#jogo.verifica_ganhador(jogo,jogo.rodadas)
print(jogo.matriz)
#print (jogo.verifica_ganhador(jogo,jogo.rodadas))