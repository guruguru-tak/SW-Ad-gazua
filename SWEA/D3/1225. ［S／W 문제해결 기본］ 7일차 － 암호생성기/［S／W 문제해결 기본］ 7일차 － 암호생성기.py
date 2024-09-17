from collections import deque

t = 10
for tc in range(1, t+1):
    _ = input()
    q = deque(map(int, input().split()))

    flag = True
    while flag:
        for i in range(1, 6):
            temp = q.popleft()
            if temp - i <= 0:
                q.append(0)
                flag = False
                break
            else:
                q.append(temp-i)

    print(f"#{tc}", *list(q))