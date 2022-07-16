def solution(nums):
    len_sets = len(list(set(nums)))ㅁ
    len_nums = len(nums)//2

    if len_nums < len_sets:
        return len_nums
    else:
        return len_sets