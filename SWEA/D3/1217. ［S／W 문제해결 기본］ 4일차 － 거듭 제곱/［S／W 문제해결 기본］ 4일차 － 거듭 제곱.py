t = 10
def powpow(n, exp):
    
    #종료 조건 exp가 1이면 2의 1승인 자기 자신 리턴
    if exp == 1:
        return n
    # exp -1 -> 하면 자기자신을 호출할 수록 8 7 6 5 4 로 줄어든다
    # for 문 쓸 필요 없음
    return n * powpow(n, exp-1)

for tc in range(1, t+1):
    _ = int(input())
    n, e = map(int, input().split())
    result = powpow(n, e)

    print(f"#{tc} {result}")
