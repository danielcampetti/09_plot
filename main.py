# Programa da interação entre Python e PowerBi

# region import
from PIL import ImageTk, Image
import tkinter as tk
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
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
# endregion

#region ----------------------------- Criando listas

x = [[1, 2, 3], [4, 5, 6]]

x1 = x[0][2]
print(x1)

x2 = np.array(range(50))
y2 = x2*3
print(y2)


plt.title('PLot1')
plt.plot(x2, y2)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.axis([0, 6, 0, 20])
plt.show()


root_largura = 700
root_comprimento = 800
root = tk.Tk()
root.title("Aplicativo Nieto Engenharia")
root.iconbitmap('.//img//logo.ico')

fig = Figure(figsize=(5, 4), dpi=100)


canvas = tk.Canvas(root, height=root_largura, width=root_comprimento)
canvas.pack()

# frame1 = tk.Frame(root, bg='#abd1db')
# frame1.place(relx=0, rely=0, relwidth=1, relheight=1)

# def function_resposta(entrada1):
#     print('Botao calc clicado',entrada1)
#     return str(entrada1)

# def function_calc(entrada1):
#     saida1['text']=function_resposta(entrada1)

# entrada1  =  tk.Entry(frame1, bg='#8bcde0')
# entrada1.grid(row=0, column=1)

# saida1  =  tk.Label(frame1, bg='#8bcde0')
# saida1.grid(row=1, column=1,ipadx=50,ipady=50)


# button_calc = tk.Button(frame1, text="Calcular", command=lambda: function_calc(entrada1.get()))
# button_calc.grid(row=3,  column=1,ipadx=50,ipady=50)

# button_quit = tk.Button(frame1, text="Fechar Programa", command=root.quit)
# button_quit.place(x=0,y=root_largura-30)
# print('-------------------Complete--------------------------------')
# root.mainloop()
# # endregion
