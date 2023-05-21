import tkinter as tk
from ..Model.Model import hello_world

hello_world()


"""
Importe a lógica contida em Model e suas funções. Coloque a parte de interação 
com o usuário em View.py, como clicar em btn etc.

"""
def start_gui():
    root = tk.Tk()

    # Cria um botão que chama a função "hello_world" quando clicado
    button = tk.Button(root, text="Clique Aqui", command=hello_world)
    button.pack()

    # Inicia o loop da interface gráfica
    root.mainloop()