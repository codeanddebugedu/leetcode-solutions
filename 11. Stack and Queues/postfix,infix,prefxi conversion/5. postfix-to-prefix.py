class Solution:
    def postToPre(self, s):
        # Stack to store operands
        stack = []

        # Process each character in postfix expression
        for char in s:
            # If the character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # Pop two operands from the stack
                operand2 = stack.pop()
                operand1 = stack.pop()

                # Combine the operands with the operator in prefix form
                new_expr = f"{char}{operand1}{operand2}"

                # Push the result back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the prefix expression
        return stack[-1]
