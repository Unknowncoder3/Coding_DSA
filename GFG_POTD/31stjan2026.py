# Implement k queues in a single array of size n
class kQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        
        self.arr = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        
        self.next = list(range(1, n))
        self.next.append(-1)
        
        self.free = 0

    def enqueue(self, x, qi):
        if self.free == -1:
            return False  # array is full
        
        index = self.free
        self.free = self.next[index]
        
        if self.front[qi] == -1:
            self.front[qi] = index
        else:
            self.next[self.rear[qi]] = index
        
        self.next[index] = -1
        self.rear[qi] = index
        self.arr[index] = x
        
        return True

    def dequeue(self, qi):
        if self.front[qi] == -1:
            return -1
        
        index = self.front[qi]
        self.front[qi] = self.next[index]
        
        self.next[index] = self.free
        self.free = index
        
        return self.arr[index]

    def isEmpty(self, qi):
        return self.front[qi] == -1

    def isFull(self):
        return self.free == -1
