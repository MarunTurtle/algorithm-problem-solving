import java.io.*;
import java.util.*;

public class Main {

    // 8 가지 나이트 이동 벡터
    private static final int[] dx = {-2, -2, -1, -1, 1, 1, 2, 2};
    private static final int[] dy = {-1,  1, -2,  2,-2, 2,-1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb  = new StringBuilder();

        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {

            int l = Integer.parseInt(br.readLine().trim());

            // 시작 좌표
            StringTokenizer st = new StringTokenizer(br.readLine());
            int sx = Integer.parseInt(st.nextToken());
            int sy = Integer.parseInt(st.nextToken());

            // 목표 좌표
            st = new StringTokenizer(br.readLine());
            int tx = Integer.parseInt(st.nextToken());
            int ty = Integer.parseInt(st.nextToken());

            // 시작과 목적지가 같으면 0
            if (sx == tx && sy == ty) {
                sb.append(0).append('\n');
                continue;
            }

            // 방문 배열: -1 이면 미방문
            int[][] dist = new int[l][l];
            for (int[] row : dist) Arrays.fill(row, -1);

            // BFS 큐 (ArrayDeque > LinkedList : 더 빠름)
            ArrayDeque<int[]> q = new ArrayDeque<>();
            q.add(new int[]{sx, sy});
            dist[sx][sy] = 0;

            // BFS
            while (!q.isEmpty()) {
                int[] cur = q.poll();
                int x = cur[0], y = cur[1];

                for (int dir = 0; dir < 8; dir++) {
                    int nx = x + dx[dir];
                    int ny = y + dy[dir];

                    // 범위 밖이거나 이미 방문했다면 skip
                    if (nx < 0 || nx >= l || ny < 0 || ny >= l || dist[nx][ny] != -1)
                        continue;

                    dist[nx][ny] = dist[x][y] + 1;

                    if (nx == tx && ny == ty) {      // 목표 도달 → 종료
                        q.clear();
                        break;
                    }
                    q.add(new int[]{nx, ny});
                }
            }
            sb.append(dist[tx][ty]).append('\n');
        }
        System.out.print(sb);
    }
}
