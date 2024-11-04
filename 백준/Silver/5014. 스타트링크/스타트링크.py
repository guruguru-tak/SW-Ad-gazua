import sys
# sys.stdin = open("input.txt", "r")


from collections import deque

def bfs(f, s, g, u, d): #bfs 큐 사용
    visited = [False] * (f+1) #인덱스 번호로 건물 층 1층부터 사용 이해 +1 해준다
    q = deque([(s, 0)]) #현재 층과 그 층까지 도달하는 데 사용된 클릭 수 저장 큐
    visited[s] = True

    while q: #큐가 비어야만 탐색 종료, 큐가 비어 있지 않으면 계속 반복
    #while len(q) > 0: 과 동일

        current, button = q.popleft() #큐에서 현재 위치와 클릭 수 가져오기

        if current == g: #목표 층 도착
            return button # 목표층 도달 시 해당 클릭 수를 반환

        if current + u <= f and not visited[current + u]: #위로 이동
            visited[current + u] = True
            q.append((current+u, button + 1))

        if current - d > 0 and not visited[current - d]: #아래로 이동
            visited[current - d] = True
            q.append((current - d, button + 1))


    return 'use the stairs' #모든 층 탐색 후 목표층 갈 수 없을 때 반환
    # BFS 루프가 종료된 후에 def 내 제일 마지마 return 값



#f=최고점 s=현재위치 g=목표지점 u=위 d=아래
f, s, g, u, d = map(int, input().split())
result = bfs(f, s, g, u, d)
print(result)