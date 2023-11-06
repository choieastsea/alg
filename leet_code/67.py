class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(num1: str, num2: str):
            # 같은 길이의 이진수 계산하여 더한 문자열 리턴
            result = ''
            up = False
            for i in range(len(num2)):
                curIdx = -1-i
                if num2[curIdx] == '1':
                    # 1,1
                    if num1[curIdx] == '1':
                        if up:
                            result += '1'
                        else:
                            result += '0'
                        up = True
                    else:
                        # 1,0
                        if up:
                            result += '0'
                            up = True
                        else:
                            result += '1'
                            up = False
                else:
                    # 0,0
                    if num1[curIdx] == '0':
                        if up:
                            result += '1'
                        else:
                            result += '0'
                        up = False
                    else:
                        # 0, 1
                        if up:
                            result += '0'
                            up = True
                        else:
                            result += '1'
                            up = False
            if up:
                result += '1'
            return result[::-1]

        dif = len(a) - len(b)
        if dif > 0:
            b = '0'* dif + b
        else: # b가 더 큼
            a = '0'*(-dif) + a
        return add(a,b)
