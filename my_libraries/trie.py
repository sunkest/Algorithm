class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.count = 0

class Trie(object):
    def __init__(self, arr=()):
        self.head = Node(None)
        if len(arr) > 0:
            for string in arr:
                self.insert(string)

    def insert(self, string):  # 삽입
        current_node = self.head
        current_node.count += 1
        for ch in string:
            if ch not in current_node.children:
                current_node.children[ch] = Node(ch)

            current_node = current_node.children[ch]
            current_node.count += 1
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

    def prefix_search(self, prefix):  # prefix로 시작하는 단어들을 반환  # 개수만 알고 싶은 경우 prefix_count 가 훨씬 빠름
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

    def prefix_count(self, prefix):  # prefix로 시작하는 단어들의 개수만 계산  # prefix_search 보다 훨씬 빠름
        current_node = self.head

        for ch in prefix:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return 0

        return current_node.count
