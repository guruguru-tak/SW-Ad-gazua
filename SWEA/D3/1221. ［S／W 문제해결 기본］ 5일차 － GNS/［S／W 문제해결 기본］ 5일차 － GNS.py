gns_dic = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

t = int(input())
for tc in range(1, t+1):
    #split 기능으로  # 특수문자 두개 나누는 처리 어려움
    _, n = input().split()
    arr = list(input().split())

    num_arr = []
    for gns in arr:
        num_arr.append(gns_dic.get(gns))

    num_arr.sort()

    result = []
    for num in num_arr:
        result.extend([k for k, v in gns_dic.items() if v == num])


    print(f"#{tc}", *result)