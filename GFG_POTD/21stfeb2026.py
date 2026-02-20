# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.
class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        
        h = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
        
        return h