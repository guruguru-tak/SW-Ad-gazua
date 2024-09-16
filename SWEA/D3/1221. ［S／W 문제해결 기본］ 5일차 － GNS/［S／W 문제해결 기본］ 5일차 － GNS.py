gns = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}


t = int(input())
for tc in range(1, t+1):
    _, n = input().split()
    str_gns = list(input().split())

    num = []
    for i in str_gns:
        # gns 딕셔너리에서 입력 값 i 의 동일 키의 밸류 값 반환
        num.append(gns.get(i))

    # 오름차순 정렬
    num.sort()
    gns_to = []
    for i in num:
        # 키, 밸류 값을 gns에서 item으로 분리해서 들고와서
        for k, v in gns.items():
            # 만약 숫자 i 가 gns의 밸류값과 같으면
            if i == v:
                # 키값을 반환
                gns_to.append(k)

    print(f"#{tc} ",*gns_to)