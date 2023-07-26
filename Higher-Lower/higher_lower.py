import random
import os
from art import logo, vs
from game_data import data  

def evaluate(A, B, G):
    
    if G=='a' and A['follower_count'] > B['follower_count']:
        return True
    
    elif G=='b' and A['follower_count'] < B['follower_count']:
        return True
    
    else:
        if A['follower_count'] < B['follower_count']:
            print('Both of them have same no. of followers')
            return True
        return False

def game():
    
    score = 0
    ans = True
    while ans:
        print(logo)
        a = random.choice(data)
        
        if score > 0:
            print(f'Your score is {score}')
            
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        b = random.choice(data)
        while b == a:
            b = random.choice(data)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

        guess = input("Who has more followers? Type 'A/a' or 'B/b': ").lower()

        ans = evaluate(a, b, guess)
        if ans:
            score += 1
            os.system('cls')
        else:
            os.system('cls')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            print(f"Fact: {a['name']} has {a['follower_count']} million followers")
            print(f"fact: {b['name']} has {b['follower_count']} million followers")

game()