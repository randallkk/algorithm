// 오아시스 재결합 platinum 5
// https://www.acmicpc.net/problem/3015
// 23-09-02 100844 KB	624 ms

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ3015 {
    public static void main(String[] args) throws IOException {
        new BOJ3015().solution();
    }

    void solution() throws IOException {
//        0. input 받기
        long answer = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        /*
             tallest가 갱신되면 그 이전 사람들은 tallest보다 작은 사람은 볼 수 없음
                == 크거나 같은 사람은 볼 수 있음
                == tallest가 갱신되면, 이전의 tallest와 새 tallest 사이의 사람들을 싹 볼 수 있음
                    & 이전 tallest와 키가 같은 사람들도 볼 수 있음 (i - idx + dup)
         */
//        stack
        LinkedList<Integer> stack = new LinkedList<>();
        Map<Integer, Integer> duplicates = new HashMap<>();
        int height = Integer.parseInt(br.readLine());
        stack.add(height);
        duplicates.put(height, 0);
        for (int i = 1; i < N; i++) {
            height = Integer.parseInt(br.readLine());
            duplicates.computeIfPresent(height, (k,v) -> v + 1);
            duplicates.putIfAbsent(height, 0);
            while (!stack.isEmpty() && height > stack.getLast()) {
                duplicates.computeIfPresent(stack.getLast(), (k, v) -> null);
                stack.removeLast();
                answer ++;
            }
            if (!stack.isEmpty()) {
                if (height == stack.getLast()) {
//                        1. dup 이용하는 방법 -> 같은 키의 사람이 연속되지 않게 서있을 때 고려하지 못함
//                            a. 그냥
//                            b. 😊 dup을 map(duplicates)으로 만들자. height가 증가할 때 지금 height보다 작은 애들은 삭제하기
//                        2. 연속된 수가 끝날때까지 popLast 했다가 다시 집어넣기 -> 너무 여러번...... 최악의 경우 O(n^2)이라 시초 날거 같음
//                            a. for i 해서 뒤에서부터 수색 -> get(i) 할때마다 시간복잡도 +i : 시간초과
//                            b. 데코레이터 만들어서 for each 직접 구현해서 수색 -> 귀찮지만 O(1)으로 접근 ㄱㄴ : 역시 시간초과
                    answer += duplicates.get(height);
                    if (duplicates.get(height) != stack.size()) answer += 1;
                } else {    // height < stack.getLast()
                    answer++;
                }
            }
            stack.add(height);
        }

        System.out.println(answer);
    }
}
