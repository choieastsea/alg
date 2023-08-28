import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. remove non-alphanumeric and to lower case
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # 3. isPalindrome?
        n = len(s)
        for i in range(n//2):
            forward =  s[i]
            backward = s[n-i-1]
            if forward != backward:
                return False
        return True