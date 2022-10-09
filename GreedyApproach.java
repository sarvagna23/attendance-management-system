public class Main {
static int capacity=25;
static void sort(int[] value,int[] weights,double[] ratio){
int n = ratio.length;
// One by one move boundary of unsorted subarray
for (int i = 0; i < n-1; i++)
{
// Find the minimum element in unsorted array
int max_idx = i;

for (int j = i+1; j < n; j++)
if (ratio[j] > ratio[max_idx])
max_idx = j;
// Swap the found minimum element with the first
// element

int temp1=value[max_idx];
value[max_idx] = value[i];
value[i] = temp1;
temp1=weights[max_idx];
weights[max_idx] = weights[i];
weights[i] = temp1;
}
System.out.println("Sorted\t\tSorted\t\tSorted");
System.out.println("Value\t\tWeight\t\tRatio");
for(int i=0;i<10;i++)
{
System.out.println(value[i]+"\t\t\t"+weights[i]+
"\t\t\t"+ratio[i]);
}
double total_value=0.0;
int index=0;
System.out.println("\n\nCurrent\t\tCorresponding\tCurrent");
System.out.println("Value\t\tWeight\t\t\tKnapsack Capacity");
//adding the best possible values in the knapsack
while(capacity-weights[index]>0){
capacity-=weights[index];
total_value+=value[index];
System.out.println(value[index]+"\t\t\t"+weights[index]+
"\t\t\t\t"+capacity);
index++;
}
//adding fractional val into the knapsack
if(capacity>0){
System.out.println("Current Value = Current sum + Value for fractional capacity");
System.out.println("Current Value = "+total_value+" + "+

capacity+" x "+ratio[index]);
total_value+=capacity*ratio[index];
}
System.out.println("\nFinal Total Value: "+total_value);
}
public static void main(String args[]) {
int[] val= new int[10];
int[] weight= new int[10];
double[] ratio = new double[10];
int r=17;
for(int i=0;i<10;i++){
val[i]=r +((r+1)*i);
weight[i]=(r+i)%10;
if(weight[i]==0)
weight[i]=(int)(Math.random()*10);
ratio[i]=(double)val[i]/(double)weight[i];
}
System.out.println("Value\tWeight\tRatio");
for(int i=0;i<10;i++)
{
System.out.println(val[i]+"\t\t\t"+weight[i]+"\t"+ratio[i]);
}
System.out.println("\n");
sort(val,weight,ratio);
}
}
