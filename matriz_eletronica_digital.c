#include <stdio.h>
#include <math.h>
/*Para compilar este programa corretamente,
você deve usar o -lm para garantir que o linker inclua a libm:
exemplo: gcc matriz_eletronica_digital.c -lm*/

int is_par(int numero) {
    if (numero % 2 == 0) {
        return 1;
    }
    else {
        return 0;
    }
}

int formula(int i, int j, int n) {
    double p;
    p = pow(2.0, n-j);
    double resultado = (i - 1) / p;

    if (is_par((int)floor(resultado))) {
        return 0;
    }
    else {
        return 1;
    }
}

int main() {
    int numero_variaveis, numero_colunas, numero_linhas, contador;
    contador = 0;
    scanf("%d", &numero_variaveis);

    numero_colunas = numero_variaveis;
    numero_linhas = (int) pow(2, numero_variaveis);
    int matriz[numero_linhas][numero_colunas];

    for (int i = 1; i <= numero_linhas; i++) {
        for (int j = 1; j <= numero_colunas; j++) {
            matriz[i][j] = formula(i, j, numero_variaveis);
        }
    }


    printf("\n");
    // mostrar matriz
    for (int i = 1; i <= numero_linhas; i++) {
        for (int j = 1; j <= numero_colunas; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }

}