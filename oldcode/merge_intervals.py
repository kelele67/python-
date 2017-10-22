#!/usr/bin/python

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        int_sort = sorted(intervals, key=lambda x: x.start)
        ans, start, end = [], int_sort[0].start, int_sort[0].end
        for n in int_sort[1:]:
            if n.start > end:
                ans.append(Interval(start, end))
                start, end = n.start, n.end
            else:
                end = max(end, n.end)
        ans.append(Interval(start, end))
        return ans


    
intervals = []
input = raw_input().split()
for a in input:
    start, end = a.split(',')
    intervals.append(Interval(start, end))

res = Solution().merge(intervals)
for x in res:
    print x.start + ',' + x.end,
if intervals[-1].end != res[-1].end:
    print intervals[-1].start + ',' + intervals[-1].end