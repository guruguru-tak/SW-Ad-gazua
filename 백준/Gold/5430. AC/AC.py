import sys
from collections import deque

input = sys.stdin.readline

t = int(input().strip())  # 첫 번째 입력: 테스트 케이스 수

for _ in range(t):
    op = input().strip()  # 명령어를 읽고 양 끝 공백 제거
    n = int(input().strip())  # 배열의 크기를 정수로 변환
    arr = input().strip()[1:-1].split(',')  # 배열 문자열에서 대괄호 제거 후 파싱

    if n == 0:
        arr = deque()  # 배열이 비어있는 경우 빈 deque로 초기화
    else:
        arr = deque(arr)

    reverse = False
    error = False

    for cmd in op:
        if cmd == 'R':
            reverse = not reverse  # R 명령어가 있을 때마다 뒤집기 플래그 변경
        elif cmd == 'D':
            if arr:
                if reverse:
                    arr.pop()  # 뒤집힌 상태에서는 뒤에서 pop
                else:
                    arr.popleft()  # 그렇지 않으면 앞에서 pop
            else:
                print("error")
                error = True
                break

    if not error:
        if reverse:
            arr.reverse()  # reverse 플래그가 True인 경우 배열을 뒤집음
        print("[" + ",".join(arr) + "]")