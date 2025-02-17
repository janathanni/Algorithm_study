def solution(k, m, score):
    score.sort(reverse=True)
    
    i = 0
    answer = 0 
    
    while i <= len(score) : 
        if ( i + m  ) > len(score) : 
            break
        
        box = score[i : i + m]
        answer += box[-1] * m 
        
        i = i + m
    

    return answer