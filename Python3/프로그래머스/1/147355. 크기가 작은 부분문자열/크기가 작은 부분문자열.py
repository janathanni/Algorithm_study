def solution(t, p):
    answer = 0 
    for i in range (0, len(t)):
        start_idx = i
        end_idx   = i + len(p)
        
        if end_idx > len(t) :
            return answer
        
        if int(t[start_idx:end_idx]) <= int(p) :
            answer += 1 
        
    return answer