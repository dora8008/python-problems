class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        sum_n = n * (n + 1) // 2
        sum_sq_n = n * (n + 1) * (2 * n + 1) // 6

        sum_arr = sum(arr)
        sum_sq_arr = sum(x * x for x in arr)

        diff = sum_arr - sum_n
        sq_diff = sum_sq_arr - sum_sq_n

        sum_dup_miss = sq_diff // diff

        duplicate = (diff + sum_dup_miss) // 2
        missing = duplicate - diff

        return [duplicate, missing]
