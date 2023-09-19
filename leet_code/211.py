from collections import deque
class WordDictionary:

    def __init__(self):
        self.head = {'isEnd' : False}

    def addWord(self, word: str) -> None:
        current = self.head
        for ch in word:
            if ch not in current:
                current[ch] = {'isEnd' : False}
            current = current[ch]
        current['isEnd'] = True
        
    def search(self, word: str) -> bool:
        q = deque([self.head])
        for ch in word:
            # print(q, ch)
            if ch == '.':
                for _ in range(len(q)):
                    current = q.popleft()
                    for k,v in current.items(): # 가능한 다음 노드들을 모두 탐색함
                        if k != 'isEnd':
                            q.append(v)
            else:     
                # 일반 문자라면, 해당 문자가 있는지 확인하고 넣어줌. 없는 것들은 무시
                for _ in range(len(q)):
                    current = q.popleft()
                    if ch in current:
                        q.append(current[ch])
        for el in q: # 마지막 단계의 노드들이 deque에 존재할 것
            if el['isEnd']:
              	# 해당 단어가 존재함!
                return True
        return False
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)