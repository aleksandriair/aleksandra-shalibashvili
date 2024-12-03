import os
import json

def analyze_sales(input_file):
    
    highest_quantity = 0
    highest_quantity_users = []
    total_amount_by_users = {}
    all_order_totals = []
    all_order_quantities = []
    total_quantity_by_products = {}

    
    with open(input_file, "r") as file:
        for line in file:
            user, product, quantity, price = line.strip().split(",")
            quantity = int(quantity)
            price = float(price)
            total = quantity * price
            
            all_order_totals.append(total)
            all_order_quantities.append(quantity)
            
            # ერთ შეკვეთაში მაქსიმალური შესყიდვის რაოდენობა და მომხმარებელი
            if quantity > highest_quantity:
                highest_quantity = quantity
                highest_quantity_users = [user]
            elif quantity == highest_quantity:
                highest_quantity_users.append(user)
                
            # ჯამური ღირებულება მომხმარებლების მიხედვით
            if user not in total_amount_by_users:
                total_amount_by_users[user] = 0
            total_amount_by_users[user] += total
            
            # ჯამური რაოდენობა პროდუქტების მიხედვით
            if product not in total_quantity_by_products:
                total_quantity_by_products[product] = 0
            total_quantity_by_products[product] += quantity
            
    # მაქსიმალური ღირებულების გამნახორციელებელი მომხმარებლის პოვნა
    highest_total = 0
    highest_spending_users = []
    
    for user, total in total_amount_by_users.items():
        if total > highest_total:
            highest_total = total
            highest_spending_users = [user]
        elif total == highest_total:
            highest_spending_users.append(user)
    
    # შესყიდვების ღირებულების საშუალო არითმეტიკულის გამოთვლა
    
    average_order_spending = sum(all_order_totals)/len(all_order_totals)
    
    # შესყიდვების რაოდენობების საშუალო არითმეტიკულის გამოთვლა
    average_order_quantity = sum(all_order_quantities)/len(all_order_quantities)
    
    # ყველაზე დიდი რაოდენობით გაყიდული პროდუქტის პოვნა
    highest_quantity_sold = 0
    highest_sold_products = []
    
    for product, quantity in total_quantity_by_products.items():
        if quantity > highest_quantity_sold:
            highest_quantity_sold = quantity
            highest_sold_products = [product]
        elif quantity == highest_quantity_sold:
            highest_sold_products.append(product)
    
    # შეჯამების გაკეთება
    summary = {
        "highest_quantity_per_order": {
            "quantity": highest_quantity,
            "users": highest_quantity_users
        },
        "highest_total_spending": {
            "amount": highest_total,
            "users": highest_spending_users
        },
        "average_order": {
            "amount": round(average_order_spending, 2),
            "quantity": round(average_order_quantity)
        },
        "highest_sold_products": {
            "quantity": round(highest_quantity_sold),
            "products": highest_sold_products
        }
    }
    
    return summary             
     
def write_summary_in_json(summary, input_file):
    json_path = os.path.join(os.path.dirname(input_file), "stats.json")
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=4) 

       
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))     
    sales_data = os.path.join(script_dir, "data_files", "data.txt")
    
    summary = analyze_sales(sales_data)
    write_summary_in_json(summary, sales_data)

if __name__ == "__main__":
    main()