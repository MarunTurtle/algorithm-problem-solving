import java.util.Scanner;

public class Main {
    static int N, M;
    static int[] result;
    static boolean[] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();  // 1부터 N까지
        M = sc.nextInt();  // M개 선택
        result = new int[M];
        visited = new boolean[N + 1]; // 인덱스 1부터 사용
        dfs(0);
    }

    static void dfs(int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                System.out.print(result[i] + " ");
            }
            System.out.println();
            return;
        }

        // 1부터 N까지 반복
        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                visited[i] = true;      // 방문 체크
                result[depth] = i;      // 현재 수열에 추가
                dfs(depth + 1);         // 다음 자리 탐색
                visited[i] = false;     // 백트래킹 (되돌리기)
            }
        }
    }
}
