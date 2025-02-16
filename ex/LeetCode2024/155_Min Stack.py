# @algorithm @lc id=155 lang=python3 
# @title min-stack

class MinStack:

  def __init__(self):
    self.stack = []
    self.min = []
    
  def push(self, val: int) -> None:
    self.stack.append(val)
    if not self.min_max:
      self.min_max.append(val)
    else:
      if val < self.min[-1]:
        self.min.append(val)
      else:
        self.min.append(self.min[-1])

  def pop(self) -> None:
    self.stack.pop()
    self.min.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.min[-1]