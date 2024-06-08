import sys
from typing import List

def twoSumSlow(nums: List[int], k: int, len: int) -> bool:
    for i in range(0, len - 1):
        for j in (i + 1, len - 1):
            if (nums[i] + nums[j] == k):
                return True
    return False

def twoSumHash(nums: List[int], k: int, len: int) -> bool:
    hash = {}

    for i in range(0, len):
        temp = k - nums[i]
        if (temp in hash):
            print("Yes")
            print(temp, hash)
            return
        hash[nums[i]] = i
    print("No")

def main() -> int:
    nums_1 = [2,11,15,7]
    nums_2 = [3,2,4]
    nums_3 = [3,3]

    k_1 = 9
    k_2 = 6
    k_3 = 6

    print(twoSumHash(nums_1, k_1, len(nums_1)))
    return 0

if __name__ == '__main__':
    sys.exit(main())