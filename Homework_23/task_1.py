class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def get_info(self):
        return f"{self.name}, {self.age}"


def main():
    person_1 = Person("Aleksandra", 27)
    person_2 = Person("Nick", 30)
    person_3 = Person("Michael", 35)

    print(person_1.get_info())
    print(person_2.get_info())
    print(person_3.get_info())

if __name__ == "__main__":
    main()