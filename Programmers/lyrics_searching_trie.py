# kakao 2020 blind #4 가사검색
# by Trie - 프로그래머스 기준 효율성테스트 2500/4700/x/x/x
from collections import defaultdict


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.count = defaultdict(int)


class Trie(object):
    def __init__(self, arr=()):
        self.head = Node(None)
        if len(arr) > 0:
            for string in arr:
                self.insert(string)

    def insert(self, string):  # 삽입
        current_node = self.head
        current_node.count[len(string)] += 1
        for ch in string:
            if ch not in current_node.children:
                current_node.children[ch] = Node(ch)

            current_node = current_node.children[ch]
            current_node.count[len(string)] += 1
        current_node.data = string

    def prefix_count(self, prefix, length):  # prefix로 시작하는 단어들의 개수만 계산  # prefix_search 보다 훨씬 빠름
        current_node = self.head

        for ch in prefix:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return 0

        return current_node.count[length]


def solution(words, queries):
    answer = []
    trie = Trie()
    reversed_trie = Trie()
    for word in words:
        trie.insert(word)
        reversed_trie.insert(word[::-1])

    for query in queries:
        length = len(query)
        result = 0
        if query == "?"*len(query):
            answer.append(trie.head.count[len(query)])

        if query[0] == '?':
            result = reversed_trie.prefix_count(query[::-1].split("?")[0], length)
        else:
            result = trie.prefix_count(query.split("?")[0], length)

        answer.append(result)

    return answer


words_ = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries_ = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words_, queries_))