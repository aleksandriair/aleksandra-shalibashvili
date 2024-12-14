class Inset:
    def __init__(self):
        self.list = []

    def insert(self, element):
        if element not in self.list:
            self.list.append(element)

    def member(self, element):
        return element in self.list

    def remove(self, element):
        if element in self.list:
            self.list.remove(element)
        else:
            raise ValueError("ვერ ვიპოვნე")

    def __str__(self):
        return f"{sorted(self.list)}"


def main():
    my_list = Inset()

    my_list.insert(5)
    my_list.insert(3)

    print(my_list.member(10))
    print(my_list.member(3))

    my_list.remove(3)
    # my_list.remove(7)
    print(my_list)


if __name__ == "__main__":
    main()
