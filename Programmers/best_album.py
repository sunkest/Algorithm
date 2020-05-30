import collections


def solution(genres, plays):
    answer = []
    d = {}
    g = {}
    for i in range(len(plays)):
        if d.get(genres[i]) is None:
            d[genres[i]] = [(i, plays[i])]
        else:
            d[genres[i]].append((i, plays[i]))
        if g.get(genres[i]) is None:
            g[genres[i]] = plays[i]
        else:
            g[genres[i]] += plays[i]

    g = sorted(g.items(), key=lambda item: item[1], reverse=True)

    for key, num in g:
        music = d[key]
        music = sorted(music, key=lambda m: m[1], reverse=True)
        answer.append(music[0][0])
        if len(music) > 1:
            answer.append(music[1][0])

    return answer

a = ['classic', 'pop', 'classic', 'classic']
b = [500, 600, 150, 800]
print(solution(a, b))
