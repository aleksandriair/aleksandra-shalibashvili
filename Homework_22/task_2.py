class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, element):
        self.queue.append(element)

    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)


def main():
    q = Queue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    print(q.pop())
    print(q.pop())
    print(q.pop())


if __name__ == "__main__":
    main()
