t = 10
for tc in range(1, t+1):
    n = int(input())
    line = list(input())  # 문자열을 리스트로 변환
    
    i = 0
    while i < len(line) - 1:
        # 열린 괄호에 대한 처리
        if line[i] == "{" and line[i+1] == "}":
            del line[i:i+2]  # 짝이 맞는 경우 해당 괄호를 제거
            i = max(0, i-1)  # 인덱스 조정
        elif line[i] == "[" and line[i+1] == "]":
            del line[i:i+2]
            i = max(0, i-1)
        elif line[i] == "(" and line[i+1] == ")":
            del line[i:i+2]
            i = max(0, i-1)
        elif line[i] == "<" and line[i+1] == ">":
            del line[i:i+2]
            i = max(0, i-1)
        else:
            i += 1  # 괄호가 맞지 않으면 인덱스 증가

    # 결과 확인
    if not line:
        print(f"#{tc} 1")  # 모든 괄호가 제거되었으면 올바른 괄호
    else:
        print(f"#{tc} 0")  # 남아있는 괄호가 있으면 잘못된 괄호