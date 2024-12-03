import json
import os

def process_salaries_data(input_file):
    try:
        with open(input_file, "r") as file:
            data = json.load(file)
                
        average_salaries = {}
    
        for dept_id, dept_data in data.items():
            dept_sum = 0
            valid_employees = 0

            for employee in dept_data["employees"]:
                try:
                    salary = employee["salary"]
                    if salary != "None" and salary.isdigit():
                        dept_sum += float(salary)
                        valid_employees += 1
                except (KeyError, ValueError) as e:
                    print(f"Error processing salary data: {e}")
                
            try:
                average_salaries[dept_data["name"]] = round(dept_sum / valid_employees, 2)
            except ZeroDivisionError:
                average_salaries[dept_data["name"]] = None
            
        return average_salaries
    
    except FileNotFoundError:
        print("File not found. Please check the file location and/or name.")

def save_output_as_json(output, output_file):
    with open(output_file, "w") as f:
        json.dump(output, f, indent=4)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "data.json")
    output_file = os.path.join(script_dir, "avg_salaries.json")

    average_salaries = process_salaries_data(input_file)
    save_output_as_json(average_salaries, output_file)
    
    print("\nAverage salaries by department:")
    print("\n".join("{}\t{}".format(k, v) for k, v in average_salaries.items()))

if __name__ == "__main__":
    main()