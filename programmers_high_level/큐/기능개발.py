import math
def solution(progresses, speeds):
    for i in range(len(progresses)):
        progresses[i] = math.ceil(( 100 - progresses[i] ) / speeds[i])
    print(progresses)
    answer = [1]
    pre = progresses[0]
    cur = 0
    for i in progresses[1:]:
        print(pre, i )
        if pre >= i:
            answer[cur] += 1
        else:
            pre = i
            answer.append(1)
            cur+=1
    
    return answer