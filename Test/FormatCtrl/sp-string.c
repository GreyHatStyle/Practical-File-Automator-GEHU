#include <stdio.h>

int main(){
    int n;
    printf("Enter no. of strings: ");
    scanf("%d",&n);

    char str[n][100];

    printf("Enter strings in line by line:\n");
    for(int i=0;i<n;i++){
        scanf(" %[^\n]s", str[i]);
    }

    printf("Your strings are: ");
    for(int i=0;i<n;i++){
        printf("%s \n", str[i]);
    }
}