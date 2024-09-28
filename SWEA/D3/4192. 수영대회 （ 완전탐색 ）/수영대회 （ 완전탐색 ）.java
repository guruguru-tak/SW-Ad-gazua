import java.util.*;

public class Solution {

    // BFS 함수 정의
    public static int bfs(int yStart, int xStart, int yEnd, int xEnd, int n, int[][] grid) {
        // 방향 벡터 (상, 하, 좌, 우)
        int[] dx = {1, 0, 0, -1};
        int[] dy = {0, 1, -1, 0};

        // 방문 여부 확인 배열
        boolean[][] visited = new boolean[n][n];

        // 큐 초기화 (y좌표, x좌표, 시간)
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {yStart, xStart, 0});
        visited[yStart][xStart] = true;

        // BFS 탐색
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int y = current[0];
            int x = current[1];
            int time = current[2];

            // 도착점에 도달하면 시간을 반환
            if (y == yEnd && x == xEnd) {
                return time;
            }

            // 네 방향으로 이동
            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];

                // 그리드 범위를 벗어나지 않고 방문하지 않았으며 장애물이 없는 경우
                if (ny >= 0 && ny < n && nx >= 0 && nx < n && !visited[ny][nx] && grid[ny][nx] == 0) {
                    visited[ny][nx] = true;
                    q.offer(new int[] {ny, nx, time + 1});
                }
            }
        }

        // 도달할 수 없으면 -1 반환
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 테스트 케이스 수 입력
        int t = sc.nextInt();

        for (int tc = 1; tc <= t; tc++) {
            // 그리드 크기 입력
            int n = sc.nextInt();
            int[][] grid = new int[n][n];

            // 그리드 데이터 입력
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    grid[i][j] = sc.nextInt();
                }
            }

            // 시작점과 도착점 입력
            int yStart = sc.nextInt();
            int xStart = sc.nextInt();
            int yEnd = sc.nextInt();
            int xEnd = sc.nextInt();

            // BFS 실행 및 결과 출력
            int result = bfs(yStart, xStart, yEnd, xEnd, n, grid);
            System.out.println("#" + tc + " " + result);
        }

        sc.close();
    }
}
