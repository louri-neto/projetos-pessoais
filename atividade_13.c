#include <stdio.h>

#ifdef _WIN32
    #include <windows.h>
#else
    #include <locale.h>
#endif

void questao11() {
    int operacao, x;
    char resposta;

    do {
        printf("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair\nOpção: ");
        scanf("%d", &operacao);

        if (operacao >= 1 && operacao <= 4) {
            printf("Número: ");
            scanf("%d", &x);

            switch (operacao) {
                case 1:
                    for (int i = 1; i <= 10; i++) {
                        printf("%d + %d = %d\n", x, i, x + i);
                    }

                    break;

                case 2:
                    for (int i = 1; i <= 10; i++) {
                        printf("%d - %d = %d\n", i, x, i - x);
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

void questao14() {
    int n[2];

    for (int i = 0; i < 2; i++) {
        printf("Número %d: ", i + 1);
        scanf("%d", &n[i]);
    } 
    
    while (n[0] >= n[1]) n[0]-=n[1];

    printf("Resto: %d", n[0]);
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
