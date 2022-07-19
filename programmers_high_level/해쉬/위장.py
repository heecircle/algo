from collections import Counter
def solution(clothes):
    answer = 1
    a = (Counter([type for clothe, type in clothes]))
    print(a)
    if (len(a)) == 1:
        for i in a:
            return a[i]
    for i in a:
        answer *= (a[i] +1)
    return answer -1