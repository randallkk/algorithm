// 보석 도둑 gold 2
// https://www.acmicpc.net/problem/1202
// priority queue   114064 KB	1580 ms

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ1202 {
    public static void main(String[] args) throws IOException {
        new BOJ1202().solution();
    }

    int N, K;
    int[][] jems;
    long[] bags;


    void solution() throws IOException {
//        0. input 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stk.nextToken());
        K = Integer.parseInt(stk.nextToken());
        jems = new int[N+1][2];
        bags = new long[K+1];
        for (int i = 1; i < N + 1; i++) {
            stk = new StringTokenizer(br.readLine());
            jems[i][0] = Integer.parseInt(stk.nextToken());
            jems[i][1] = Integer.parseInt(stk.nextToken());
        }
        for (int i = 1; i < K + 1; i++) {
            bags[i] = Integer.parseInt(br.readLine());
        }

//        1. 우선순위 큐
        priorityQueue();

    }

    /**
     * a. 냅색: 메모리 초과 -> 열받아서 분류 봄
     * @throws IOException
     */
    void knapsack() throws IOException {
        int[][] memo = new int[N+1][K+1];
        for (int i = 1; i < N+1; i++) {
            for (int j = 1; j < K+1; j++) {
                memo[i][j] = Math.max(memo[i-1][j-1]+jems[i][1], memo[i-1][j]);
            }
        }
        System.out.println(memo[N][K]);
    }

    /**
     * b. 우선순위 큐
     * @throws IOException
     */
    void priorityQueue() {
        Arrays.sort(jems, Comparator.comparingInt(arr -> arr[0]));
        Arrays.sort(bags);
        PriorityQueue<int[]> pq = new PriorityQueue<>((arr1, arr2) -> arr2[1] - arr1[1]);

        long answer = 0;
        int idx = 1;
        for(long bag: bags) {
            while (idx <= N && bag >= jems[idx][0]) {
                pq.offer(jems[idx]);
                idx++;
            }
            if (!pq.isEmpty()) {
                answer += pq.poll()[1];
            }
        }
        System.out.println(answer);
    }
}
