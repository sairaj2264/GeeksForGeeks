class Solution:
    def infixtoPostfix(self, s):
        stack = []

        def priority(e):
            if e == '^':
                return 3
            if e == '*' or e == '/':
                return 2
            if e == '+' or e == '-':
                return 1
            if e == '(':
                return 0

        answer = []

        for ch in s:

            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
                answer.append(ch)


            elif ch == '(':
                stack.append(ch)


            elif ch == ')':
                while stack and stack[-1] != '(':
                    answer.append(stack.pop())
                stack.pop()         


            else:

                while (stack and stack[-1] != '(' and
                       (priority(stack[-1]) > priority(ch) or
                        (priority(stack[-1]) == priority(ch) and ch != '^'))):

                    answer.append(stack.pop())

                stack.append(ch)

        while stack:
            answer.append(stack.pop())

        return "".join(answer)