import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 테스트 케이스 수

        for (int t = 1; t <= T; t++) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();

            int dx = Math.abs(x2 - x1);
            int dy = Math.abs(y2 - y1);

            // 두 점 사이의 x 차이와 y 차이 중 더 큰 값에 따라 최소 이동 횟수 계산
            int max = Math.max(dx, dy);
            int min = Math.min(dx, dy);

            // 홀짝 여부에 따라 최소 이동 횟수 결정
            int minMoves = max * 2 - (max % 2 != min % 2 ? 1 : 0);

            System.out.printf("#%d %d\n", t, minMoves);
        }
        sc.close();
    }
}