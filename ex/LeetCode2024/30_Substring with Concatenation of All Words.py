# @algorithm @lc id=30 lang=python3 
# @title substring-with-concatenation-of-all-words


from en.Python3.mod.preImport import *
# @test("barfoothefoobarman",["foo","bar"])=[0,9]
# @test("wordgoodgoodgoodbestword",["word","good","best","word"])=[]
# @test("barfoofoobarthefoobarman",["bar","foo","the"])=[6,9,12]
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_freq = {}
        for word in words:
            word_freq[word] = 1 + word_freq.get(word, 0)
        
        word_len = len(words[0])
        window_len = len(words) * word_len

        res = []

        for i in range(len(s) - window_len + 1):
            substr_freq = {}
            j = i

            while j < i + window_len:
                cur_word = s[j:j+word_len]
                if cur_word not in word_freq:
                    break
                substr_freq[cur_word] = substr_freq.get(cur_word, 0) + 1

                if substr_freq[cur_word] > word_freq[cur_word]:
                    break
                j += word_len
            if j == i + window_len:
                res.append(i)
        return res