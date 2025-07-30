import java.io.*;
import java.util.*;

public class Main {
    static int N, M, U;
    static int[] uniq, pick;
    static StringBuilder sb = new StringBuilder();

    static void dfs(int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++) sb.append(pick[i]).append(' ');
            sb.append('\n');
            return;
        }
        for (int i = 0; i < U; i++) {
            pick[depth] = uniq[i];
            dfs(depth + 1);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(arr);

        uniq = new int[N];
        U = 0;
        for (int x : arr) if (U == 0 || uniq[U - 1] != x) uniq[U++] = x;

        pick = new int[M];
        dfs(0);
        System.out.print(sb);
    }
}