from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [-1] * n
        right = [-1] * n
        left[0] = 1
        right[-1] = 1
        curr_rating = 1
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                curr_rating += 1
            else:
                curr_rating = 1
            left[i] = curr_rating
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                curr_rating += 1
            else:
                curr_rating = 1
            right[i] = curr_rating
        answer = 0
        for i in range(n):
            answer += max(left[i], right[i])
        return answer
