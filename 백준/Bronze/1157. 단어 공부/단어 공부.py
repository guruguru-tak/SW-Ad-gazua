import sys
input = sys.stdin.readline
from collections import Counter
# sys.stdin = open("input.txt", "r", encoding='utf-8')

string = input()

# 입력 값 전부 대문자로 변환
line_Up = string.upper()

# 카운터 함수로 미리 최대 값 찾기, count 함수는 O(n) 이라 시간 초과
cnt = Counter(line_Up)

# 가장 많이 등장한 빈도
max_Count = max(cnt.values())
# print(max_Count)

# 딕셔너리에서 카운터한 아이템 꺼내서 이 아이템이 최대 빈도수와 동일하면 result 배열에 넣기
result = [char for char, count in cnt.items() if count == max_Count]
#
# print(result)


# 길이 1이상이면 (1자리, 공백) 빼곤, 여러개 동일한 경우임
if len(result) > 1:
    # 글자 1개 입력시 공백 포함되기에 공백 예외처리 제거
    if len(result) == 2 and result[1] == "\n":
        print(*result)
    else:
        print("?")
else:
    print(*result)

