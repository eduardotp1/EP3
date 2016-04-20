import tkinter as tk

class tabuleiro:
    
    def __init__ (self):
        self.window = tk.Tk()
        self.window.title ('Jogo da Velha!')
        
        
        botao1=tk.Button(self.window,width=15,height=8)
        botao1.grid(row=0,column=0)
        
        botao2=tk.Button(self.window,width=15,height=8)
        botao2.grid(row=0,column=1)
        
        botao3=tk.Button(self.window,width=15,height=8)
        botao3.grid(row=0,column=2)
        
        botao4=tk.Button(self.window,width=15,height=8)
        botao4.grid(row=1,column=0)
        
        botao5=tk.Button(self.window,width=15,height=8)
        botao5.grid(row=1,column=1)
        
        botao6=tk.Button(self.window,width=15,height=8)
        botao6.grid(row=1,column=2)
        
        botao7=tk.Button(self.window,width=15,height=8)
        botao7.grid(row=2,column=0)
        
        botao8=tk.Button(self.window,width=15,height=8)
        botao8.grid(row=2,column=1)
        
        botao9=tk.Button(self.window,width=15,height=8)
        botao9.grid(row=2,column=2)
        
        proximajogada=tk.Label(self.window,text='Proxima Jogada:')
        proximajogada.grid(row=3)
 
    def iniciar(self):    
        self.window.mainloop()
 
     
root = tabuleiro()
root.iniciar()