class Solution:
    def maxFrequency(self, nums, k, numOperations):
        nums.sort()
        left = 0
        max_freq = 1
        n = len(nums)
        
        for right in range(n):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            window_size = right - left + 1
            max_freq = max(max_freq, min(window_size, numOperations + 1))
        
        return max_freq
