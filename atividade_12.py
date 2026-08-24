def questão6():
    números = [int(input("Número 1: ")), int(input("Número 2: ")), int(input("Número 3: "))]

    print(f"Maior: {max(números)}\nMenor: {min(números)}")

def questão7():
    salário = float(input("Salário: "))

    if salário > 1250.0:
        aumento = 1.1

    else: 
        aumento = 1.15

    print(f"Salário aumentado: {salário * aumento:.2f}")

    

questão7()
