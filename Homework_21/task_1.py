import json


def read_file(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None


class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = []
        for emp in employees:
            employee = Employee(
                name=emp["name"],
                position=emp["position"],
                salary=int(emp["salary"])
            )
            self.employees.append(employee)

    def average(self):
        if not self.employees:
            return None
        return sum(employee.salary for employee in self.employees) / len(self.employees)

    def max(self):
        if not self.employees:
            return None
        return max(employee.salary for employee in self.employees)

    def min(self):
        if not self.employees:
            return None
        return min(employee.salary for employee in self.employees)

    def positions(self):
        position_counts = {}
        for employee in self.employees:
            if employee.position in position_counts:
                position_counts[employee.position] += 1
            else:
                position_counts[employee.position] = 1
        return position_counts


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary


def main():
    data = read_file("data.json")
    if data:
        for dept_key, dept_data in data.items():
            department = Department(
                name=dept_data["name"],
                description=dept_data["description"],
                employees=dept_data["employees"]
            )

            print(f"\nDepartment: {department.name}")
            print(f"Description: {department.description}")
            print(f"Average salary: {department.average()}")
            print(f"Maximum salary: {department.max()}")
            print(f"Minimum salary: {department.min()}")
            print(f"Position counts: {department.positions()}")


if __name__ == "__main__":
    main()
