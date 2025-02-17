def solution(players, callings):
    # 초기 선수 순서 (리스트로 관리)
    score_player = players[:]
    
    # 선수들의 현재 위치를 딕셔너리로 관리
    player_score = {player: idx for idx, player in enumerate(players)}
    
    # 호출된 선수 처리
    for calling in callings:
        current_pos = player_score[calling]  # 호출된 선수가 위치한 자리
        # 한 칸 앞으로 이동
        new_pos = current_pos - 1
        
        # 앞에 있는 선수와 교환
        front_player = score_player[new_pos]
        
        # 선수들의 위치 업데이트
        score_player[new_pos] = calling
        score_player[current_pos] = front_player
        
        # player_score 딕셔너리도 갱신
        player_score[calling] = new_pos
        player_score[front_player] = current_pos
    
    return score_player