# Stack using Collections

import collections
import queue

stack = collections.deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(f"The stack is {stack}")
while len(stack) != 0:
    x = stack.pop()
    print(f"Popped element is {x}")
    print(f"Stack remaining is {stack}")


# Stack using Queue

stack = queue.LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)
print(f"The stack is {stack}")
while True:
    x = stack.get()
    print(f"Popped element is {x}")
    print(f"Stack remaining is {stack}")
