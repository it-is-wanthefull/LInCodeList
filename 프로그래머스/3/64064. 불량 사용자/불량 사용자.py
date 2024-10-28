import re
from itertools import product

def solution(user_id, banned_id):
    outer_list = list()
    for b in banned_id:
        
        inner_list = list()
        for u in user_id:
            query = b.replace('*', '.')
            match = re.match(f'^{query}$', u)
            if match:
                inner_list.append(u)
                
        outer_list.append(inner_list)
    
    def combination_of_list(outer_list, selected_list, final_set):
        if len(outer_list) == 0:
            final_set.add(tuple(sorted(selected_list)))
            return
        for selected in outer_list[0]:
            if selected not in selected_list:
                new_selected_list = selected_list + [selected]
                combination_of_list(outer_list[1:], new_selected_list, final_set)
                
    selected_list = list()
    final_set = set()
    combination_of_list(outer_list, selected_list, final_set)
    
    return len(final_set)