# @algorithm @lc id=274 lang=python3 
# @title h-index


from en.Python3.mod.preImport import *
# @test([3,0,6,1,5])=3
# @test([1,3,1])=1
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = len(citations)
        citation_buckets = [0] * (papers + 1)

        for citation in citations:
            citation_buckets[min(citation, papers)] += 1

        cumulative_papers = 0
        for h_index in range(papers, -1, -1):
            cumulative_papers += citation_buckets[h_index]
            if cumulative_papers >= h_index:
                return h_index