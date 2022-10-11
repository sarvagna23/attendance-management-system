import java.util.*;
import java.util.HashMap;
import java.util.TreeMap;
import java.util.Map;

class Graph {

    
    class Edge {
        int s, d, w;

       
        Edge() {
            s = d = w = 0;
        }

        Edge(int s, int d, int w) {
            this.s = s;
            this.d = d;
            this.w = w;
        }
    }

    int V, E; // No. of vertices & edges

    Edge arr[]; //Array of objects of class Edge

    // Creating a graph with V vertices and E edges
    Graph(int v, int e) {
        V = v;
        E = e;
        arr = new Edge[e];

        // Creating objects 
        for (int i = 0; i < e; i++)
            arr[i] = new Edge();
    }

    void BellmanFord(Graph g, int s) {


        // Using hashmap to store vertex-dist pairs
        HashMap < Integer, Integer > map = new HashMap < Integer, Integer > (g.V);

        // Distance from source to all other verties as Infinity value
        for (int i = 0; i < g.E; i++) {
            map.put(g.arr[i].s, Integer.MAX_VALUE);
            map.put(g.arr[i].d, Integer.MAX_VALUE);
        }

      
        map.put(s, 0);

        // Relaxing edges |V| - 1 times
        for (int i = 1; i < g.V; i++) {
            for (int j = 0; j < g.E; j++) {
                // Get the edge data
                int u = g.arr[j].s;
                int v = g.arr[j].d;
                int w = g.arr[j].w;
                if (map.get(u) != Integer.MAX_VALUE && map.get(u) + w < map.get(v))
                    map.put(v, map.get(u) + w);
            }
        }

        
        TreeMap < Integer,Integer > sort = new TreeMap < > (map);

        for (Map.Entry < Integer,Integer > entry: sort.entrySet()) {
           
            if (entry.getKey() == s)
                continue;

            System.out.println(entry.getKey() + " " +
                // If the distance of vertex even after relaxing is infinity, print -1
                // Else print the value of the obtained distance 
                (entry.getValue() == Integer.MAX_VALUE ? -1 : entry.getValue()));

        }
        // Detecting negative cycle
        for (int j = 0; j < E; ++j) {
            int u = g.arr[j].s;
            int v = g.arr[j].d;
            int w = g.arr[j].w;
            if (map.get(u) != Integer.MAX_VALUE && map.get(u) + w < map.get(v)) {
                System.out.println("The Graph contains negative weight cycle.");
                return;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt(); // Number of testcases

        for (int i = 0; i < t; i++) {
            int V = sc.nextInt(); // Number of vertices
            int E = sc.nextInt(); //Number of edges

            Graph graph = new Graph(V, E);

          
            int src = sc.nextInt();
            graph.arr[0].s = src;
            graph.arr[0].d = sc.nextInt();
            graph.arr[0].w = sc.nextInt();

          
            for (int x = 1; x < E; x++) {
                graph.arr[x].s = sc.nextInt();
                graph.arr[x].d = sc.nextInt();
                graph.arr[x].w = sc.nextInt();
            }

            System.out.println();
            graph.BellmanFord(graph, src);
            System.out.println();
        }

        System.out.println();
        System.out.println("Exiting...");
        sc.close();

    }
}
