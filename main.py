import colorama
from colorama import Fore
import random
print(Fore.RED + "Tordi'sbet")
print(Fore.RED + "You are welcome to my betting site")

print("This is a platform that offers you the opportunity to bet and earn a hug amount of money")
started_up = input("To get started, click signup or signin to get started(signup/signin): ")

first_name = input("first name: ")
middle_name = input("Midlle name: ")
last_name = input("Last name: ")
date_of_birth = input("Enter your date of birth here: ")
sex = input("Enter your sex (M/F)")
number = input("Enter your mobile number here: ")
country = input("Enter your country here: ")

#print("Thank your for signing in........")

print("Bet zero is a visual betting were the player is expected to select a number at random")
print("To get started, click YES to get sterted and NO to cancel (YES/NO)")
game_set = input("click to select the level of game you want to play.....(1/2/3/4/5): ")

level_1 = 'You are expected to select a number at random from 0-10 to win a sum of 5,000 naira'
level_2 = 'You are expected to select a number at random from 0-15 to win a sum of 10,000 naira'
level_3 = 'You are expected to select a number at random from 0-20 to win a sum of 20,000 naira'
level_4 = 'You are expected to select a number at random from 0-30 to win a sum of 50,000 naira'
level_5 = 'You are expected to select a number at random from 0-50 to win a sum of 100,000 naira'

first_select = input("Choose number at random of your choice you want to play for first level here: ")
first_game = random.randrange(0, 10)
if(first_select == first_game):
    print("You have won the game, kindly redeem your prize.....")
else:
    print("You have entered a wronge code... please try again...")
print(first_game)

second_select = input("Choose number at random of your choice you want to play for second here: ")
second_game = random.randrange(0, 15)
if("second_select == second_game"):
    print("You have won the game, kindly redeem your prize.....")
else:
    print("You have entered a wronge code... please try again...")
print(second_game)

third_select = input("Choose number at random of your choice you want to play for third level here: ")
third_game = random.randrange(0, 20)
if(third_select == third_game):
    print("You have won the game, kindly redeem your prize.....")
else:
    print("You have entered a wronge code... please try again...")
print(third_game)

forth_select = input("Choose number at random of your choice you want to play for forth level here: ")
forth_game = random.randrange(0, 30)
if(forth_game == forth_select):
    print("You have won the game, kindly redeem your prize.....")
else:
    print("You have entered a wronge code... please try again...")
print(third_game)

fifth_select = input("Choose number at random of your choice you want to play for fifth level here: ")
fifth_game = random.randrange(0, 50)
if(fifth_select == fifth_game):
    print("You have won the game, kindly redeem your prize......")
else:
    print("You have entered a wronge code... please try again...")
print(fifth_game)

