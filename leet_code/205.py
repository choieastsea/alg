class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sDict = {} # from : to
        toSet = set() # 바뀐 것들 목록
        for i in range(len(s)):
            if s[i] in sDict:
                if t[i] in toSet:
                    if t[i] != sDict[s[i]]:
                        return False
                    else:
                        continue
                return False
            else:
                if t[i] in toSet:
                    return False
                sDict[s[i]] = t[i]
                toSet.add(t[i])
        return True