def solution(numbers):
    ## 잘 모르겠어서 GPT한테 물어봤음 
    
    n = len(numbers)
    answer = [-1] * n  # 결과를 저장할 리스트 초기화 (모든 값을 -1로 설정)
    stack = []  # 스택: 아직 "오른쪽에 있는 큰 수"를 찾지 못한 숫자들의 인덱스를 저장

    for i in range(n):
        # 스택이 비어있지 않고, 현재 숫자 numbers[i]가 스택 맨 위 인덱스에 해당하는 숫자보다 클 때
        while stack and numbers[i] > numbers[stack[-1]]:
            # 스택 맨 위 인덱스 pop
            j = stack.pop()
            # pop한 인덱스 j에 해당하는 answer 값을 현재 숫자 numbers[i]로 갱신
            answer[j] = numbers[i]

        # 현재 인덱스 i를 스택에 push
        stack.append(i)

    return answer