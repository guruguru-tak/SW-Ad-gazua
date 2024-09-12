t = 10
for tc in range(1, t+1):
    onebon_n = int(input())
    onebon_pwd = list(map(int, input().split()))
    cmd_n = int(input())
    cmd = list(input().split())

    for c in range(len(cmd)):

        if cmd[c] == 'I':
            idx = int(cmd[c+1])
            # print(tc, "idx", idx)
            num_cnt = int(cmd[c+2])
            # print(tc, "num_cnt", num_cnt)
            for n in range(c+3, c+3+num_cnt):
                onebon_pwd.insert(idx, int(cmd[n]))
                #추가하면서 바로 뒤에 추가 이어가기에 idx 증가해야 함
                idx += 1
                
        elif cmd[c] == 'D':
            idx = int(cmd[c+1])
            num_cnt = int(cmd[c+2])
            for n in range(c+3, c+3+num_cnt):
                onebon_pwd.pop(idx)
                idx+1
                
        elif cmd[c] == "A":
            num_cnt = int(cmd[c+1])
            for n in range(c+2, c+2+num_cnt):
                #뒤에 추가는 항상 인덱스 맨 뒤 추가라서 인덱스 조정 필요 없음
                onebon_pwd.append(cmd[n])
        else:
            pass
        
    print(f"#{tc}", end=" ")
    for i in range(10):
        print(onebon_pwd[i], end=" ")
    print()



