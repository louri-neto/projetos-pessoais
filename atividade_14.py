def questão1():
    s = str(input("String: "))
    c = str(input("Caractere: "))
    p = s.find(c, int(input("Posição: ")))

    if p == True:
        print("Caractere encontrado")

    else:
        print("Caractere não encontrado")

def questão2():
    data = str(input("Data (DD/MM/AAAA): "))

    if len(data) != 10:
        print("A string deve ter 10 caracteres")
        return
    
    if data[2] != "/" and data[5] != "/":
        print("Sem barras ou barras em posições erradas")
        return

    for i in range(10):
        if i == 2 or i == 5:
            continue

        if not data[i].isdigit():
            print("A string não deve conter letras, símbolos (a não ser o /) ou espaços")
            return
    
    dia, mês, ano = [int(x) for x in data.split("/")]

    print(f"Dia: {dia}\n"
          f"Mês: {mês}\n"
          f"Ano: {ano}")

def questão3():
    frase = input("Frase: ")

    semEspaço = frase.replace(" ", "")

    print(f"Frase sem espaços: {semEspaço}")

questão3()