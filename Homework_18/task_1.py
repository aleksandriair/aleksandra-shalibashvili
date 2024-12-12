import os

def process_sales_data(input_file, small_file, high_file):
    with open(input_file, "r") as file:

        small_purchases = []
        high_purchases = []
    
        for line in file:
            user, product, amount, price = line.strip().split(",")
            total = int(amount) * float(price)
        
            if total < 10:
                small_purchases.append(line)
            else:
                high_purchases.append(line)
        
    with open(small_file, "w") as file:
        file.writelines(small_purchases)
        
    with open(high_file, "w") as file:
        file.writelines(high_purchases)
        
    print(small_purchases)
    print(high_purchases)

def main():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
        
    input_file = os.path.join(script_dir, "data_files", "data.txt")
    small_file = os.path.join(script_dir, "data_files", "small.txt")
    high_file = os.path.join(script_dir, "data_files", "high.txt")
    
    process_sales_data(input_file, small_file, high_file)

if __name__ == "__main__":
    main()