import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.num_to_indices = {}
        for i, num in enumerate(nums):
            if num not in self.num_to_indices:
                self.num_to_indices[num] = []
            self.num_to_indices[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.num_to_indices[target])
