import art
import os
print(art.logo)

player_dic = {}
user_name = ""
user_amount = 0

def lets_clear():
    clear = lambda: os.system('clear')
    clear()

def dic_smasher(user_name, user_amount):
    loop_stopper = False
    while loop_stopper == False:
        user_name = input("Please enter your name: ")
        user_amount = int(input("Please enter your bid amount: "))

        player_dic[user_name] = user_amount

        cont = input("Do you want to continue? Yes or No: ").lower()
        if cont == "no":
            loop_stopper = True
            lets_clear()
        else:
            lets_clear()

    #print(player_dic)

def find_the_winner():
    the_winner = max(player_dic, key=player_dic.get)
    print(f"The winner is {the_winner} at ${player_dic[the_winner]}")

dic_smasher(user_name, user_amount)

find_the_winner()
