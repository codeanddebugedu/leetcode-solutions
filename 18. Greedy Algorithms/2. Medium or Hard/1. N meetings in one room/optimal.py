class Meeting:
    def __init__(self, start, end, position):
        self.start = start
        self.end = end
        self.position = position


class Solution:
    def maximumMeetings(self, n, start, end):
        meets = [Meeting(start[i], end[i], i + 1) for i in range(n)]
        meets.sort(key=lambda x: (x.end, x.start))
        lastTime = meets[0].end
        count = 1
        for i in range(1, n):
            if meets[i].start > lastTime:
                count += 1
                lastTime = meets[i].end
        return count
