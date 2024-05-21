"""
Time Complexity: O(N*4*3)
Reason: There are three nested loops

Space Complexity: O(4)
Reason: We are using an external array of size 4 to store only one row.
"""


class Solution:

    def maximumPoints(self, points, n):
        # Initialize a list 'prev' to store the maximum points for each possible last activity on the previous day.
        prev = [0] * 4

        # Initialize 'prev' with the maximum points for the first day's activities.
        prev[0] = max(points[0][1], points[0][2])
        prev[1] = max(points[0][0], points[0][2])
        prev[2] = max(points[0][0], points[0][1])
        prev[3] = max(points[0][0], max(points[0][1], points[0][2]))

        # Loop through the days starting from the second day.
        for day in range(1, n):
            # Initialize a temporary list 'temp' to store the maximum points for each possible last activity on the current day.
            temp = [0] * 4

            for last in range(4):
                # Initialize 'temp' for the current last activity.
                temp[last] = 0

                for task in range(3):
                    if task != last:
                        # Calculate the total points for the current day's activity and the previous day's maximum points.
                        activity = points[day][task] + prev[task]
                        # Update 'temp' with the maximum points for the current last activity.
                        temp[last] = max(temp[last], activity)

            # Update 'prev' with 'temp' for the next iteration.
            prev = temp

        # Return the maximum points achievable after the last day with any activity.
        return prev[3]
