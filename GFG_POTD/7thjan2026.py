#Count distinct elements in every window
class Solution:
    def countDistinct(self, arr, k):
        from collections import defaultdict
        
        freq = defaultdict(int)
        result = []
        
        # First window
        for i in range(k):
            freq[arr[i]] += 1
        
        result.append(len(freq))
        
        # Sliding window
        for i in range(k, len(arr)):
            # Remove element going out
            outgoing = arr[i - k]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]
            
            # Add new element
            incoming = arr[i]
            freq[incoming] += 1
            
            result.append(len(freq))
        
        return result
