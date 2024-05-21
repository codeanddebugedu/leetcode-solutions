class Solution:
    def solve(self, day, last, points):
        # Base case: When we reach day 0, return the maximum point for the last day.
        if day == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])
            return maxi

        maxi = 0
        # Iterate through all activities for the current day.
        for i in range(3):
            if i != last:
                # Calculate the total points for the current day's activity and recursively call for the previous day.
                activity = points[day][i] + self.solve(day - 1, i, points)
                maxi = max(maxi, activity)

        return maxi

    def maximumPoints(self, points, n):
        return self.solve(n - 1, 3, points)
