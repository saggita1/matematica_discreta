#include <stdio.h>
#define MAX 50

int main() {
    int m, soma = 0;

    int mat[MAX][MAX];
    scanf("%d", &m);

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &mat[i][j]);
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            soma += mat[i][j];
        }
    }
        

    printf("%d\n", soma);
}