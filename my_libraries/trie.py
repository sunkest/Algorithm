class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self, arr=()):
        self.head = Node(None)
        if len(arr) > 0:
            for string in arr:
                self.insert(string)

    def insert(self, string):  # 삽입
        current_node = self.head

        for ch in string:
            if ch not in current_node.children:
                current_node.children[ch] = Node(ch)

            current_node = current_node.children[ch]

        current_node.data = string

    def search(self, string):  # 문자열이 trie에 추가된 적이 있는지 검색.
        current_node = self.head
        for ch in string:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return False

        if current_node.data is not None:   # 탐색 후 current_node의 data가 None이 아닌경우
            return True
        else:
            return False

    def prefix_search(self, prefix):  # prefix로 시작하는 단어들을 반환
        current_node = self.head
        result = []

        for ch in prefix:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return []

        search_head = current_node
        stack = [ch for ch in search_head.children.values()]

        while stack:
            dfs_node = stack.pop()
            if dfs_node.data is not None:
                result.append(dfs_node.data)
            stack.extend([ch for ch in dfs_node.children.values()])

        return result
