def solution(babbling):
    substring_list = ["aya", "ye", "woo", "ma", "****", "***", "**"]
    answer_count = 0
    
    for string in babbling:
        for substring in substring_list:
            string = string.replace(substring, "*")
        if string == "*":
            answer_count += 1
            
    return answer_count