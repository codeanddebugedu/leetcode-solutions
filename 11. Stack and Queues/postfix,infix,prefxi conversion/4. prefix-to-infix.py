class Solution:
    def preToInfix(self, s):
        # Stack to store operands
        stack = []

        for char in s[::-1]:
            # If character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # Pop two operands but with reversed order
                operand1 = stack.pop()
                operand2 = stack.pop()

                # Combine operands with the operator
                new_expr = f"({operand1}{char}{operand2})"

                # Push the result back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the infix expression
        return stack[-1]
