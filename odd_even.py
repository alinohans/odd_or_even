import random
inputs = [1,2,3,4,5,6,10]
def userBat(k,pr):
    runs = 0
    out = 0
    while out == 0:
        user_choice = int(input("\nEnter your choice[1-6 or 10]: "))
        computer_choice = random.choice(inputs)
        print("Computer's coice: ",computer_choice)
        if user_choice == computer_choice:
            print("OUT")
            out = 1
            print("Final Total: ",runs)
        else:
            runs += user_choice
            print("Your current runs: ",runs)
            if k == 0 and runs < pr:
                print("Required: ",(pr - runs) + 1)
        if k == 0 and runs > pr:
            out = 1
    return runs

def computerBat(k,ur):
    runs = 0
    out = 0
    while out == 0:
        user_choice = int(input("\nEnter your choice[1-6 or 10]: "))
        computer_choice = random.choice(inputs)
        print("Computers's Choice: ",computer_choice)
        if user_choice == computer_choice:
            print("OUT")
            out = 1
            print("Final Total: ",runs)
        else:
            runs += computer_choice
            print("Computer's current runs: ",runs)
            if k == 1 and runs < ur:
                print("Required: ",(ur - runs) + 1)
        if k == 1 and runs > ur:
            out = 1
    return runs

play = 'Y'
while play == 'Y':
    choice = input("Odd or Even: ")
    user_toss = int(input("Enter your choice[1-6 or 10]: "))
    computer_toss = random.choice(inputs)
    print("Computer's Choice: ",computer_toss)
    print()
    total = user_toss + computer_toss
    if choice == 'Even' or choice == 'even':
        if total % 2 == 0:
            print("You won the toss")
            k = input("Do you want bat or bowl? ")
            if k == 'bat':
                user_bat = 1
            else:
                user_bat = 0
        else:
            print("Computer won the toss")
            user_bat = random.randint(0,1)
            if user_bat == 1:
                print("Computer chooses to bowl first")
            else:
                print("Computer chooses to bat first")    
    else:
        if total % 2 ==0:
            print("Computer won the toss")
            user_bat = random.randint(0,1)
            if user_bat == 1:
                print("Computer chose to bowl first")
            else:
                print("Computer chose to bat first")
        else:
            print("You won the toss")
            k = input("Do you want to bat or bowl? ")
            if k == 'bat':
                user_bat = 1
            else:
                user_bat = 0
    user_runs = 0
    computer_runs = 0
    if user_bat == 1:
        print("\n\nYou are Batting")
        user_runs = userBat(user_bat,computer_runs)
        print("\n\nTarget: ",user_runs+1)
        print("\n\nComputer's Batting")
        computer_runs = computerBat(user_bat,user_runs)   
    else:
        print("\n\nComputer's Batting")
        computer_runs = computerBat(user_bat,user_runs)
        print("\n\nTarget: ",computer_runs+1)
        print("\n\nYou are Batting")
        user_runs = userBat(user_bat,computer_runs)
    print()
    print("Your Total Runs: ",user_runs)
    print("Computer's Total Runs: ",computer_runs)
    if computer_runs > user_runs:
        if user_bat == 0:
            print(f'Computer Won by {computer_runs - user_runs} runs')
        else:
            print("Computer Won by 1 wicket")
        play = 'N'
    elif computer_runs < user_runs:
        if user_bat == 1:
            print(f'\nYou Won by {user_runs - computer_runs} runs')
        else:
            print("You Won by 1 wicket")
        play = 'N'
    else:
        print("Tie")
        play = input("Rematch?(Y/N) ")
print()

 