class Node:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        current = self.head
        for ch in word:
            if ch not in current.next:
                # 없다면 노드 새로 만들어줌
                current.next[ch] = Node()
            # 다음 노드로 이동
            current = current.next[ch]
        # 마지막 노드에 isEnd 추가
        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.head
        for ch in word:
            if ch in current.next:
                current = current.next[ch]
            else:
                return False
        if current.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        current = self.head
        for ch in prefix:
            if ch in current.next:
                current = current.next[ch]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)