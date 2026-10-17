import tkinter as tk
import random as r
import time as t

def lgbt():
    janela = tk.Tk()
    janela.title("Se você leu isto, você é ainda mais LGBTQIAPN+")
    janela.resizable(False, False)
    janela.state("zoomed")

    largura_tela = janela.winfo_screenwidth()

    tamanho_fonte = int(largura_tela * 0.025)

    cores = ["#E40303", "#FF8C00", "#FFED00", "#008026", "#004DFF", "#750787"]

    for cor in cores:
        frame = tk.Frame(janela, bg=cor)
        frame.pack(expand=True, fill="both")

    mensagem = tk.Label(janela, text="Você é LGBTQIAPN+", bg="white", fg="black", font=("Comic Sans MS", tamanho_fonte))
    mensagem.place(relx=0.5, rely=0.5, anchor="center")

    janela.mainloop()

resposta = input("Você aceita o presente? (s/n): ")

if resposta == "s" or resposta == "S":
    for i in range(4):
        print("PLAYSTATION!", end=" ", flush=True)
        t.sleep(1.25)

    presente = r.randint(0,3)

    match presente:
        case 1:
            print("\nParabéns, você ganhou um PlayStation 5 Pro com GTA 6 comprado na pré-venda. Aproveite!")

        case 2:
            print("\nOloko, você adquiriu os poderes malignos do Tio Léo e do Geraldo. Use-os com sabedoria e moderação...")

        case 3:
            while True:
                lgbt()

        case _:
            print("\nO presente está vazio, que pena...")

elif resposta == "n" or resposta == "N":
    print("Evapore então, seu merda.")

else:
    print("Você só tinha UM trabalho, que era digitar o solicitado, e não o fez... (s/n)")
