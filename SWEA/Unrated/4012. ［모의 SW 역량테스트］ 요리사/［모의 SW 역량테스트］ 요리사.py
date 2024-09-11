from itertools import combinations

def matdori(case):

    result = 0
    # 테이블 안 테이블 인덱스 받아오면 그 값을 이용해서 
    # 모든 n//2 가지의 2차원 좌표로 다 더해서 그 맛 결과 보내줌
    # 사이 대각선은 인풋이 0이기에 다 더해도 상관 없음
    for y in case:
        for x in case:
            result += table[y][x]

    return result

t = int(input())
for tc in range(1, t+1):

    n = int(input())
    food = n//2

    table = [list(map(int, input().split())) for _ in range(n)]

    min_mat = 10**18
    for case in combinations([i for i in range(n)], food):
        #튜플에서 리스트로 변환
        case_A = list(case)
        case_B = list(i for i in range(n) if i not in case_A)

        mat_a = matdori(case_A)
        mat_b = matdori(case_B)

        min_mat = min(min_mat, abs(mat_a-mat_b))

    print(f"#{tc} {min_mat}")