#Flattening a Linked List


'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        # Base case
        if root is None or root.next is None:
            return root

        # Recursively flatten the right list
        root.next = self.flatten(root.next)

        # Merge current list with flattened right list
        root = self.merge(root, root.next)

        return root

    def merge(self, a, b):
        # If one list is empty
        if a is None:
            return b
        if b is None:
            return a

        # Choose smaller value
        if a.data < b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)

        result.next = None  # VERY IMPORTANT
        return result
