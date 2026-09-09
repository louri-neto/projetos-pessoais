#include <stdio.h>
#include <math.h>

#ifdef _WIN32
    #include <windows.h>
#else
    #include <locale.h>
#endif

void questao11() {
    int operacao, x;
    char resposta;

    do {
        printf(
            "1 - Adição\n"
            "2 - Subtração\n"
            "3 - Multiplicação\n"
            "4 - Divisão\n"
            "5 - Sair\n"
            "Opção: ");
        scanf("%d", &operacao);

        if (operacao != 5) {
            printf("Número: ");
            scanf("%d", &x);

            switch (operacao) {
                case 1:
                    for (int i = 1; i <= 10; i++) {
                        printf("%d + %d = %d\n", x, i, x + i);
                    }

                    break;

                case 2:
                    for (int i = 0; i <= 10; i++) {
                        printf("%d - %d = %d\n", i + x, x, i);
                    }

                    break;

                case 3:
                    for (int i = 1; i <= 10; i++) {
                        printf("%d * %d = %d\n", x, i, x * i);
                    }

                    break;

                case 4:
                    for (int i = 1; i <= 10; i++) {
                        printf("%d / %d = %d\n", x * i, x, i);
                    }

                    break;

                default:
                    printf("Operação inválida");

                    break;
            }

            printf("Continuar? (s/n): ");
            scanf(" %c", &resposta);

            if (resposta == 'n' || resposta == 'N') break;
        }

        
    } while (operacao != 5);
}

void questao12() {
    int n, primo = 1; 
    
    printf("Número: ");
    scanf("%d", &n);

    if (n <= 1) primo = 0;

    else if (n == 2) primo = 1;

    else if (n % 2 == 0) primo = 0;

    else {
        for (int i = 3; i < n; i += 2) {
            if (n % i == 0) {
                primo = 0;
                break;
            }
        }
    }

    if (primo) printf("É primo");

    else printf("Não é primo");
}

void questao13() {
    double n; 
    double b = 2.0;
    double p;

    printf("Número: ");
    scanf("%lf", &n);

    while (fabs(b * b - n) > 0.0001) {
        p = (b + (n / b)) / 2;
        b = p;
    }

    printf("Raiz: %.4lf", b);
}

void questao14() {
    int n[2];

    for (int i = 0; i < 2; i++) {
        printf("Número %d: ", i + 1);
        scanf("%d", &n[i]);
    } 
    
    while (n[0] >= n[1]) n[0] -= n[1];

    printf("Resto: %d", n[0]);
}

void questao15() {
    int n = 0;

    printf("Número: ");
    scanf("%d", &n);

    int original = n;
    int reverso = 0;

    while (original != 0) {
        reverso = reverso * 10 + (original % 10);
        original /= 10;
    }

    if (n == reverso) printf("É um palindromo");

    else printf("Não é um palindromo");
}

int main() {
    #ifdef _WIN32
        SetConsoleCP(65001);
        SetConsoleOutputCP(65001);
    #else
        setlocale(LC_ALL, "");
    #endif

    questao11();

    return 0;
}
