# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
class Solution:
    def canAttend(self, arr):
        # Sort meetings by starting time
        arr.sort(key=lambda x: x[0])
        
        prev_end = arr[0][1]
        
        for i in range(1, len(arr)):
            if arr[i][0] < prev_end:
                return False
            prev_end = arr[i][1]
        
        return True