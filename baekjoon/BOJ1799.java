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
    List<Place> empty;
    int maxCnt = 0;

    void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        empty = new ArrayList<>(10);
        StringTokenizer stk;
        for (int i = 0; i < N; i++) {
            stk = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(stk.nextToken());
                if (board[i][j] == 1) empty.add(new Place(i, j));
            }
        }

//        1. dfs
        recursion(0, 0);
        System.out.println(maxCnt);
    }

//    recursion
    void recursion(int idx, int placed) {
        if (idx == empty.size()) {
            maxCnt = Math.max(maxCnt, placed);
            return;
        }
        if (placed + (empty.size() - idx - 1) <= maxCnt) {
            return;
        }
        if (isPlaceable(idx)) {
            Place place = empty.get(idx);
            board[place.r][place.c] = 0;
            recursion(idx + 1, placed + 1);
            board[place.r][place.c] = 1;
        }
        recursion(idx + 1, placed);
    }

//    bfs
    boolean isPlaceable(int idx) {
        int[] dr = {-1, -1, 1, 1};
        int[] dc = {-1, 1, -1, 1};
        int r = empty.get(idx).r;
        int c = empty.get(idx).c;
        int nr, nc;
        if (board[r][c] == 0) return false;
        else {
            for (int i = 0; i < 4; i++) {
                int nr, nc;
                while ()
            }
        }
    }

    class Place {
        int r;
        int c;

        Place(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
}
