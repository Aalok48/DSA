# Queue using list
# Queue means insertion from one end and deletion from another end... so queue is open from both ends

queue = []


def enqueue():
    print("Enter the element you want to add to queue: ")
    num = int(input())
    queue.insert(0, num)
    print(f"The Queue is {queue}")


def dequeue():
    if len(queue) > 0:
        num = queue.pop()
        print(f"The Queue is {queue} and the element removed is {num}")
    else:
        print("Empty queue")


def show():
    print(f"The Queue is {queue}")


while True:
    print("Select the operation you want to perform 1.Add 2.Remove 3.Show 4.Quit")
    choice = int(input())
    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        show()

    else:
        exit()
