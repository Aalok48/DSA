stack = []


def push():
    element=int(input("Enter a number: "))
    stack.append(element)
    print(f"Element pushed in the stack is: {element}")
    print(f"Stack is: {stack}")


def pop():
    if not stack:
        print("Stack is empty!!!")
    else:
        element = stack.pop()
        print(f"Element popped from stack is: {element}")
        print(f"Stack remained is: {stack}")


while True:
    print("Choose operation: 1.Push 2.Pop 3.Quit")
    option = int(input())
    if option == 1:
        push()
    elif option == 2:
        pop()
    elif option == 3:
        break
    else:
        print("Wrong option!!!")