class Solution:
    def getPairs(self, arr):
        arr.sort()
        seen = set()
        res = set()

        for num in arr:
            if -num in seen:
                res.add((-abs(num), abs(num)) if num < 0 else (-num, num))
            seen.add(num)

        result = [list(pair) for pair in res]
        result.sort()
        return result
