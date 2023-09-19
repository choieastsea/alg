from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        한글자씩 다른 단어들로 search space를 확장하면서 BFS를 수행
        확장시, 최초 마주치는 단어는 이후에 선택되지 않도록 해야함
        최단 거리에 위치한 endWord 발견시 len(depth)를 리턴
        """
        q = deque()
        visited = {}
        q.append((beginWord, 1)) # word, depth
        visited[beginWord] = True
        while q:
            curWord, depth = q.popleft()
            # 주변으로 확장
            for word in wordList:
                if not word in visited:
                    # 한 글자만 다른 단어로 공간 확장
                    diffCnt = 0
                    for i in range(len(word)):
                        if word[i] != curWord[i]:
                            diffCnt += 1
                            if diffCnt > 1:
                                break
                    if diffCnt == 1:
                        # 답 발견하면 종료
                        if word == endWord:
                            return depth + 1
                        q.append((word, depth + 1))
                        visited[word] = True
        return 0