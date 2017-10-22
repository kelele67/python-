class Solution:
    def maxInWindows(self, num, size):
        if size <= 0:
            return []
        result = []
        for i in range(0, len(num)+1-size):
            result.append(max(num[i:i+size]))
        return result