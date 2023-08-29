// 비숍 gold 1
// https://www.acmicpc.net/problem/1799

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ1799 {
    public static void main(String[] args) throws IOException {
        new BOJ1799().solution();
    }

    int N;
    int[][] board;
    List<Place>[] empty;
    int maxCnt = 0;
    boolean[] positive, negative;

    void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        empty = new List[2 * N - 1];
        for (int i = 0; i < 2 * N - 1; i++) {
            empty[i] = new ArrayList<Place>();
        }
        StringTokenizer stk;
        for (int i = 0; i < N; i++) {
            stk = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(stk.nextToken());
                if (board[i][j] == 1) empty[i+j].add(new Place(i, j));
            }
        }

//        a. 재귀 + bfs
//        recursiveBfs(0, 0);

//        b. N-Queen처럼 풀어보자
//          -1. 비숍을 놓을 수 있는 자리를 기준으로 재귀 -> 2^(빈자리 수), 최악: 2^100 = 시간초과
//          -2. 대각선 한 쪽을 기준으로 재귀 -> 생각해보니까 똑같음. 근데 positive[idx]가 프루닝이 많이 되는 것 같다.
        positive = new boolean[2 * N - 1];    // 우상향. r+c를 index로 가짐 (r+c가 같으면 같은 우상향 대각선에 존재)
        negative = new boolean[2 * N - 1];    // 우하향. r-c+4를 index로 가짐
        likeNQueen(0, 0);

        System.out.println(maxCnt);
    }

    void likeNQueen(int idx, int placed) {
        if (idx >= 2 * N - 1 || positive[idx] || placed + 2 * N - 1 - idx <= maxCnt) {
            maxCnt = Math.max(maxCnt, placed);
            return;
        }
        likeNQueen(idx + 1, placed);
        for (Place place : empty[idx]) {
            int r = place.r;
            int c = place.c;
            if (isPlaceableIdx(r, c)) {
                positive[r+c] = true;
                negative[r-c + N-1] = true;
                maxCnt = Math.max(maxCnt, placed);
                likeNQueen(idx + 1, placed + 1);
                positive[r+c] = false;
                negative[r-c + N-1] = false;
            }
        }
    }

    boolean isPlaceableIdx(int r, int c) {
        if (board[r][c] == 0) return false;
        if (positive[r+c]) return false;
        if (negative[r-c+N-1]) return false;
        return true;
    }

/*  a. 재귀 + bfs

    void recursiveBfs(int idx, int placed) {
        if (idx == empty.size()) {
            maxCnt = Math.max(maxCnt, placed);
            return;
        }
        if (placed + (empty.size() - idx - 1) <= maxCnt) {
            return;
        }
        if (isPlaceableBfs(idx)) {
            Place place = empty.get(idx);
            board[place.r][place.c] = -1;
            recursiveBfs(idx + 1, placed + 1);
            board[place.r][place.c] = 1;
        }
        recursiveBfs(idx + 1, placed);
    }

//    bfs
    boolean isPlaceableBfs(int idx) {
        int[] dr = {-1, -1, 1, 1};
        int[] dc = {-1, 1, -1, 1};
        int r = empty.get(idx).r;
        int c = empty.get(idx).c;
        if (board[r][c] == 0) return false;
        else {
            int nr, nc;
            for (int i = 0; i < 4; i++) {
                nr = r + dr[i];
                nc = c + dc[i];
                while (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                    if (board[nr][nc] == -1) return false;
                    else {
                        nr += dr[i];
                        nc += dc[i];
                    }
                }
            }
            return true;
        }
    }

 */

    class Place {
        int r;
        int c;

        Place(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
}
