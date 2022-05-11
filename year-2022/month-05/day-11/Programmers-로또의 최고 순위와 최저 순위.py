def solution(lottos, win_nums):
    dic = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2}
    return [dic[len([i for i in lottos if i in win_nums]) + lottos.count(0)],
            dic[len([i for i in lottos if i in win_nums])]]
