def solution(n, m, section):
    pos    = section[0]
    answer = 0
    
    for start_section in section : 
        if start_section == pos :
            answer += 1
            pos     = pos + m 
        elif start_section < pos : 
            continue
        elif start_section > pos : 
            answer += 1
            pos     = start_section + m 
            
    return answer