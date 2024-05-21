"""
Time Complexity: O(N*4*3)
Reason: There are N*4 states and for every state, 
we are running a for loop iterating three times.

Space Complexity: O(N) + O(N*4)
"""


class Solution:
    def solve(self, day, last, points, dp):
        # Check if the result for this day and last activity is already computed
        if dp[day][last] != -1:
            return dp[day][last]
        # Base case: When we reach day 0, return the maximum point for the last day.
        if day == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])
            dp[day][last] = maxi
            return dp[day][last]

        maxi = 0
        # Iterate through all activities for the current day.
        for i in range(3):
            if i != last:
                # Calculate the total points for the current day's activity and recursively call for the previous day.
                activity = points[day][i] + self.solve(day - 1, i, points, dp)
                maxi = max(maxi, activity)

        dp[day][last] = maxi
        return dp[day][last]

    def maximumPoints(self, points, n):
        dp = [[-1 for j in range(4)] for i in range(n)]
        return self.solve(n - 1, 3, points, dp)
