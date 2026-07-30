import tkinter as tk
import random as r
import time as t

def lgbt():
    cor_vermelho = "#E40303"
    cor_laranja = "#FF8C00"
    cor_amarelo = "#FFED00"
    cor_verde = "#008026"
    cor_azul = "#004DFF"
    cor_roxo = "#750787"

    janela = tk.Tk()
    janela.title("Se você leu isto, você é ainda mais LGBTQIAPN+")
    janela.state("zoomed")
    janela.configure(bg="white")
    janela.resizable(False, False)
    
    vermelho = tk.Frame(
        janela,
        bg=cor_vermelho
    )
    vermelho.pack(expand=True, fill="both")
    
    laranja = tk.Frame(
        janela,
        bg=cor_laranja
    )
    laranja.pack(expand=True, fill="both")

    amarelo = tk.Frame(
        janela,
        bg=cor_amarelo
    )
    amarelo.pack(expand=True, fill="both")

    verde = tk.Frame(
        janela,
        bg=cor_verde
    )
    verde.pack(expand=True, fill="both")

    azul = tk.Frame(
        janela,
        bg=cor_azul,
    )
    azul.pack(expand=True, fill="both")

    roxo = tk.Frame(
        janela,
        bg=cor_roxo
    )
    roxo.pack(expand=True, fill="both")

    mensagem = tk.Label(
        janela,
        text="Você é LGBTQIAPN+",
        bg="white",
        fg="black",
        font=("Comic Sans MS", 24) 
    )
    mensagem.place(relx=0.5, rely=0.5, anchor="center")

    janela.mainloop()

resposta = input(f"Você aceita o presente? (s/n): ")

if resposta == "s":
    for i in range(4):
        print(f"PLAYSTATION!", end=" ", flush=True)
        t.sleep(1.25)

    presente = r.randint(0,3)

    if presente == 0: print(f"\nO presente está vazio, que pena...")

    elif presente == 1: print(f"\nParabéns mano, você ganhou um PlayStation 5 Pro com GTA 6 comprado na pré-venda. Aproveite!")

    elif presente == 2: print (f"\nOloko mano, você adquiriu os poderes malignos do Tio Léo e do Geraldo. Use-os com sabedoria e moderação...")

    else: lgbt()

elif resposta == "n": print(f"Evapore então, seu merda.")

else: print(f"Você só tinha UM trabalho, que era digitar o solicitado, e não o fez... (s/n)")