class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        longestLen = 0
        for end in range(len(s)):
            # check repeat
            # print(substr, s[end])
            ind = substr.find(s[end])
            if ind >= 0:
                longestLen = max(longestLen, len(substr))
                substr = substr[ind+1:] + s[end]
                print('after:',substr)
            else:
                substr += s[end]
        # print(substr)
        return max(longestLen, len(substr))