from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCounter = Counter(ransomNote)
        mCounter = Counter(magazine)
        return len(rCounter - mCounter) <=0
        