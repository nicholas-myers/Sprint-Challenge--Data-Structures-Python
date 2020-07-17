class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0
        
    def append(self, item):
        if len(self.storage) < self.capacity:     
            self.storage.append(item)
        elif len(self.storage) == self.capacity:
            self.storage.pop(self.oldest)
            self.storage.insert(self.oldest, item)
            if self.oldest < (self.capacity - 1):
                self.oldest += 1
            elif self.oldest == (self.capacity - 1):
                self.oldest = 0

    def get(self):
        return self.storage