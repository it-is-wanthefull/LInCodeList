def solution(bandage, health, attacks):
    now_hp = health
    heal_stack = 0
    for i in range(attacks[-1][0]):
        now_time = i+1
        
        if now_time == attacks[0][0]:
            now_hp -= attacks[0][1]
            attacks.pop(0)
            heal_stack = 0
            if now_hp <= 0:
                return -1
            continue
            
        now_hp += bandage[1]
        heal_stack += 1
        if heal_stack == bandage[0]:
            heal_stack = 0
            now_hp += bandage[2]
        now_hp = min(now_hp, health)
    
    return now_hp