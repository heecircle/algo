# from collections import Counter
# def solution(genres, plays):
#     new_list = {}
#     for i in range(len(genres)) : 
#         if genres[i] in new_list.keys():
#             new_list[genres[i]][0] += plays[i]
#             new_list[genres[i]][1].append([i, plays[i]])
#         else:
#             new_list[genres[i]] = [plays[i],[[i,plays[i]]]]
#     new_dict = (sorted(new_list.items(), key = lambda item: item[1][0], reverse = True))
#     answer = []
#     for i in new_dict:
#         a = (sorted(i[1][1], key=lambda x : x[-1], reverse = True))
#         for i in range(2):
#             answer.append(a[i][0])
    
#     return answer


# 참고 풀이

def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer