from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Initialize an empty stack to keep track of remaining asteroids.
        stack = []

        # Iterate through each asteroid in the input list.
        for asteroid in asteroids:
            # Assume that the current asteroid will not explode.
            should_append = True

            # While there is a potential collision (stack is not empty and the current asteroid is negative and the top of the stack is positive).
            while stack and stack[-1] > 0 and asteroid < 0:
                # Compare the sizes (absolute values) of the top asteroid in the stack and the current asteroid.
                if abs(stack[-1]) < abs(asteroid):
                    # The current asteroid is larger, pop the top of the stack (it gets destroyed).
                    stack.pop()
                    # Continue to check for further collisions with other asteroids in the stack.
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    # Both asteroids are the same size, destroy both.
                    stack.pop()
                    # Mark the current asteroid as exploded, so it will not be added to the stack.
                    should_append = False
                    break
                else:
                    # The current asteroid is smaller and it gets destroyed.
                    should_append = False
                    break

            # If the current asteroid is not destroyed in a collision, add it to the stack.
            if should_append:
                stack.append(asteroid)

        return stack
