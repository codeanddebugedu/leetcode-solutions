"""
Time Complexity: O(N*4*3)
Reason: There are N*4 states and for every state, 
we are running a for loop iterating three times.

Space Complexity: O(N*4)
"""


class Solution:

    def maximumPoints(self, points, n):
        # Initialize a DP table with dimensions (n x 4) to store the maximum points.
        dp = [[0 for j in range(4)] for i in range(n)]

        # Initialize the DP table for day 0 with base cases.
        dp[0][0] = max(points[0][1], points[0][2])
        dp[0][1] = max(points[0][0], points[0][2])
        dp[0][2] = max(points[0][0], points[0][1])
        dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]))

        # Loop through the days starting from the second day.
        for day in range(1, n):
            for last in range(4):
                dp[day][
                    last
                ] = 0  # Initialize the maximum points for the current day and last activity.
                for task in range(3):
                    if task != last:
                        # Calculate the total points for the current day's activity and the previous day's maximum points.
                        activity = points[day][task] + dp[day - 1][task]
                        dp[day][last] = max(dp[day][last], activity)

        # Return the maximum points achievable after the last day with any activity.
        return dp[n - 1][3]
