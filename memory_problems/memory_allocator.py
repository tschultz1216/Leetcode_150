FREE = chr(0)

class Allocator:

    def __init__(self, n: int):
        self.data = FREE*n   

    def allocate(self, size: int, mID: int) -> int:
        i = self.data.find(FREE*size)
        if i != -1:
            self.data = self.data[:i] + chr(mID)*size + self.data[i+size:]
        return i

    def freeMemory(self, mID: int) -> int:
        freed = self.data.count(chr(mID))
        self.data = self.data.replace(chr(mID), FREE)
        return freed
