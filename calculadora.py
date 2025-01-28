import tkinter as tk
import math  # Para a função de raiz quadrada

#Função para adicionar um número a tela
def ApertaBotao(key):
    Texto.set(Texto.get() + str(key))
    #Função para limpar a tela
def clear():
    Texto.set("")
#Função para apagar o último caractere
def backspace():
    current_text = Texto.get()
    Texto.set(current_text[:-1])
def calculate():
    try:
        # Se o símbolo de raiz quadrada (√) for encontrado, realiza o cálculo
        if '√' in Texto.get():
            value = float(Texto.get().replace('√', ''))  # Remove o símbolo √ e pega o número
            if value < 0:
                Texto.set("Erro")  # Não permite calcular raiz quadrada de números negativos
            else:
                result = math.sqrt(value)  # Calcula a raiz quadrada
                Texto.set(result)
        else:
            # Substitui ^ por ** para calcular a potência
            expression = Texto.get().replace('^', '**')
            result = eval(expression.replace('x', '*').replace('÷', '/'))  # Substitui x por * e ÷ por /
            Texto.set(result)
    except Exception as e:
        Texto.set("Erro")
# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")
Texto = tk.StringVar()
Entrada = tk.Entry(root, textvariable=Texto, font=("Arial", 20), bd=10, relief="sunken", justify="right", width=16)
Entrada.grid(row=0, column=0, columnspan=4, pady=10)
button_matrix = [
    ['C', '^', '√', '←'],
    ['1', '2', '3', 'x'],
    ['4', '5', '6', '-'],
    ['7', '8', '9', '+'],
    ['0', '.', '=', '÷']]
# Criando os botões com base na matriz
for row_index, row in enumerate(button_matrix):
    for col_index, button_text in enumerate(row):
        if button_text == "":  # Ignora células vazias na matriz
            continue
        if button_text == "=":
            tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 16), command=calculate).grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")
        elif button_text == "C":
            tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 16), command=clear).grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")
        elif button_text == "←":
            tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 16), command=backspace).grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")
        elif button_text == "^":
            tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 16), command=lambda: ApertaBotao('^')).grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")
        elif button_text == "√":
            tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 16), command=lambda: ApertaBotao('√')).grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")
        elif button_text == "x":
            tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 16), command=lambda key='x': ApertaBotao(key)).grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")
        elif button_text == "÷":
            tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 16), command=lambda key='÷': ApertaBotao(key)).grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")
        else:
            tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 16), command=lambda key=button_text:ApertaBotao(key)).grid(row=row_index + 1, column=col_index, padx=5, pady=5, sticky="nsew")

# Ajustando a responsividade da grade
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
# Rodando a interface
root.mainloop()
