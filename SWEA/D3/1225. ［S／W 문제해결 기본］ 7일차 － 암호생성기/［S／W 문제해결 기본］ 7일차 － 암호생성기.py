from collections import deque
t = 10
for tc in range(1, t+1):

    _ = int(input())
    # 빈큐 기본형 ([])
    q = deque(list(map(int, input().split())))
    # print(q[7])

    while q[7] != 0:
        cycle = 5
        if q[7] != 0:
            for i in range(1, cycle+1):
                left = q.popleft()
                left -= i
                #0보다 작거나 같으면
                if left <= 0:
                    #0을 추가
                    q.append(0)
                    break
                else:
                    q.append(left)
        else:
            break
    #큐를 리스트로 바꾸고 아스트릭으로 리스트 벗겨서 공백과 함께 출력
    print(f"#{tc}", *list(q))
