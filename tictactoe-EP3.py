# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:43:25 2016

@author: Eduardo Prawita
"""

import tkinter as tk
import jogo

class tabuleiro:
    
    def __init__ (self):
        self.window = tk.Tk()
        self.window.title ('Jogo da Velha!')
        self.jogo=jogo.jogo()
        
        
        self.botao1=tk.Button(self.window,width=15,height=8 )
        self.botao1.grid(row=0,column=0)
        self.botao1.configure(command=lambda: self.callback1 ())
        
        self.botao2=tk.Button(self.window,width=15,height=8 )
        self.botao2.grid(row=0,column=1)
        self.botao2.configure(command=lambda: self.callback2 ())
        
        self.botao3=tk.Button(self.window,width=15,height=8 )
        self.botao3.grid(row=0,column=2)
        self.botao3.configure(command=lambda: self.callback3 ())
        
        self.botao4=tk.Button(self.window,width=15,height=8 )
        self.botao4.grid(row=1,column=0)
        self.botao4.configure(command=lambda: self.callback4 ())
        
        self.botao5=tk.Button(self.window,width=15,height=8 )
        self.botao5.grid(row=1,column=1)
        self.botao5.configure(command=lambda: self.callback5 ())
        
        self.botao6=tk.Button(self.window,width=15,height=8)
        self.botao6.grid(row=1,column=2)
        self.botao6.configure(command=lambda: self.callback6 ())
        
        self.botao7=tk.Button(self.window,width=15,height=8 )
        self.botao7.grid(row=2,column=0)
        self.botao7.configure(command=lambda: self.callback7 ())
        
        self.botao8=tk.Button(self.window,width=15,height=8 )
        self.botao8.grid(row=2,column=1)
        self.botao8.configure(command=lambda: self.callback8 ())
        
        self.botao9=tk.Button(self.window,width=15,height=8)
        self.botao9.grid(row=2,column=2)
        self.botao9.configure(command=lambda: self.callback9 ())
        
        self.proximajogada=tk.Label(self.window)
        self.proximajogada.configure(text="Proxima Jogada:X")
        self.proximajogada.grid(row=3)
 
    def iniciar(self):    
        self.window.mainloop()
        
        
    def callback1 (self):
        self.fim()
        self.jogo.recebe_jogadas(0,0)
        if self.jogo.rodadas % 2 == 0:
            self.botao1.configure(text="O")
            self.proximajogada.configure(text="Proxima Jogada:X")
        else:
            self.botao1.configure(text="X")
            self.proximajogada.configure(text="Proxima Jogada:O")
            
    def callback2 (self):
        self.fim()
        self.jogo.recebe_jogadas(0,1)
        if self.jogo.rodadas % 2 == 0:
            self.botao2.configure(text="O")
            self.proximajogada.configure(text="Proxima Jogada:X")
        else:
            self.botao2.configure(text="X")
            self.proximajogada.configure(text="Proxima Jogada:O")
           
    def callback3 (self):
        self.fim()        
        self.jogo.recebe_jogadas(0,2)
        if self.jogo.rodadas % 2 == 0:
            self.botao3.configure(text="O")
            self.proximajogada.configure(text="Proxima Jogada:X")
        else:
            self.botao3.configure(text="X")
            self.proximajogada.configure(text="Proxima Jogada:O")
          
    def callback4 (self):
        self.fim()
        self.jogo.recebe_jogadas(1,0)
        if self.jogo.rodadas % 2 == 0:
            self.botao4.configure(text="O")
            self.proximajogada.configure(text="Proxima Jogada:X")
        else:
            self.botao4.configure(text="X")
            self.proximajogada.configure(text="Proxima Jogada:O")
           
    def callback5 (self):
        self.fim()
        self.jogo.recebe_jogadas(1,1)
        if self.jogo.rodadas % 2 == 0:
            self.botao5.configure(text="O")
            self.proximajogada.configure(text="Proxima Jogada:X")
        else:
            self.botao5.configure(text="X")
            self.proximajogada.configure(text="Proxima Jogada:O")
        
    def callback6 (self):
        self.fim()
        self.jogo.recebe_jogadas(1,2)
        if self.jogo.rodadas % 2 == 0:
            self.botao6.configure(text="O")
            self.proximajogada.configure(text="Proxima Jogada:X")
        else:
            self.botao6.configure(text="X")
            self.proximajogada.configure(text="Proxima Jogada:O")
       
    def callback7 (self):
        self.fim()
        self.jogo.recebe_jogadas(2,0)
        if self.jogo.rodadas % 2 == 0:
            self.botao7.configure(text="O")
            self.proximajogada.configure(text="Proxima Jogada:X")
        else:
            self.botao7.configure(text="X")
            self.proximajogada.configure(text="Proxima Jogada:O")
         
    def callback8 (self):
        self.fim()
        self.jogo.recebe_jogadas(2,1)
        if self.jogo.rodadas % 2 == 0:
            self.botao8.configure(text="O")
            self.proximajogada.configure(text="Proxima Jogada:X")
        else:
            self.botao8.configure(text="X")
            self.proximajogada.configure(text="Proxima Jogada:O")
     
    def callback9 (self):
        self.fim()
        self.jogo.recebe_jogadas(2,2)
        if self.jogo.rodadas % 2 == 0:
            self.botao9.configure(text="O")
            self.proximajogada.configure(text="Proxima Jogada:X")
        else:
            self.botao9.configure(text="X")
            self.proximajogada.configure(text="Proxima Jogada:O")       
                   
                   
    def fim (self):
<<<<<<< HEAD
        if self.jogo.verifica_ganhador == 2 :
            self.proximajogada.configure(text="X ganhou")
            self.jogo.limpa_jogadas()
        elif self.jogo.verifica_ganhador == 1 :
            self.proximajogada.configure(text="Bolinha ganhou")
            self.jogo.limpa_jogadas()
        elif self.jogo.verifica_ganhador==0:
            self.proximajogada.configure(text="Empatou")
            self.jogo.limpa_jogadas()
        
=======
        self.jogo.verifica_ganhador(self.jogo.rodadas)
        self.jogo.limpa_jogadas()
        if self.jogo.verifica_ganhador == 2 :
            self.proximajogada.configure(text="X ganhou")
        if self.jogo.verifica_ganhador == 1 :
            self.proximajogada.configure(text="Bolinha ganhou")
        else :
            self.proximajogada.configure(text="Empatou")
>>>>>>> 9f943f037c47ab9e2991f94ddccf477f6358f8bc
            
        
        
        
root = tabuleiro()
root.iniciar()