def questão6():
    n = [float(input("Número 1: ")), float(input("Número 2: ")), float(input("Número 3: "))]

    print(f"Maior: {max(n)}\nMenor: {min(n)}")

def questão7():
    salário = float(input("Salário: "))

    if salário > 1250.0:
        aumento = 1.1

    else: 
        aumento = 1.15

    print(f"Salário aumentado: {salário * aumento:.2f}")

def questão8():
    import operator as op

    operadores = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv,}

    n = [float(input("Número 1: ")), float(input("Número 2: "))]
    operação = input("Operação: ")

    if operação in operadores:
        print(f"Resultado: {operadores[operação](n[0], n[1])}")

    else:
        print("Operação inválida")

def questão9():
    valor_da_casa = float(input("Valor da casa: "))
    salário = float(input("Salário: "))
    meses_a_pagar = int(input("Anos a pagar: ")) * 12

    if valor_da_casa / meses_a_pagar > 0.3 * salário:
        print("Empréstimo reprovado")
    else:
        print(f"Empréstimo aprovado\nPrestação mensal:{valor_da_casa / meses_a_pagar:.2f}")

def questão10():
    kwh = float(input("kWh consumidos: "))
    instalação = input("Tipo de instalação: ")

    

questão10()
