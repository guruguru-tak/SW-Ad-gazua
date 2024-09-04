from itertools import combinations

cards_num , max_num = map(int, input().split())
cards_list = list(map(int, input().split()))

#입력 카드 중에 3장 골라야 한다

result = 0
for cards in combinations(cards_list, 3):
    cards_sum = sum(cards)
    #m 값을 넘기지 않는 조건 추가
    if cards_sum <= max_num:
        result = max(result, cards_sum)

print(result)