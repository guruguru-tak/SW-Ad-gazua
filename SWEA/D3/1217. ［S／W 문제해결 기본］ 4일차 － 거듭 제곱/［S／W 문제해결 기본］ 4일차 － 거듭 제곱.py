
t = 10

def powpow(exp):
    # print(exp)
    #종료 조건
    if exp == 1:
        # 반환할 값 n -> 처음 들어온 exp 까지 리턴 반복
        return n
    # n 에 반환받는 재귀함수 선언, 파라미터는 1씩 감소
    # 최종 exp 가 1이 되면 n*n -> n**n * n 다시 반대로 증가
    # 마지막 최종 n**exp 의 값이 리턴 값으로 나가게 됨
    return n*powpow(exp-1)

for tc in range(1, t+1):
    _ = input()
    n, e = map(int, input().split())

    print(f"#{tc} {powpow(e)}")