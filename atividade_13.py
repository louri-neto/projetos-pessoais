def questão11():
    while True:
        operação = int(input("1 - Adição\n"
                             "2 - Subtração\n"
                             "3 - Multiplicação\n"
                             "4 - Divisão\n"
                             "5 - Sair\n"
                             "Opção: "))

        if operação != 5:
            x = int(input("Número: "))

            match operação:
                case 1:
                    for i in range(1, 11):
                        print(f"{x} + {i} = {x + i}")

                case 2:
                    for i in range(x, x + 11):
                        print(f"{i} - {x} = {i - x}")

                case 3:
                    for i in range(1, 11):
                        print(f"{x} * {i} = {x * i}")

                case 4:
                    for i in range(1, 11):
                        print(f"{x * i} / {x} = {i}")

                case _:
                    print("Operação inválida")

            resposta = input("Continuar? (s/n): ").upper()

            if resposta == "N": break

        else: break

def questão12():
    n = int(input("Número: "))
    primo = True

    if n <= 1: primo = False

    elif n == 2: primo = True

    elif n % 2 == 0: primo = False

    else:
        for i in range(3, n, 2):
            if n % i == 0: 
                primo = False
                break

    if primo: print("É primo")

    else: print("Não é primo")

def questão13():
    n = float(input("Número: "))
    b = 2

    while abs(b * b - n) > 0.0001:
        p = (b + (n / b)) / 2
        b = p

    print(f"Raiz: {b:.4f}")

def questão14():
    n = [int(input("Número 1: ")), int(input("Número 2: "))]

    while n[0] >= n[1]: n[0] -= n[1]

    print(f"Resto: {n[0]}")

def questão15():
    n = int(input("Número: "))
    original = n
    reverso = 0

    while original != 0:
        reverso = reverso * 10 + (original % 10)
        original //= 10

    if n == reverso: print("É um palindromo")

    else: print("Não é um palindromo")


questão14()