import art
import os

print(art.logo)
print("Welcome to the Secret auction program")

auction_records = {}
while True:
    name = input("What's your name? ")
    bid = int(input("What's your bid: Ksh "))
    auction_records[name] = bid
    response = input("Are there other bidders? Type 'yes' or 'no. ").lower()
    if response == 'yes':
        os.system('cls')
        continue
    else:
        os.system('cls')
        break

print(auction_records)
highest_bid = 0
highest_bid_name = ''
for name in auction_records:
    current_bid = auction_records[name]
    if current_bid >  highest_bid:
        highest_bid_name = name
        highest_bid = current_bid

print(f"The winner is {highest_bid_name} with a bid of Ksh{highest_bid}.")