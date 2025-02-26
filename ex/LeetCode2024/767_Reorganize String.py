# @algorithm @lc id=778 lang=python3 
# @title reorganize-string


from en.Python3.mod.preImport import *
# @test("aab")="aba"
# @test("aaab")=""
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap)
            print(maxHeap, res, char, cnt)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
                print(maxHeap, res, char, cnt)
                print()
        return res