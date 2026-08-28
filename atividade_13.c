#include <stdio.h>

#ifdef _WIN32
    #include <windows.h>
#else
    #include <locale.h>
#endif

void questao11() {
    char operacao;

    printf("Operações\n+ - Adição\n- - Subtração\n* - Multiplicação\n/ - Divisão\nOpção: ");
    scanf(" %c", operacao);

    
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
