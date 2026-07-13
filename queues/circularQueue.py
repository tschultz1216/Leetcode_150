"""
622. Design Circular Queue
--------------------------
Implement a circular queue (ring buffer) of fixed capacity k backed by a
plain array.  All operations must run in O(1) time without using any
built-in queue / deque.

Data representation:
  - self.buf    : fixed-size list of length k (slots are pre-allocated)
  - self.head   : index of the front element
  - self.size   : number of elements currently stored

Derived values (no extra pointers needed):
  - rear slot   : (self.head + self.size - 1) % k
  - next write  : (self.head + self.size)     % k

Operations:
  isEmpty()  → size == 0
  isFull()   → size == k
  Front()    → buf[head]                       if not empty, else -1
  Rear()     → buf[(head + size - 1) % k]      if not empty, else -1
  enQueue(v) → write to buf[(head + size) % k], increment size
  deQueue()  → advance head = (head + 1) % k, decrement size

  Time:  O(1) for every operation
  Space: O(k)

Example — k = 3:
  enQueue(1): buf=[1,_,_] head=0 size=1
  enQueue(2): buf=[1,2,_] head=0 size=2
  enQueue(3): buf=[1,2,3] head=0 size=3  → full
  deQueue():  buf=[1,2,3] head=1 size=2  (slot 0 is logically freed)
  enQueue(4): buf=[4,2,3] head=1 size=3  → wrap-around write to slot 0
  Front() → buf[1] = 2
  Rear()  → buf[(1+3-1)%3] = buf[0] = 4
"""


from pickle import FALSE


class MyCircularQueue:

    def __init__(self, k: int):
        self.buffer = [0] * k
        self.k = k
        self.size = 0
        self.head = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            rear_slot: int = (self.head + self.size) % self.k
            self.buffer[rear_slot] = value
            self.size += 1
            return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.head = (self.head + 1) % self.k
            self.size -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[(self.head + self.size - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    # Reproduces the LeetCode example exactly
    q = MyCircularQueue(3)
    tests = [
        ("enQueue", 1, True),
        ("enQueue", 2, True),
        ("enQueue", 3, True),
        ("enQueue", 4, False),   # full
        ("Rear",    None, 3),
        ("isFull",  None, True),
        ("deQueue", None, True),
        ("enQueue", 4, True),
        ("Rear",    None, 4),
    ]

    for op, arg, expected in tests:
        result = getattr(q, op)(arg) if arg is not None else getattr(q, op)()
        status = "✅" if result == expected else "❌"
        call   = f"{op}({arg})" if arg is not None else f"{op}()"
        print(f"{status} {call:<18} → got {result!r:<6}  expected {expected!r}")
