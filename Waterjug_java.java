import java.util.*;

class Exp1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter X : ");
        int x = sc.nextInt();
        System.out.print("Enter Y : ");
        int y = sc.nextInt();

        int[] jug1 = new int[100];
        int[] jug2 = new int[100];

        int j = 0;
        jug1[j] = 0;
        jug2[j] = 0;

        j++;
        jug1[j] = 0;
        jug2[j] = 3;

        j++;

        if ((jug1[j - 1] + jug2[j - 1] <= 4) && jug2[j - 1] > 0) {
            jug1[j] = jug1[j - 1] + jug2[j - 1];
            jug2[j] = 0;
        }
        j++;

        if (jug2[j - 1] < y) {
            jug1[j] = jug1[j-1];
            jug2[j] = y;
        }

        j++;

        if ((jug1[j - 1] + jug2[j - 1] >= 4) && jug2[j - 1] > 0) {
            jug1[j] = x;
            jug2[j] = jug2[j - 1] - (x - jug1[j - 1]);
        }

   
        for (int i = 0; i <= j; i++) {
            System.out.print(jug1[i] + " ");
            System.out.print(jug2[i]);
            System.out.println("\n");
        }
        sc.close();
    }
}
