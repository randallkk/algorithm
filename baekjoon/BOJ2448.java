// 별 찍기 - 11    gold 4
// https://www.acmicpc.net/submit/2448
// 24-05-02    java 11  122896 KB	500 ms

import java.util.Arrays;
import java.util.Scanner;

public class BOJ2448 {
    public static void main(String[] args) {
        new BOJ2448().solution();
    }

    char[][] star;
    int N;

    private void solution() {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        star = new char[N][N * 2];
        for (int i = 0; i < N; i++) {
            Arrays.fill(star[i], ' ');
        }
        drawTree(0, N, N);
        StringBuilder sb = new StringBuilder();
        for (char[] chars : star) {
            sb.append(chars).append('\n');
        }
        System.out.println(sb);
    }

    void drawTree(int top, int center, int size) {
        if (size == 3) {
            drawUnit(top, center - 3);
            return;
        }
        drawTree(top, center, size / 2);
        drawTree(top + size / 2, center - size / 2, size / 2);
        drawTree(top + size / 2, center + size / 2, size / 2);
    }

    void drawUnit(int top, int left) {
//        star[top][left+2] = '*';
//        for (int i = left+1; i < left+5; i+=2) {
//            star[top+1][i] = '*';
//        }
//        for (int i = left; i < left+5; i++) {
//            star[top+2][i] = '*';
//        }
        for (int i = 0; i < 3; i++) {
            for (int j = left + 2 - i; j < left + 5; j += 3 - i) {
                star[top + i][j] = '*';
            }
        }
    }
}
