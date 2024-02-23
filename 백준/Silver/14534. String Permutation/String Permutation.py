def my_permutation(nums):
    sum_permutations = []

    if len(nums) == 1:
        return [nums]

    for i in range(len(nums)):
        nums_copy = nums.copy()
        nums_copy.pop(i)
        sub_permutations = my_permutation(nums_copy)
        for p in sub_permutations:
            sum_permutations.append([nums[i]] + p)
    return sum_permutations

#----- ----- ----- ----- ----- ----- ----- ----- ----- -----

if __name__ == '__main__':
    from itertools import permutations

    T = int(input())
    for i in range(1, T+1):

        s = input().strip()
        result1 = list(permutations(list(s))) #자체제작 함수
        result2 = my_permutation(list(s))     #라이브러리 함수

        print(f"Case # {i}:")
        for perm1, perm2 in zip(result1, result2):
            r1 = ''.join(perm1)
            r2 = ''.join(perm2)
            #print(r1)
            print(r2)
            # if r1 != r2:
            #     print("diffffffffffffffffffffffff")
            #     break