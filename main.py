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
# endregion

# region ----------------------------- Criando listas


x2 = np.array(range(50))
y2 = x2*3


plt.title('PLot1')
plt.plot(x2, y2)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.axis([0, 6, 0, 20])
# plt.show()


root = tk.Tk()
root.title("Aplicativo Nieto Engenharia")
root.iconbitmap('.//img//logo.ico')
root.minsize(1000, 700)
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)

frame1 = tk.Frame(root, bg='#abd1db')
# frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
frame1.grid(row=0, column=1, sticky='N')

df = pd.DataFrame({'A': range(20),
                   'B': [math.sin(i) for i in range(20)]
                   }, index=range(20))


x2 = np.array(range(50))
y2 = x2*3

# fig = Figure()
figure1 = plt.Figure(figsize=(5, 4), dpi=80)
ax1 = figure1.add_subplot(111)
canvas = FigureCanvasTkAgg(figure1, frame1)
# canvas.draw()
canvas.get_tk_widget().grid(row=1, column=2, sticky='N')

df = df.iloc[:, 1]
df.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
ax1.set_title('Initial data')

button_quit = tk.Button(frame1, text="Fechar Programa", command=root.quit)
button_quit.grid(row=2, column=2, sticky='N')

print('-------------------Complete--------------------------------')
root.mainloop()


# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# def on_key(event):
#     print('press')
#     key_press_handler(event, canvas, toolbar)

# canvas.mpl_connect('key', on_key)

# frame1 = tk.Frame(root, bg='#abd1db')
# frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
