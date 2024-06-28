def solution(babbling):
    answer_count = 0
    substring_list = ["aya", "ye", "woo", "ma"]
    zip_list = ["****", "***", "**", "*"]
    
    for string in babbling:
        for substring in substring_list:
            string = string.replace(substring, "*")
        for e in zip_list:
            string = string.replace(e, "count")
        if string == "count":
            answer_count += 1
    return answer_count