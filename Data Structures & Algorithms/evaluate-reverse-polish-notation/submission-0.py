class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)

            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)

            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(token))

        return stack[-1] 