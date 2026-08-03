import tkinter as tk
import random as r
import time as t

def lgbt():
    janela = tk.Tk()
    janela.title("Se você leu isto, você é ainda mais LGBTQIAPN+")
    janela.state("zoomed")
    janela.resizable(False, False)
    
    vermelho = tk.Frame(
        janela,
        bg="#E40303"
    )
    vermelho.pack(expand=True, fill="both")
    
    laranja = tk.Frame(
        janela,
        bg="#FF8C00"
    )
    laranja.pack(expand=True, fill="both")

    amarelo = tk.Frame(
        janela,
        bg="#FFED00"
    )
    amarelo.pack(expand=True, fill="both")

    verde = tk.Frame(
        janela,
        bg="#008026"
    )
    verde.pack(expand=True, fill="both")

    azul = tk.Frame(
        janela,
        bg="#004DFF"
    )
    azul.pack(expand=True, fill="both")

    roxo = tk.Frame(
        janela,
        bg="#750787"
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

if resposta == "s" or resposta == "S":
    for i in range(4):
        print(f"PLAYSTATION!", end=" ", flush=True)
        t.sleep(1.25)

    presente = r.randint(1,4)

    if presente == 1:
        print(f"\nO presente está vazio, que pena...")

    elif presente == 2:
        print(f"\nParabéns, você ganhou um PlayStation 5 Pro com GTA 6 comprado na pré-venda. Aproveite!")

    elif presente == 3:
        print(f"\nOloko, você adquiriu os poderes malignos do Tio Léo e do Geraldo. Use-os com sabedoria e moderação...")

    else:
        lgbt()

elif resposta == "n" or resposta == "N":
    print(f"Evapore então, seu merda.")

else:
    print(f"Você só tinha UM trabalho, que era digitar o solicitado, e não o fez... (s/n)")
