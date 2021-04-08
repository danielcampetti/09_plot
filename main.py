#Programa da interação entre Python e PowerBi

#region import
from PIL import ImageTk, Image
import tkinter as tk
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
#endregion

#region dados iniciais
L = 10  # largura total do galpao
Ag = 5  # altura do pé direito do galpao
At = 1  # altura do pé direito do telhado
Nn = 3  # Numeros de V
dT = 2  # 'Meio Comprimento do banzo de contato topo tesouras direitos e esquerdos
h = 0.4  # Largura da tesoura
a = 0.3  # Comnprimento a
Cg = 15  # Comprimento do galpao
Npo = 3  # Numero de porticos
T1 = 0.05
T2 = 0.04
#endregion

#region soluções iniciais
Np = Nn*2
d = dT/2
Kt = (L/2)-a-d
Alpha = math.atan(At/Kt)
b = math.asin(Alpha)*h
c = math.tan(Alpha)*b
e = h-(a*At/Kt)
f = math.sin(Alpha)*h
j = math.tan(Alpha)*d
# valor do passo de comprimento em 'y' de cada meio V
Ap = (At-c)/Np
K = Kt-b
Kp = K/Np  # valor do passo de comprimento em 'x' de cada meio V
#endregion

root_largura = 700
root_comprimento = 800
root = tk.Tk()
root.title("Aplicativo Nieto Engenharia")
root.iconbitmap('.//img//logo.ico')
canvas = tk.Canvas(root, height=root_largura, width=root_comprimento)
canvas.pack()

frame1 = tk.Frame(root, bg='#abd1db')
frame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# teste
button_quit = tk.Button(frame1, text="Fechar Programa", command=root.quit)
button_quit.pack()

root.mainloop()
print('-------------------Complete--------------------------------')
