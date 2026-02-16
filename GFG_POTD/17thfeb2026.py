class Solution:
    def overlapInt(self, arr):
        events = []
        
        # Create events
        for start, end in arr:
            events.append((start, 1))      # interval starts
            events.append((end + 1, -1))   # interval ends (inclusive)
        
        # Sort events by time
        events.sort()
        
        max_overlap = 0
        curr = 0
        
        # Sweep line
        for _, delta in events:
            curr += delta
            max_overlap = max(max_overlap, curr)
        
        return max_overlap