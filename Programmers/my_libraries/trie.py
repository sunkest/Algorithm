class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self, arr=None):
        if arr is None:
            self.head = Node(None)
        else:
            for string in arr:
                self.insert(string)

    def insert(self, string):
        current_node = self.head

        for ch in string:
            if ch not in current_node.children:
                current_node.children[ch] = Node(ch)

            current_node = current_node.children[ch]

        current_node.data = string

    def search(self, string):
        current_node = self.head
        for ch in string:
            if ch in current_node.children[ch]:
                current_node = current_node.children[ch]
            else:
                return False

        if current_node.data is not None:   # 탐색 후 current_node의 data가 None이 아닌경우
            return True
        else:
            return False
