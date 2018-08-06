class Prime
{
public static void main(String args[])
{
int i,a=0,b=0,n=11;
a=n/2;
if(n==0||n==1)
{
System.out.println(n+"yes");
}
else
{  
for(i=2;i<=a;i++)
{      
if(n%i==0){      
System.out.println(n+" no");      
b=1;      
}      
}      
if(b==0) 
{ 
System.out.println(n+" yes"); 
}  
}
}    
}   
