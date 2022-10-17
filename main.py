from calendar import c
from errno import WSAESHUTDOWN
from this import d
from art import higher_lower_logo, higher_lower_vs
from higher_lower_data import data
import os
import random
def get_random():
    return random.choice(data)
def compare_data(account):
    #global compare_name, compare_desc, compare_country, compare_follower
    compare_name = account["name"]
    compare_desc = account["description"]
    compare_country = account["country"]
    compare_follower = account["follower_count"]
    return f"{compare_name}, a {compare_desc}, from {compare_country}."
def check_answer(guess, a_follower, b_follower):
    while a_follower>b_follower:
        return guess=='a'
    else:
        return guess=='b'
def game():
    print(higher_lower_logo)
    score = 0
    data_b = get_random()
    #print(data_a)
    #print(data_b)
    game_should_continue = True
    while game_should_continue:
        data_a = data_b
        data_b = get_random()
        while data_a == data_b:
            data_b = get_random()

        print(f"Compare A: {compare_data(data_a)}.")
        print(higher_lower_vs)
        print(f"Against B: {compare_data(data_b)}.")
        account_a_follower = data_a["follower_count"]
        account_b_follower = data_b["follower_count"]
        print(f"{account_a_follower}, {account_b_follower}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        print(guess)
        is_correct = check_answer(guess, account_a_follower, account_b_follower)
        os.system('cls')
        print(higher_lower_logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            
            print(f"Sorry, that's wrong. Final score: {score}")
game()



