class List(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def min(self):
        if not self:
            raise ValueError("The list is empty")
        return min(self)

    def max(self):
        if not self:
            raise ValueError("The list is empty")
        return max(self)


def main():
    my_list = List()

    my_list.append(5)
    my_list.append(10)
    my_list.append(3)

    print(my_list.min())
    print(my_list.max())


if __name__ == "__main__":
    main()
