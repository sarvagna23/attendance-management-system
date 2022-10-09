import java.util.*;
public class Main
{
    public static void reset()
   
    }
    public static void display()
    {
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                System.out.print(visited[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static boolean possible(int i,int j)
    {
        if(i>=0 && j>=0 && i<m && j<n && maze[i][j]!=1 && visited[i][j]<2 && main_visited[i][j]!=1)
        {
            return true;
        }
        return false;
    }
    public static int calculate_h(Node curr)
    {
        return (int)Math.pow(dest.posi-curr.posi,2)+(int)Math.pow(dest.posj-curr.posj,2);
    }
    public static Node search(Node n,int g,int fbound)
    {
        counter++;
        int i=n.posi,j=n.posj;
        int hval=calculate_h(n);
        //System.out.println(i+" "+j+"\n");
        int fval=g+hval;
        n.f=fval;
        n.g=g;
        n.h=hval;
        if((fval>fbound) || (n.posi==dest.posi && n.posj==dest.posj))
        {
            return n;
        }
        int min=Integer.MAX_VALUE;
        PriorityQueue<Node> list=nextNode(n);
        //Iterator val= list.iterator();
        while(!list.isEmpty())//(Node element: list)
        {
            //Node neighbour=element;
            Node neighbour=list.poll();
            main_visited[n.posi][n.posj]=1;

            neighbour.parent_i=n.posi;
            neighbour.parent_j=n.posj;
            //System.out.println(neighbour.posi+" "+neighbour.posj);
            Node temp=search(neighbour,g+1,fbound);
            if(temp.posi==dest.posi && temp.posj==dest.posj)
            {
                return temp;
            }
            if(temp.f<min)
            {
                min=temp.f;
                i=temp.posi;
                j=temp.posj;
            }
        }
        return nodeDetails[i][j];
    }
    public static PriorityQueue<Node> nextNode(Node curr)
    {
        int i=curr.posi;
        int j=curr.posj;
        PriorityQueue<Node> list = new PriorityQueue<Node>(new Node(0,0));
       
        
        if(possible(i-1,j)==true)
        {
            list.add(nodeDetails[i-1][j]);
            visited[i-1][j]++;
        }
       
        
        if(possible(i-1,j-1)==true)
        {
            list.add(nodeDetails[i-1][j-1]);
            visited[i-1][j-1]++;
        }
       
        
        if(possible(i,j-1)==true)
        {
            list.add(nodeDetails[i][j-1]);
            visited[i][j-1]++;
        }
       
        
        if(possible(i+1,j-1)==true)
        {
            list.add(nodeDetails[i+1][j-1]);
            visited[i+1][j-1]++;
        }
       
        
        if(possible(i+1,j)==true)
        {
            list.add(nodeDetails[i+1][j]);
            visited[i+1][j]++;
        }
       
        
        if(possible(i+1,j+1)==true)
        {
            list.add(nodeDetails[i+1][j+1]);
            visited[i+1][j+1]++;
        }
       
        
        if(possible(i,j+1)==true)
        {
            list.add(nodeDetails[i][j+1]);
            visited[i][j+1]++;
        }
       
        
        if(possible(i-1,j+1)==true)
        {
            list.add(nodeDetails[i-1][j+1]);
            visited[i-1][j+1]++;
        }
       
        return list;
    }
    public static void path(){
        System.out.println("The path of the Maze is ");
        int row = dest.posi;
        int col = dest.posj;
        //System.out.println("");
        Stack<Node> s = new Stack<Node>();
        while(!(nodeDetails[row][col].parent_i==row && nodeDetails[row][col].parent_j==col)){
            s.push(new Node(row,col));
            int temp_row = nodeDetails[row][col].parent_i;
            int temp_col = nodeDetails[row][col].parent_j;
            row = temp_row;
            col = temp_col;
        }
        s.push(new Node(row,col));
        while(!s.empty()){
            Node p = s.pop();
            System.out.print(" -> "+p.posi+","+p.posj);
        }
        System.out.println();
    }
    public static void IDAstar(Node start)
    {
        int fbound=start.f,limit=10;
        while(true)
        {
            Node temp=search(start,0,fbound);
            if(temp.posi==dest.posi && temp.posj==dest.posj)
            {
                System.out.println("End Point Found");
                path();
                break;
            }
            if(counter>limit)
            {
                System.out.println("Path Not Found");
                break;
            }
            fbound=temp.f;
            //counter++;
            //System.out.println(counter);
        }
        display();
    }
    public static int[][] maze = {{0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                                  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
                                  {0, 0, 0, 0, 1, 0, 0, 0, 0, 0}};
    public static int m=maze.length;
    public static int n=maze[0].length;
    public static Node[][] nodeDetails =new Node[m][n];
    public static int[][] visited=new int[m][n];
    public static int[][] main_visited=new int[m][n];
    public static Node dest=new Node(4,5);
    public static int counter=0;
public static void main(String[] args) {
int i,j,temp_i,temp_j;
for(i=0;i<m;i++)
{
   for(j=0;j<n;j++)
   {
       nodeDetails[i][j]=new Node(i,j);
   }
}
Node start=new Node(0,0,0);
start.posi=0;
start.posj=0;
start.parent_i=start.posi;
start.parent_j=start.posj;
IDAstar(start);
}
}
class Node implements Comparator<Node>
{
    int f,g,h,parent_i,parent_j,posi,posj;
    Node(int f,int g,int h)
    {
        this.f=f;
        this.g=g;
        this.h=h;
    }
    Node(int posi,int posj)
    {
        this.posi=posi;
        this.posj=posj;
    }
    public int compare(Node n1,Node n2)
    {
        if(n1.f>n2.f)
        {
            return -1;
        }
        else if(n1.f<n2.f)
        {
            return 1;
        }
        return 0;
    }
}
