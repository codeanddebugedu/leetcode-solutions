from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = []
        for i in range(n):
            start, end = intervals[i][0], intervals[i][1]

            # Skip intervals if in between
            if len(ans) != 0 and end <= ans[-1][1]:
                continue

            # Go for futher intervals
            for j in range(i + 1, n):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break
            ans.append([start, end])
        return ans
