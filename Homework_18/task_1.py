def process_sales_data(input_file, small_file, high_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    small_purchases = []
    high_purchases = []
    
    for line in lines:
        user, product, amount, price = line.strip().split(',')
        total = float(amount) * float(price)
        
        if total < 10:
            small_purchases.append(line)
        else:
            high_purchases.append(line)
    
    with open(small_file, 'w') as f:
        f.writelines(small_purchases)
        
    with open(high_file, 'w') as f:
        f.writelines(high_purchases)

process_sales_data('data.txt', 'small.txt', 'high.txt')