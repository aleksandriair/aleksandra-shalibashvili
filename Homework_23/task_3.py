class Student():
    def __init__(self, name):
        self._name = name
        self._scores = []

    @property
    def name(self):
        return self._name

    @property
    def scores(self):
        return self._scores

    def add_score(self, score):
        if 0 <= score <= 100:
            self._scores.append(score)
        else:
            print("Incorrect score")

    def get_average(self):
        if len(self.scores) == 0:
            return f"This student has no scores"
        return sum(self.scores) / len(self.scores)

    def get_scores(self):
        return self.scores


def main():
    student_1 = Student("Abby")
    student_2 = Student("Betsy")
    student_3 = Student("Charissa")

    student_1.add_score(78)
    student_2.add_score(54)
    student_2.add_score(67)
    student_3.add_score(95)
    student_3.add_score(99)
    student_3.add_score(105)

    print(f"The average score of {student_1.name} is {student_1.get_average()}")
    print(f"The average score of {student_2.name} is {student_2.get_average()}")
    print(f"The average score of {student_3.name} is {student_3.get_average()}")


if __name__ == "__main__":
    main()
