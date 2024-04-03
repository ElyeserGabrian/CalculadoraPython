import tkinter as tk

# Função para adicionar número ou operador ao campo de entrada
def adicionar_caractere(caractere):
    entrada_texto.insert(tk.END, caractere)

# Função para calcular e mostrar o resultado
def calcular():
    expressao = entrada_texto.get()
    try:
        resultado = eval(expressao)
        resultado_texto.set(resultado)
    except Exception as e:
        resultado_texto.set("Erro")

# Função para limpar o campo de entrada e o resultado
def limpar():
    entrada_texto.delete(0, tk.END)
    resultado_texto.set("")

# Criação da janela
janela = tk.Tk()
janela.title("Calculadora do Ely")

# Variável para armazenar o resultado
resultado_texto = tk.StringVar()
resultado_texto.set("")

# Resultado
resultado_label = tk.Label(janela, textvariable=resultado_texto, font=('Arial', 14))
resultado_label.grid(row=1, column=15, columnspan=4, padx=10, pady=10)

# Campo de entrada
entrada_texto = tk.Entry(janela, width=30, font=('Arial', 14))
entrada_texto.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Botões numéricos
for i in range(10):
    if i == 0:
        tk.Button(janela, text=str(i), width=10, command=lambda i=i: adicionar_caractere(str(i))).grid(row=4, column=1)
    else:
        tk.Button(janela, text=str(i), width=10, command=lambda i=i: adicionar_caractere(str(i))).grid(row=(9-i)//3 + 2, column=(i-1)%3)

# Botões de operações
operadores = ['+', '-', '*', '/']
for i, operador in enumerate(operadores):
    tk.Button(janela, text=operador, width=10, command=lambda operador=operador: adicionar_caractere(operador)).grid(row=i+2, column=3)

# Botão de igual
tk.Button(janela, text='=', width=10, command=calcular).grid(row=4, column=2)

# Botão de limpar
tk.Button(janela, text='C', width=10, command=limpar).grid(row=4, column=0)

# Loop principal
janela.mainloop()
