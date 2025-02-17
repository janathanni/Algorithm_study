import math

def solution(number, limit, power):
    blade_atk = 0
    
    for i in range(1, number + 1):
        # 숫자 1일 때는 공격력 1
        if i == 1:
            blade_atk += 1
            continue
        
        tmp_blade_atk = 0
        
        # i의 약수 개수 구하기 (sqrt(i)까지 계산)
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:  # j가 i의 약수라면
                if j * j == i:
                    tmp_blade_atk += 1  # 제곱수일 경우 약수는 하나만 추가
                else:
                    tmp_blade_atk += 2  # 일반적인 경우 약수는 두 개 (j, i // j)
        
        # 공격력이 limit을 넘으면 power로 제한
        if tmp_blade_atk > limit:
            tmp_blade_atk = power
        
        blade_atk += tmp_blade_atk
    
    return blade_atk