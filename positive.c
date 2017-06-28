#include<stdio.h>
#include<conio.h>
void main()
{
int n;
clrscr();
printf("\n enter a value");
scanf("%d",&n);
if(n>1)
printf("positive");
else if(n==0)
printf("0");
else
printf("negative");
getch();
}
