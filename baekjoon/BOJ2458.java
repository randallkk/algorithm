// 키 순서 gold 4
// https://www.acmicpc.net/problem/2458
// 24-05-09 java 11	37396 KB	632 ms


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ2458 {
    public static void main(String[] args) throws IOException {
        new BOJ2458().solution();
    }

    private void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(stk.nextToken());
        int M = Integer.parseInt(stk.nextToken());
        int[][] relations = new int[N + 1][N + 1];
        for (int i = 0; i < M; i++) {
            stk = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(stk.nextToken());
            int b = Integer.parseInt(stk.nextToken());
            relations[a][b] = 1;
            relations[b][a] = -1;
        }

        for (int k = 1; k <= N; k++) {
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (relations[i][j] != 0) {
                    } else if (relations[i][k] + relations[k][j] == 2) {
                        relations[i][j] = 1;
                        relations[j][i] = -1;
                    } else if (relations[i][k] + relations[k][j] == -2) {
                        relations[i][j] = -1;
                        relations[j][i] = 1;
                    }
                }
            }
        }

        int answer = 0;
        for (int i = 1; i <= N; i++) {
            if (Arrays.stream(relations[i]).filter(value -> value == 0).count() == 2) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}
