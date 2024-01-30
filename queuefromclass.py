# Queue from deque of collections module

import collections


q = collections.deque()


def appendleft():
    print("Enter a number: ")
    num = int(input())
    q.appendleft(num)
    print(f"The Queue is {q}")


def popright():
    if len(q) > 0:
        num = q.pop()
        print(f"The queue is {q} and element popped is {num}")
    else:
        print("Empty queue")


def show():
    print(f"The Queue is {q}")


while True:
    print("Select an operation to perform 1.Add 2.Delete 3.Show 4.Quit")
    choice = int(input())
    if choice == 1:
        appendleft()

    elif choice == 2:
        popright()

    else:
        exit()
