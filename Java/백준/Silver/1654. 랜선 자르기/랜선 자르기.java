import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        long N = Long.parseLong(st.nextToken());

        long[] A = new long[K];
        long hi = 0;
        for (int i = 0; i < K; i++) {
            A[i] = Long.parseLong(br.readLine());
            if (A[i] > hi) hi = A[i];
        }

        long lo = 1, ans = 0;
        while (lo <= hi) {
            long mid = (lo + hi) >>> 1;
            long cnt = 0;
            for (long a : A) cnt += a / mid;

            if (cnt >= N) {   // 가능 → 더 길게
                ans = mid;
                lo = mid + 1;
            } else {          // 불가능 → 더 짧게
                hi = mid - 1;
            }
        }
        System.out.println(ans);
    }
}
