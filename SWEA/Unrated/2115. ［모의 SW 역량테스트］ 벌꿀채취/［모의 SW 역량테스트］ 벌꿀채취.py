from itertools import combinations
t = int(input())

# 수 제한치 확인, 최대값 구하기
# combinations으로 각 꿀통 받아서
# 그 꿀통의 리밋보다 작은 것 중에 가장 큰 것 보내기
def max_work(compare):
    total_tong = 0
    # 벌통 길이가 몇인지 모르기에 -> 각 길이 수만큼 뽑아서 각 조합 구함
    for i in range(1, len(compare)+1):
        # 각 길이만큼 각 조합 구함
        for tong_su in combinations(compare, i):
            # 뽑은 통수 리스트로 바꿈
            tong_su = list(tong_su)
            # 리스트로 바꿔서 sum 사용가능, sum 통수 -> 리밋보다 크면 넘어가기
            if sum(tong_su) > cnt_limit:
                continue
            # 전체 통수를 비교함 -> i*i == i**2 해서 i 각 수를 통수에서 꺼내 sum 반복
            total_tong = max(total_tong, sum([i * i for i in tong_su]))

    return total_tong

# 해당 인덱스 내 벌통 수치만 보내기
def create_honey(h, y, x):
    global max_print

    max_bee2 = 0
    max_bee1 = 0

    #방문 배열 선언
    visited = [[False]*n for _ in range(n)]
    for i in range(tong_limit):
        visited[y][x+i] = True

    #1번 벌 최대값 작업
    max_bee1 = max_work(h)

    #벌 2 작업 시작
    for y in range(n):
        for x in range(n-tong_limit+1):
            #중복 제외 조건 추가 / 통_리밋 사이즈 받음
            # / any -> 최소 하나만 True면 넘겨라
            if not any(visited[y][x:x+tong_limit]):
                max_bee2 = max(max_bee2, max_work(grid[y][x:x+tong_limit]))

    # 글로벌이라서 return 필요 없음
    max_print = max(max_bee1+max_bee2, max_print)


for tc in range(1, t+1):
    n, tong_limit, cnt_limit = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # 두 벌꿀의 최대치 합 변수
    max_print = 0


    #벌 1 선택
    for y in range(n):
        for x in range(n-tong_limit+1):
            # 리스트 파싱하기 , 이미 파싱한 통_리밋 사이즈 보냄
            create_honey(grid[y][x:x+tong_limit], y, x)

    print(f"#{tc} {max_print}")






