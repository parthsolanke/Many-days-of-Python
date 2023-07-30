import os
from art import logo

print(logo)


def max_bid(dict):
    max = 0
    for key in dict:
        if dict[key] > max:
            max = dict[key]
            winner = key
    print(f'Highest bid is {winner}, with ${dict[winner]} of bid amount')


bids = {}
ch = 'yes'
while ch == 'yes':
    name = input("What is your name?: ")
    amt = int(input("Enter amount: "))
    bids[name] = amt

    ch = input("Are there other users who want to bid? (yes/no): ")
    if ch == 'yes':
        os.system('cls')
    else:
        max_bid(bids)
