class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        해당 숫자들로 만들 수 있는 문자열의 조합 리턴
        """
        if not digits:
            return []
        comb = []
        char_list = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def bt(letters, digits):
            if len(letters) == len(digits):
                # 종료 조건
                comb.append(letters)
            else:
                # letters에 추가 필요
                next_num = int(digits[len(letters)])
                for ch in char_list[next_num]:
                    bt(letters+ch, digits)
        bt('',digits)
        return comb