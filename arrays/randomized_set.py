"""
Insert Delete GetRandom O(1)
-----------------------------
Implement a RandomizedSet where insert, remove, and getRandom all operate
in average O(1) time. getRandom must return each element with equal probability.
"""
from typing import Any


import random


class RandomizedSet:

    def __init__(self):
        self.list = []
        self.map = {}
        pass

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.list.append(val)
            self.map[val] = len(self.list) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            indexToRemove: int =self.map[val]
            lastIndex = len(self.list) - 1
            placeholder: int = self.list[lastIndex]
            self.list[indexToRemove] = placeholder
            self.list.pop(lastIndex)
            self.map[placeholder] = indexToRemove
            del self.map[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.list)
        
    


if __name__ == "__main__":
    rs = RandomizedSet()

    # insert
    print("✅" if rs.insert(1) == True else "❌", "insert(1) → True")
    print("✅" if rs.insert(2) == True else "❌", "insert(2) → True")
    print("✅" if rs.insert(1) == False else "❌", "insert(1) → False (already present)")

    # remove
    print("✅" if rs.remove(1) == True else "❌", "remove(1) → True")
    print("✅" if rs.remove(3) == False else "❌", "remove(3) → False (not present)")

    # getRandom — must return 2 (only element)
    result = rs.getRandom()
    print("✅" if result == 2 else "❌", f"getRandom() → {result} (expected 2)")

    # distribution check — insert more elements, verify all are returned
    rs2 = RandomizedSet()
    for v in [10, 20, 30]:
        rs2.insert(v)
    samples = [rs2.getRandom() for _ in range(300)]
    for v in [10, 20, 30]:
        count = samples.count(v)
        status = "✅" if 50 <= count <= 150 else "❌"
        print(f"{status} {v} appeared {count}/300 times (~33% expected)")
