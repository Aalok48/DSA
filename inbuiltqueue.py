# Inbuilt queue in python
# similarly queue has also lifo queue that acts as stack and priorityqueue


import queue

q = queue.Queue()

q.put(10)
q.put(20)
q.put(30)

print(q.get())
