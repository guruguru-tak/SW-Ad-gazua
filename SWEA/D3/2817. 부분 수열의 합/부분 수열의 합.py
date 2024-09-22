t = int(input())

def backtrack(start, current_sum):
    global result

    # 재귀 종료 조건 먼저 선언
    # k와 현재까지의 합이 같다면 결과값 1 더하고 함수 종료
    if current_sum == k:
        result += 1
        return
    # k 보다 현대까지의 합이 크다면 그냥 함수 종료
    if current_sum > k:
        result

    # i 는 n까지의 인덱스 숫자 넘버까지 반복
    for i in range(start, n):
        # 현재 i 선택시 다음 재귀 i+1 호출,
        # i + 1 = 다음 재귀 호출에서 숫자를 선택할 시작 인덱스를 지정합니다. 중복된 숫자를 선택하지 않고, 각 숫자를 한 번만 사용
        # current_sum + n_list[i] = 현재 선택한 숫자를 합
        # 이전의 sum 에서 현재의 리스트 인덱스 값만 계속해서 더한다
        # 예시)[1, 2, 3], k = 4이면 // 3번째까지 가서 [레벨 1: i = 0 이면 sum = 1], [레벨 2:i = 1 이면 sum = 1 + 2], [레벨 3: i = 2 이면 sum 1 + 2 + 3 = 6]로 k초과 조건 달성
        # k = 6 이기에 두 번째 레벨의 백트래킹으로 돌아감
        # 백트래킹 다시 되돌아가서 실패했던 [2번째 레벨에서 i = 1 에서 i = 2 로 sum = 4] 달성 result + 1 로 반환
        # 그리고 다시 마지막까지 돌았기에 [첫 번째 레벨로 돌아가서 최초 i = 1, sum = 2] 부터 시작, 레벨 2: [i = 2, sum = 2 + 3 = 5] k 초과 return
        # 모든 경우 다 돌았기에 return = 1만 나오게 된다
        backtrack(i+1, current_sum+n_list[i])
        # 백트래킹: 유효한 조합을 찾거나 더 이상 진행할 수 없을 때, 이전 단계로 돌아가서 다른 선택지를 시도.

for tc in range(1, t+1):
    n, k = map(int, input().split())
    # n 개의 자연수 수열 입력
    n_list = list(map(int , input().split()))

    result = 0
    # start: 현재 조합에서 선택할 시작 인덱스
    # current_sum: 현재까지 선택한 자연수의 합
    # count: 현재까지 선택한 자연수의 개수 (필요에 따라 사용할 수 있음)
    # 초기 호출 start = 리스트의 첫 번째 숫자, current_sum = 현재 숫자 합
    backtrack(0, 0)

    print(f"#{tc} {result}")
