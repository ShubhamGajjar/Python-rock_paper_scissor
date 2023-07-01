import random as rn

while True:
    user_in = input("Enter a choice (rock, paper, scissor) : ")
    cpu_in = ["rock","paper","scissor"]
    cpu_ans = rn.choice(cpu_in)

    print("Your input = "+user_in+", Computer input = "+cpu_ans)

    if user_in == cpu_ans:
        print("Its a draw !, both you have selected : "+user_in)
    elif user_in == "rock":
        if cpu_ans == "scissor":
            print("Rock smashes scissor, You Win")
        else:
            print("Paper blocks Rock, You Lost")
    elif user_in == "paper":
        if cpu_ans == "rock":
            print("Paper blocks Rock, You Won")
        else:
            print("Scissor cuts Paper, You Lost")
    elif user_in == "scissor":
        if cpu_ans == "paper":
            print("Scissor cuts Paper, You Won")
        else:
            print("Rock smashes Scissor, You Lost")

    repeat = input("wanna Play with me, Again ! Enter 'y' to continue : ")
    if repeat != "y":
        break

