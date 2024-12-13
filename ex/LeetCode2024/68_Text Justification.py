# @algorithm @lc id=68 lang=python3 
# @title text-justification


from en.Python3.mod.preImport import *
# @test(["This","is","an","example","of","text","justification."],16)=["This    is    an","example  of text","justification.  "]
# @test(["What","must","be","acknowledgment","shall","be"],16)=["What   must   be","acknowledgment  ","shall be        "]
# @test(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20)=["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            
            if length + len(line) + len(words[i]) > maxWidth:
                extra_space = maxWidth - length
                spaces = extra_space // max(len(line) - 1, 1)
                remainder = extra_space % max(len(line) - 1, 1)
                
                for j in range(max(1,len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))
                line, length = [], 0
            
            
            line.append(words[i])
            length += len(words[i])
            i += 1
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + " " * trail_space)
        
        return res