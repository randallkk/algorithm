// 청소년 상어   gold 2
// https://www.acmicpc.net/problem/19236
// 24-03-10     17836 KB	212 ms

import java.util.ArrayList;
import java.util.Scanner;

public class BOJ19236 {
    public static void main(String[] args) {
        new BOJ19236().solution();
    }

    static int[] dr = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dc = {0, -1, -1, -1, 0, 1, 1, 1};
    static int answer = 0;
    static final int SHARK = -1;
    static final int EMPTY = 0;

    private void solution() {
        Scanner scanner = new Scanner(System.in);
        Fish[] fish = new Fish[17];
        int[][] status = new int[4][4];
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                int num = scanner.nextInt();
                int dir = scanner.nextInt()-1;
                fish[num] = new Fish(num, i, j, dir);
                status[i][j] = num;
            }
        }
        scanner.close();

        Fish firstEaten = fish[status[0][0]];
        Shark shark = new Shark(0, 0,firstEaten.dir, firstEaten.num);
        status[0][0] = SHARK;
        fish[firstEaten.num] = null;
        Space space = new Space(shark, fish, status);
        enterSpace(space);

        System.out.println(answer);
    }

    void enterSpace(Space space) {
        Shark shark = space.shark;

        Space nextLevel = moveFish(space);              // 물고기 움직이기
        Fish[] fish = nextLevel.fish;
        int[][] status = nextLevel.status;

        ArrayList<Integer> targets = shark.findTargets(status);

        if (targets.isEmpty()) {    // 상어가 움직일 수 없으면 탈출
            answer = Integer.max(shark.ate, answer);
            return;
        }

        for (int target : targets){

            Shark fullShark = shark.moveTo(fish[target]);   // 상어 움직이기
            status[shark.row][shark.col] = EMPTY;
            Fish eaten = fish[status[fullShark.row][fullShark.col]];    // 물고기 먹기
            fish[eaten.num] = null;
            status[fullShark.row][fullShark.col] = SHARK;
            nextLevel.shark = fullShark;

            enterSpace(nextLevel);

            status[shark.row][shark.col] = SHARK;           // 상어 원상복구
            status[fullShark.row][fullShark.col] = EMPTY;
            fish[eaten.num] = eaten;     // 먹힌 물고기 원상복구
            status[eaten.row][eaten.col] = eaten.num;
        }
    }

    Space moveFish(Space space) {
        Fish[] movedFish = space.copyFish();
        int[][] movedStatus = space.copyStatus();
        for (int i = 1; i < 17; i++) {
            Fish fish = movedFish[i];
            if (fish == null) {
                continue;
            }
            Fish moved = fish.move(movedStatus);
            if (movedStatus[moved.row][moved.col] == EMPTY) {   // 빈자리에 들어가는 경우
                movedStatus[fish.row][fish.col] = EMPTY;
            } else if (!fish.equals(moved)) {                   // 다른 물고기랑 자리를 바꾸는 경우
                Fish other = movedFish[movedStatus[moved.row][moved.col]];
                movedFish[other.num] = other.move(fish.row, fish.col);
                movedStatus[fish.row][fish.col] = other.num;
            }
            movedFish[moved.num] = moved;
            movedStatus[moved.row][moved.col] = moved.num;
        }
        return new Space(space.shark, movedFish, movedStatus);
    }

    static boolean isOut(int r, int c) {
        return r < 0 || r >= 4 || c < 0 || c >= 4;
    }

    static class Fish {
        int num;
        int row;
        int col;
        int dir;

        public Fish(int num, int row, int col, int dir) {
            this.num = num;
            this.row = row;
            this.col = col;
            this.dir = dir;
        }

        Fish move(int[][] status) {
            for (int i = 0; i < 7; i++) {
                int nd = (dir + i) % 8;
                int nr = row + dr[nd];
                int nc = col + dc[nd];
                if (isOut(nr, nc) || status[nr][nc] == SHARK) continue;
                return new Fish(num, nr, nc, nd);
            }
            return this;
        }

        Fish move(int r, int c) {
            return new Fish(num, r, c, dir);
        }
    }

    static class Shark {
        int row;
        int col;
        int dir;
        int ate;

        public Shark(int row, int col, int dir, int ate) {
            this.row = row;
            this.col = col;
            this.dir = dir;
            this.ate = ate;
        }

        Shark moveTo(Fish target) {
            return new Shark(target.row, target.col, target.dir, ate + target.num);
        }

        ArrayList<Integer> findTargets(int[][] space) {
            ArrayList<Integer> targets = new ArrayList<>(3);
            for (int i = 1; i <= 3; i++) {
                int nr = row + dr[dir] * i;
                int nc = col + dc[dir] * i;
                if (isOut(nr, nc)) break;
                if (space[nr][nc] == EMPTY) continue;
                targets.add(space[nr][nc]);
            }
            return targets;
        }
    }

    static class Space {
        Shark shark;
        Fish[] fish;
        int[][] status;

        public Space(Shark shark, Fish[] fish, int[][] status) {
            this.shark = shark;
            this.fish = fish;
            this.status = status;
        }

        int[][] copyStatus() {
            int[][] copied = new int[4][4];
            for (int i = 0; i < 4; i++) {
                System.arraycopy(status[i], 0, copied[i], 0, 4);
            }
            return copied;
        }

        Fish[] copyFish() {
            Fish[] copied = new Fish[17];
            System.arraycopy(fish, 0, copied, 0, 17);
            return copied;
        }
    }
}
