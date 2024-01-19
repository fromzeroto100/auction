import os 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to the Auction")

new_bid = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")        

while not bidding_finished:
    name = input("Enter your name: ")
    bid = int(input("Enter your offer: $ "))
    new_bid[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no;' ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(new_bid)

    elif should_continue == "yes":
        clear()    
# user_bids = {}

# def bids(name, bid):
#     new_bid = {"name": name, "bid": bid}
#     user_bids.append(new_bid)
#     print("Is there any other bids? Yes or No ")
#     if "yes" or "Yes":
#         clear()
#     else:
            


