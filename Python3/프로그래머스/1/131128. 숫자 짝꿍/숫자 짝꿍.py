# def solution(X, Y):
#     answer = ''
    
#     if len(X) > len(Y) : 
#         X, Y = Y, X 
    
#     pairs = []
    
#     Y_pos = 0
    
#     #1. 짝꿍을 찾은 리스트 생성
#     for i in (0, len(X)-1) : 
#         for j in (Y_pos, len(Y)-1):
#             if X[i] == Y[j]: 
#                 pairs.append(X[i])    
                
#     #2. 짝꿍 리스트를 내림차순으로 정렬 => 만약 짝꿍 리스트가 빈 배열이면 -1 
    
#     if not pairs : 
#         answer = '-1' 
#     else : 
#         pairs.sort(reverse=True)
    
#     #3. 짝꿍 리스트에 있는 내용 그대로 숫자 출력 
#     for pair in pairs:
#         answer = answer + pair
    
#     return answer


def solution(X, Y):
    answer = ''
    
    X = sorted(list(X)) 
    Y = sorted(list(Y))
    
    pairs = []
    
    #1. 짝꿍을 찾은 리스트 생성
    while len(X) > 0 and len(Y) > 0 :
        if X[-1] == Y[-1] : 
            pairs.append(X[-1])
            X.pop()
            Y.pop() 
        elif X[-1] > Y[-1] : 
            X.pop()
        elif X[-1] < Y[-1] : 
            Y.pop() 

    if len(pairs) > 0 : 
        for pair in pairs : 
            answer = answer + pair
        
        if answer[0] == '0' : 
            answer = '0'
        
    else : 
        answer = "-1"
    
    return answer