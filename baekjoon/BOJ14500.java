// 테트로미노    gold 4
// https://www.acmicpc.net/problem/14500
// 24-05-03    java 11    33056 KB	504 ms

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14500 {
    public static void main(String[] args) throws IOException {
        new BOJ14500().solution();
    }

    static int N, M;
    static int[][] paper;
    static int answer = 0;

    private void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stk.nextToken());
        M = Integer.parseInt(stk.nextToken());
        paper = new int[N][M];
        for (int i = 0; i < N; i++) {
            stk = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                paper[i][j] = Integer.parseInt(stk.nextToken());
            }
        }

        simulate2Vert();
        simulate2Hori();
        simulate3Vert();
        simulate3Hori();

        System.out.println(answer);
    }

    private static void simulate2Vert() {
        int[] di = {0, 1, 1};
        int[] dj = {-1, -1, 1};
        int[][] vert2Sum = new int[N][M];
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < M; j++) {
                vert2Sum[i][j] = paper[i - 1][j] + paper[i][j];
            }
        }

        for (int i = 1; i < N; i++) {
            for (int j = 0; j < M; j++) {
                for (int d = 0; d < 3; d++) {
                    int ni = i + di[d];
                    int nj = j + dj[d];
                    if (isOut(ni, nj)) {
                        continue;
                    }
                    answer = Math.max(answer, vert2Sum[i][j] + vert2Sum[ni][nj]);
                }
            }
        }
    }

    private static void simulate2Hori() {
        int[] dj = {1, 1};
        int[] di = {-1, 1};
        int[][] hori2Sum = new int[N][M];
        for (int j = 1; j < M; j++) {
            for (int i = 0; i < N; i++) {
                hori2Sum[i][j] = paper[i][j - 1] + paper[i][j];
            }
        }

        for (int j = 1; j < M - 1; j++) {
            for (int i = 0; i < N; i++) {
                for (int d = 0; d < 2; d++) {
                    int ni = i + di[d];
                    int nj = j + dj[d];
                    if (isOut(ni, nj)) {
                        continue;
                    }
                    answer = Math.max(answer, hori2Sum[i][j] + hori2Sum[ni][nj]);
                }
            }
        }
    }

    private static void simulate3Vert() {
        int[] di = {0, -1, -1, -1, 1, 1, 1};
        int[] dj = {1, -2, -1, 0, -2, -1, 0};
        for (int i = 0; i < N; i++) {
            int base = paper[i][0] + paper[i][1];
            for (int j = 2; j < M; j++) {
                base += paper[i][j];
                simulate1(di, dj, base, i, j);
                base -= paper[i][j - 2];
            }
        }
    }

    private static void simulate3Hori() {
        int[] dj = {0, -1, -1, -1, 1, 1, 1};
        int[] di = {1, -2, -1, 0, -2, -1, 0};
        for (int j = 0; j < M; j++) {
            int base = paper[0][j] + paper[1][j];
            for (int i = 2; i < N; i++) {
                base += paper[i][j];
                simulate1(di, dj, base, i, j);
                base -= paper[i - 2][j];
            }
        }
    }

    private static void simulate1(int[] di, int[] dj, int base, int i, int j) {
        for (int d = 0; d < 7; d++) {
            int ni = i + di[d];
            int nj = j + dj[d];
            if (isOut(ni, nj)) {
                continue;
            }
            answer = Math.max(answer, base + paper[ni][nj]);
        }
    }

    private static boolean isOut(int r, int c) {
        return r < 0 || r >= N || c < 0 || c >= M;
    }
}
