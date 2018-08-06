class Palindrome
{
public static void main(String args[])
{
int a,b=0,c;
int n=121;
c=n;
while(n>0)
{
a=n%10;
b=(b*10)+a;
n=n/10;
}
if(c==b)
{
System.out.println("yes");
}
else
{
System.out.println("no");
}
}
}
