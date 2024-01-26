#include <stdio.h>

int main(){
    int n,m;
    printf("Enter size of matrix: ");
    scanf("%d %d", &n, &m);
    
    int mat[n][m];
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            printf("Enter element: ");
            scanf("%d", &mat[i][j]);
        }
    }

    printf("\nYour matrix is: \n");
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
}