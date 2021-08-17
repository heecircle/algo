wine = int(input())
wine_capa = [0]
result = [0 for _ in range(wine + 1)]

for _ in range(wine):
    wine_capa.append(int(input())) #포도주 양 받기

for i in range(1, wine + 1):
    if i == 1:
        result[1] = wine_capa[1]
    elif i == 2:
        result[2] = wine_capa[1] + wine_capa[2]
    else:
        result[i] = max(result[i-3] + wine_capa[i-1] + wine_capa[i], result[i-2] + wine_capa[i], result[i-1])  
        #세개 중에 가장 큰값 구해서 result에 넣어주기 첫번재껀 연속 두개, 두번째껀 하나띄고 한개 마시는 경우. 그냥 안마시는 경우 
        #마안마마/마안마/안
print(result[i])

