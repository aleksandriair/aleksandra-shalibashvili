import json
from collections import defaultdict

def analyze_sales(filename):
    purchases_by_user = defaultdict(list)
    product_quantities = defaultdict(int)
    
    with open(filename, 'r') as f:
        for line in f:
            user, product, amount, price = line.strip().split(',')
            amount = int(amount)
            price = float(price)
            total = amount * price
            
            purchases_by_user[user].append({
                'amount': amount,
                'total': total
            })
            product_quantities[product] += amount
    
    max_quantity = max(
        (sum(p['amount'] for p in purchases), user)
        for user, purchases in purchases_by_user.items()
    )
    max_quantity_users = [
        user for user in purchases_by_user
        if sum(p['amount'] for p in purchases_by_user[user]) == max_quantity[0]
    ]
    
    max_value = max(
        (sum(p['total'] for p in purchases), user)
        for user, purchases in purchases_by_user.items()
    )
    max_value_users = [
        user for user in purchases_by_user
        if sum(p['total'] for p in purchases_by_user[user]) == max_value[0]
    ]
    
    all_purchases = [p for purchases in purchases_by_user.values() for p in purchases]
    avg_value = sum(p['total'] for p in all_purchases) / len(all_purchases)
    avg_quantity = sum(p['amount'] for p in all_purchases) / len(all_purchases)
    
    max_sold = max(product_quantities.values())
    most_sold_products = [
        product for product, quantity in product_quantities.items()
        if quantity == max_sold
    ]
    
    stats = {
        "max_quantity_users": max_quantity_users,
        "max_value_users": max_value_users,
        "average_purchase_value": round(avg_value, 2),
        "average_purchase_quantity": round(avg_quantity, 2),
        "most_sold_products": most_sold_products
    }
    
    with open('stats.json', 'w') as f:
        json.dump(stats, f, indent=4)
    
    return stats

if __name__ == "__main__":
    stats = analyze_sales('data.txt')
    print(json.dumps(stats, indent=4))