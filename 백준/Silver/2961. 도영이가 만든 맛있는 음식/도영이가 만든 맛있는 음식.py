n = int(input())
ingredients = []
ans = []
result = [] # 정답 담을 배열
for i in range(n):
    a, b = map(int,input().split()) # 입력 받고
    ingredients.append([a,b])

def combi(cnt,ans):
    if cnt == n: # n번 됐으면 함수 종료조건
        if ans: # 만약 정답배열에 담겼으면
            mul_ = 1
            add_ = 0
            for a in ans:
                mul_ *= a[0] # 신맛들은 곱하기
                add_ += a[1] # 쓴맛들은 더하기
            result.append(abs(mul_ - add_)) # 두 개 뺀 절대값 정답 배열에 담고
        return # 함수 끝내기

    # 현재 재료를 포함하는 경우
    ans.append(ingredients[cnt])
    combi(cnt+1, ans)
    ans.pop()

    # 현재 재료를 포함하지 않는 경우
    combi(cnt+1, ans)

combi(0,[])
print(min(result))