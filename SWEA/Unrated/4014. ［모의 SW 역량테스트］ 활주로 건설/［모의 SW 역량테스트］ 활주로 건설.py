t = int(input())

def check(road):
    global total_cnt

    visited = [False]*len(road)
    for i in range(1, len(road)):
        # dari_x -> 만큼 높이마다 길이 체크 필요 인덱스 초과면 버리고
        # 높이 같으면 컨티뉴
        if road[i-1] == road[i]: continue

        # 높이 다른것 중 -> 경사로 올라가는 것 -> 뒤의 길이가 dari_x만큼 가능한지 췍
        elif road[i-1] + 1 == road[i]:
            # 맨 처음 i-dari 가 -1로 (인덱스 수) 벽 넘어가면 끝
            if i - dari_x < 0: return
            for ch in range(i-dari_x, i):
                # 이미 경사로 쓰고 있는 지점이면 반대편에 경사로 설치 불가로 끝
                if visited[ch]: return
                # 위 조건 아니면 사용 가능하기에 방문처리
                visited[ch] = True
                # 경사로 세우기 길이 다르면 바로 끝
                if road[i-1] != road[ch]:
                    return
        # 높이 다른 것 중 -> 경사로 내려가는 것 -> 뒤의 길이가 dari_x만큼 가능한지 췍
        elif road[i-1] == road[i] + 1:
            # 뒤에 i + dari 가 (전체 길이 수)로 벽 넘어가면 끝
            if i + dari_x > len(road): return
            for ch in range(i, i + dari_x):
                # 이미 경사로 쓰고 있는 지점이면 반대편에 경사로 설치 불가로 끝
                if visited[ch]: return
                # 위 조건 아니면 사용 가능하기에 방문처리
                visited[ch] = True
                # 경사로 세우기 길이 다르면 바로 끝
                if road[i] != road[ch]:
                    return
        # 지대 +1 씩 차이 말고, +2 이상 씩 차이나는 땅 전부 끝
        else:
            return

    # for 문 다 돌고 전체 갯수 리턴해주기
    # print(road)
    total_cnt += 1

for tc in range(1, t+1):
    n, dari_x = map(int, input().split())

    land = [list(map(int, input().split())) for _ in range(n)]

    total_cnt = 0

    # 함수로 보낼 활주로 1차원 배열 생성
    # 가로 세로 -> 가로 세로 -> 가로 세로 이렇게 반복
    for i in range(n):
        # 2차원 배열 중 먼저 첫 가로 줄만 먼저 보냄
        road = land[i]
        # print(road)
        check(road)

        #2차원 배열 중 먼저 첫 세로 줄만 리스트로 만들어서 보냄
        road = [land[j][i] for j in range(n)]
        # print(road)
        check(road)

    print(f"#{tc} {total_cnt}")
