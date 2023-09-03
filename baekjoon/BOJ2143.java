// 두 배열의 합 gold 3
// https://www.acmicpc.net/problem/2143
// 23-09-04

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ2143 {
    public static void main(String[] args) throws IOException {
        new BOJ2143().solution();
    }

    int T;
    long answer;
    void solution() throws IOException {
        answer = 0;
//        0. input 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        int[] arr1 = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int m = Integer.parseInt(br.readLine());
        int[] arr2 = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

//        1. 누적합 배열 만들기
        int[] prefixSum1 = new int[n];
        int[] prefixSum2 = new int[m];
        prefixSum1[0] = arr1[0];
        prefixSum2[0] = arr2[0];
        for (int i = 1; i < n; i++) {
            prefixSum1[i] = prefixSum1[i-1] + arr1[i];
        }
        for (int i = 1; i < m; i++) {
            prefixSum2[i] = prefixSum2[i-1] + arr2[i];
        }

//        2. 부 배열들의 합 구하기
        Map<Integer, Long> subArrSum1 = makeSubArrSum(n, prefixSum1);
        Map<Integer, Long> subArrSum2 = makeSubArrSum(m, prefixSum2);

//        3.
        for (int sum1 : subArrSum1.keySet()) {
            if (subArrSum2.containsKey(T - sum1)) {
                answer += subArrSum1.get(sum1) * subArrSum2.get(T - sum1);
            }
        }

        System.out.println(answer);
    }

    private Map<Integer, Long> makeSubArrSum(int m, int[] prefixSum) {
        Map<Integer, Long> subArrSum = new TreeMap<>();
        for (int i = 0; i < m; i++) {
            subArrSum.computeIfPresent(prefixSum[i], (k, v) -> v + 1);
            subArrSum.putIfAbsent(prefixSum[i], 1L);
            for (int j = 0; j < i; j++) {
                int subSum = prefixSum[i] - prefixSum[j];
                subArrSum.computeIfPresent(subSum, (k, v) -> v + 1);
                subArrSum.putIfAbsent(subSum, 1L);
            }
        }
        return subArrSum;
    }
}
