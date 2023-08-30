class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = "+-*/"
        for token in tokens:
            # print(stack, token)
            opInd = operator.find(token)
            if opInd > -1:
                # op
                a = stack.pop()
                b = stack.pop()
                if opInd == 0:
                    stack.append(b + a)
                elif opInd == 1:
                    stack.append(b - a)
                elif opInd == 2:
                    stack.append(b * a)
                elif opInd == 3:
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack.pop()