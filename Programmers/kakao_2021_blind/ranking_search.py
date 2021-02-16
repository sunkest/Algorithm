# 구현, 이진탐색
# 유형별로 분류해놔야함
# 효율성테스트 362/361/1281/1280 ms
from bisect import bisect_left

LANGS = ['cpp', 'java', 'python']
JOBS = ['backend', 'frontend']
CAREERS = ['junior', 'senior']
FOODS = ['chicken', 'pizza']


def solution(info, query):
    pool = {lang: {job: {career: {food: [] for food in FOODS} for career in CAREERS} for job in JOBS} for lang in LANGS}
    
    # 입력
    for string in info:
        lang, job, career, food, score = string.split(' ')
        pool[lang][job][career][food].append(int(score))

    # 이진탐색 위해 정렬
    for lang in LANGS:
        for job in JOBS:
            for career in CAREERS:
                for food in FOODS:
                    pool[lang][job][career][food].sort()


    answer = []
    for q in query:
        result = 0
        lang, job, career, last = q.split(' and ')
        food, score = last.split(' ')
        score = int(score)
        langs = []; jobs = []; careers = []; foods= [],
        if lang == '-':
            langs = LANGS[:]
        else:
            langs = [lang]
        if job == '-':
            jobs = JOBS[:]
        else:
            jobs = [job]
        if career == '-':
            careers = CAREERS[:]
        else:
            careers = [career]
        if food == '-':
            foods = FOODS[:]
        else:
            foods = [food]

        for lang in langs:
            for job in jobs:
                for career in careers:
                    for food in foods:
                        arr = pool[lang][job][career][food]
                        result += len(arr) - bisect_left(arr, score)

        answer.append(result)

    return answer


info_ = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query_ = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"]
print(solution(info_, query_))
