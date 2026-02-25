import random
USER_CHOICES = ("rock","paper","scissor")

def get_user_input():
    choice = input('pick your choice ["rock","paper","scissor"]:  ')
    while choice not in USER_CHOICES:
        choice = input('pick your choice ["rock","paper","scissor"]:  ')
    return choice 

def get_pc_input():
    pc_choice = random.choice(USER_CHOICES)
    print(f"pc choice was : {pc_choice}")
    return pc_choice

def determine_winner(user_input,pc_input):
    if user_input == pc_input:
        return "draw!"
    elif (user_input == "rock" and pc_input == "scissor") \
        or (user_input == "scissor" and pc_input == "paper") \
        or (user_input == "paper" and pc_input == "rock"):
            print("user won")
    else :
        print("pc won")
        
def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input, pc_input)
    print("end of program")
    
    
answer = 'y'
while answer == "y":
    main()
    answer = input("do you want to continue? (y/n):")