import sys

# sys.stdin = open("input.txt", "r", encoding='utf-8')

n = int(input())

# 중복 제거 집합 사용
line = set()
sort_cnt = 0
for _ in range(n):
    line.add(input())

# 길이순으로 정렬한 뒤, 길이가 같다면 사전순으로 정렬
# key=lambda x: (len(x), x): 각 요소에 대해 (길이, 문자열)의 형태로 정렬 키
sorted_line = sorted(line, key = lambda x: (len(x), x))
for i in sorted_line:
    print(i)