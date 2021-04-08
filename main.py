# Programa da interação entre Python e PowerBi

# region import
from PIL import ImageTk, Image
import tkinter as tk
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


# endregion

# region dados iniciais
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
# endregion

# region soluções iniciais
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
Npp = (Npo-2)  # Numero de passos comprimento de cada portico

if Npp == 0:
    Npp == 1
Pp = Cg/Npp   # #Distancia entre porticos


# endregion

# region ----------------- Criando LabelFrame and plot


# x2 = np.array(range(50))
# y2 = x2*3


# plt.title('PLot1')
# plt.plot(x2, y2)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.axis([0, 6, 0, 20])
# # plt.show()


# root = tk.Tk()
# root.title("Aplicativo Nieto Engenharia")
# root.iconbitmap('.//img//logo.ico')
# root.minsize(1500, 900)

# frame1 = tk.LabelFrame(root, text="LabelFrame 1", bg='#6473c4')
# frame1.grid(row=0, column=0, sticky='N')
# frame2 = tk.LabelFrame(root, text="LabelFrame 2", bg='#3c3e4d')
# frame2.grid(row=1, column=0, sticky='N')

# x2 = np.array(range(50))
# y2 = x2*3
# df = pd.DataFrame({'A': x2, 'B': y2}, index=range(50))
# # fig = Figure()
# figure1 = plt.Figure(figsize=(5, 4), dpi=80)
# ax1 = figure1.add_subplot(111).plot(x2,y2)
# canvas = FigureCanvasTkAgg(figure1, frame1)
# canvas.draw()
# canvas.get_tk_widget().grid(row=1, column=0, sticky='N')

# toolbarFrame = tk.Frame(frame2)
# toolbarFrame.grid(row=22, column=4)
# toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

# button_quit = tk.Button(frame1, text="10", command=root.quit, padx=50, pady=50)
# button_quit.grid(row=0, column=0, sticky='N')

# button_quit1 = tk.Button(frame2, text="11", command=root.quit)
# button_quit1.grid(row=0, column=0, sticky='N')

# print('-------------------Complete--------------------------------')
# root.mainloop()

# endregion


# region

# PONTOS BANZOS ESQUERDO E DIREITO
# ------------BANZOS ESQUERDA---------------
# Ponto x=0
# coord(1,:)=[0 Ag];
a = np.array([[0, 1, 2, 3], [0, 4, 5, 6]])
# print(a)
a = np.append(a, [[50, 60, 70, 0]], axis=0)
# b = a[1, 1]
# print(a)
# print(b)
a = np.append(a, [[500, 600, 700, 0]], axis=0)

# print(a)


# coord = np.array([0, Ag+e])


# print('coord'=str(coord))

aa=1

def pr(variavel):
    print(str(variavel),'==',str(variavel))

pr(aa)
    # coord(2,:)=[0 Ag+e];
    # terca(1,:)=coord(2,:); %Capturando terça inicial - X ESQUERDO


    # engregion
