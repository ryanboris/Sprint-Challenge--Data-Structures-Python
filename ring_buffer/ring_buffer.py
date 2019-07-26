class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def __str__(self):
        print(
            f'current: {self.current}, storage: {self.storage}, capacity: {self.capacity}')

    def append(self, item):
        if self.current == self.capacity:
            self.current = 0
            self.storage[0] = item

        self.storage[self.current] = item
        self.current += 1

    def get(self):
        filtered = list(filter(lambda x: (x is not None), self.storage))
        return filtered
