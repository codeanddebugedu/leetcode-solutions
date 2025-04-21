class Solution:
    def preToPost(self, s):
        # Stack to store operands
        stack = []

        # Traverse the prefix expression from right to left using index
        n = len(s)
        for i in range(n - 1, -1, -1):  # Reverse iteration using index
            char = s[i]

            # If the character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # Pop two operands from the stack
                operand1 = stack.pop()
                operand2 = stack.pop()

                # Combine the operands with the operator in postfix form
                new_expr = operand1 + operand2 + char

                # Push the result back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the postfix expression
        return stack[-1]
