import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] req = new long[N];
        long maxReq = 0;
        for (int i = 0; i < N; i++) {
            req[i] = Long.parseLong(st.nextToken());
            if (req[i] > maxReq) maxReq = req[i];
        }
        long M = Long.parseLong(br.readLine().trim());

        long low = 0, high = maxReq, answer = 0;
        while (low <= high) {
            long mid = (low + high) / 2;
            long sum = 0;
            for (long r : req) {
                sum += Math.min(r, mid);
                if (sum > M) break;
            }
            if (sum <= M) {
                answer = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        System.out.println(answer);
    }
}
