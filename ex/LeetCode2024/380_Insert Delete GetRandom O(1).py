# @algorithm @lc id=380 lang=python3 
# @title insert-delete-getrandom-o1

import random

class RandomizedSet:

    def __init__(self):
      self.nums = []
      self.length = len(self.nums)

    def insert(self, val: int) -> bool:
      if val in self.nums:
        return False
      else:
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
      if val in self.nums:
        self.nums.remove(val)
        return True
      else:
        return False

    def getRandom(self) -> int:
      if len(self.nums) >= 1:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()