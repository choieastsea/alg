class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = {'end' : False}
        for word in strs:
            if word == '':
                return ''
            curNode = trie
            for ch in word:
                if ch not in curNode:
                    # 없으면 새로운 노드 추가
                    curNode[ch] ={'end' : False}
                curNode = curNode[ch]
            curNode['end'] = True
        # print(trie)
        lcp = ''
        curNode = trie
        while True:
            # 자식이 1개(end 포함하면 2개)가 아닐때까지 탐색
            if len(curNode.keys()) != 2 or curNode['end']:
                break
            else:
                for key in curNode.keys():
                    if key != 'end':
                        lcp += key
                        curNode = curNode[key]
                        break
        return lcp