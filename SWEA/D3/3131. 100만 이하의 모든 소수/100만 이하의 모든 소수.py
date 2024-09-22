# 수가 크면 소수 찾는 에라토스테네스의 체가 효율적
def sieve_of_eratosthenes(max_Limit):
    #에라토스테네스의 체를 사용하여 max_limit 이하의 모든 소수를 반환합니다.
    # 체로 거르는 것 처럼 True 만 출력
    is_prime = [True]*(max_Limit+1)
    # 0과 1은 소수가 아니기에 False
    is_prime[0] = is_prime[1] = False

    # 공식 -> 먼저 각 2의 배수라면 자기 자신 2 를 뺸 2의배수 전부 Fasle
    # 3, 5, 7 뺀 3, 5 , 7 의 배수(mutiple) 전부 False
    # 4의 배수나 8의 배수는 어차피 2의 배수 안이기에 이미 False 돼있음
    # max_Limit**0.5 == math.sqrt(max_Limit) 와 동일
    # 에라토스테네스의 체에서는 제곱근까지만 소수를 판별하면 충분. 그 이유는, 어떤 수 n이 소수가 아니려면 반드시 √n 이하의 약수가 존재하기 때문
    for cur in range(2, int(max_Limit**0.5)+1):
        # 현재 cur 배수 인지 확인
        if is_prime[cur]:
            # 배수 제거, 현재 cur 3이라면, 3*3 부터 시작해서, cur 만큼 스텝 증가 -> cur 만큼 증가는 3 -> 6 즉 3의 배수를 뜻함
            # 즉 9 이상부터 12 , 15, 18 씩 제거,
            # 6은 이미 2 에서 제거되었기에 시작점은 cur * cur 임
            for mutiple in range(cur*cur, max_Limit + 1, cur):
                # 해당 배수의 수는 전부 소수가 아님을 지정
                is_prime[mutiple] = False

    # 최종 primes 값이 True 면
    # enumerate(is_prime) => is_prime 리스트 에서 인덱스와 값을 동시에 가져온다
    # num이 숫자를, primes  그 숫자가 소수인지 아닌지를 나타냄
    # primes의 True 에 해당하는 num 만 return
    primes = [num for num, primes in enumerate(is_prime) if primes]
    return primes

max_Limit = 10**6
primes = sieve_of_eratosthenes(max_Limit)
print(*primes, end=" ")