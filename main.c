
#include<stdio.h>  
int main()    
{    
  int n,rem,sum=0,temp;    
  printf("Enter a number to cheack for Armstrong Number = ");    
  scanf("%d",&n);    
  temp=n;    
  while(n>0)    
  {    
    r=n%10;    
    sum=sum+(r*r*r);    
    n=n/10;    
  }    
  if(temp==sum)    
  printf("\n%d is an Armstrong Number.",temp);    
  else    
  printf("\n%d is not an Armstrong Number.",temp);    
  return 0;  
}   
