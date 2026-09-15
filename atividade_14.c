#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#ifdef _WIN32
    #include <windows.h>
#else
    #include <locale.h>
#endif

int findchar(const char *s, char c, int p) {
    for (int i = p; i < strlen(s); i++) if (s[i] == c) return i;

    return -1;
}

void questao1() {
    char s[32], c;
    unsigned int p;

    printf("String: ");
    fgets(s, sizeof(s), stdin);

    printf("Caractere: ");
    scanf(" %c", &c);

    printf("Posição: ");
    scanf("%u", &p);

    if (findchar(s, c, p) != -1) printf("Caractere encontrado\n");

    else printf("Caractere não encontrado\n");
}

void questao2() {
    char data[11];
    int dia, mes, ano;

    printf("Data (DD/MM/AAAA): ");
    fgets(data, sizeof(data), stdin);

    if (strlen(data) != 10) {
        printf("A string deve ter 10 caracteres");
        return;
    }

    if (data[2] != '/' && data[5] != '/') {
        printf("Sem barras ou barras em posições erradas");
        return;
    }

    for (int i = 0; i < 10; i++) {
        if (i == 2 || i == 5) continue;

        if (!isdigit(data[i])){
            printf("A string não deve conter letras, símbolos (a não ser o /) ou espaços");
            return;
        }
    }

    sscanf(data, "%d/%d/%d", &dia, &mes, &ano);

    printf("Dia: %d\nMês: %d\nAno: %d\n", dia, mes, ano);
}

void questao3() {
    char frase[128], semEspaco[128];
    int j = 0;

    printf("Frase: ");
    fgets(frase, sizeof(frase), stdin);

    for (int i = 0; frase[i] != '\0'; i++) {
        if (frase[i] != ' ') {
            semEspaco[j] = frase[i];
            j++;
        }
    }

    semEspaco[j] = '\0';

    printf("Frase sem espaços: %s\n", semEspaco);
}

int main() {
    #ifdef _WIN32
        SetConsoleCP(65001);
        SetConsoleOutputCP(65001);
    #else
        setlocale(LC_ALL, "");
    #endif

    questao3();

    return 0;
}