#include<stdio.h>
int main(){
    int num1,num2,num3;
    printf("First value:");
    scanf("%d",&num1);
    printf("Second value:");
    scanf("%d",&num2);
    printf("Third value:");
    scanf("%d",&num3);

    if(num1>num2 && num1>num3){
        printf("%d is largest value",num1);
    }else if(num2>num1 && num2>num3){
        printf("%d is largest value",num2);
    }else if(num3>num1 && num3>num2){
        printf("%d is largest value",num3);
    }else{
        printf("invalid inputs");
    }
}