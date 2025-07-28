import java.util.*;

public class Main {
    static int N, M;
    static int[] numbers;
    static int[] output;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        numbers = new int[N];
        output = new int[M];

        for (int i = 0; i < N; i++) {
            numbers[i] = sc.nextInt();
        }

        Arrays.sort(numbers);  
        dfs(0, 0);             
    }

    static void dfs(int depth, int start) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                System.out.print(output[i] + " ");
            }
            System.out.println();
            return;
        }

        for (int i = start; i < N; i++) {
            output[depth] = numbers[i];
            dfs(depth + 1, i + 1); 
        }
    }
}
