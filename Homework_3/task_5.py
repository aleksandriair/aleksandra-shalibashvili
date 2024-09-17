from forex_python.bitcoin import BtcConverter
import datetime

purchase_year = int(input("Please enter the year of BitCoin purchase: "))
purchase_month = int(input("Please enter the month of your purchase: "))
purchase_day = int(input("Please enter the day of your purchase: "))
purchase_usd = int(input("Please enter the amount in USD that you spent on the purchase: "))

date_obj = datetime.datetime(purchase_year,purchase_month,purchase_day)
b = BtcConverter()
bitcoin_price_then = int(b.get_previous_price('USD',date_obj))
bitcoin_amount = purchase_usd / bitcoin_price_then

bitcoin_price_now = b.get_latest_price('USD')
bitcoin_value_now = bitcoin_price_now * bitcoin_amount

net_benefit = round((bitcoin_value_now - purchase_usd),2)

if net_benefit > 0:
    print("Congratulations! Your total profit equals",net_benefit)
elif net_benefit < 0:
    print("Oopsie! You have lost a total of",net_benefit)
else:
    print("You don't have any profit/loss")