class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.insert(0, element)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(f"Peeking element: {stack.peek()}")
    print(f"Popping element: {stack.pop()}")
    print(f"Peeking element: {stack.peek()}")

    print(f"Stack is empty: {stack.is_empty()}")
    print(f"Stack size: {stack.size()}")

    print(f"Popping element: {stack.pop()}")
    print(f"Popping element: {stack.pop()}")

    print(f"Stack is empty: {stack.is_empty()}")
    print(f"Stack size: {stack.size()}")


if __name__ == "__main__":
    main()
