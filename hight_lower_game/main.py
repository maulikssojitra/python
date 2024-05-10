import random
import os
from game_data import data
from art import logo, vs

def format_data(account):
    account_name = account["name"]
    account_def = account['description']
    account_country = account['country']
    return f"{account_name}, a{account_def}, from {account_country}"

def check_ans(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

os.system('cls')
print(logo)
score = 0
flag = True
account_b = random.choice(data)

while flag:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Againts B : {format_data(account_b)}")


    guess = input("Who has more followers?, Type 'A' or 'B' : ").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_ans(guess, a_followers, b_followers)

    os.system('cls')
    print(logo)

    if is_correct:
        score += 1
        print(f"You're Right! Current score {score}")
    else:
        flag = False
        print(f"You're Wrong. Final score {score}")