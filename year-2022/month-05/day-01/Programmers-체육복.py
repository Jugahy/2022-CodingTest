def solution(n, lost, reserve):
    a = 0
    dic = {}

    for i in range(1, n + 1):
        if i in lost and i in reserve:
            dic[i] = 1
        elif i in lost:
            dic[i] = 0
        elif i in reserve:
            dic[i] = 2
        else:
            dic[i] = 1

# 딕셔너리의 value들을 받을 때 리스트로 받았으니 다시 딕셔너리로 사용할려면 인덱스 주의
    for j in range(n):
        if list(dic.values())[j] == 0:
            try:
                if dic[j] == 2 and dic[j + 2] == 2:
                    dic[j] = 1
                    dic[j + 1] = 1

                elif dic[j] == 2:
                    dic[j] = 1
                    dic[j + 1] = 1

                elif dic[j + 2] == 2:
                    dic[j + 2] = 1
                    dic[j + 1] = 1
            except KeyError:
                pass

    for k in range(1, n + 1):
        if dic[k] == 0:
            a = +1

    return n - a