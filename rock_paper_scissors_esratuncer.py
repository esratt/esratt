import random
action_list = ["paper", "scissors", "rock"]

computer_score = 0
player_score = 0

total_raund = input("How many rounds do you want play? Please enter a number:")

round_counter = 0

while True:
    round_counter +=1
    print("Round Number:", round_counter)

    computer_choose = random.choice(action_list)
    player_choose = input("Please choose your action:")

    print("Computer's choice :", computer_choose)
    print("Player's choice:", player_choose)



    if computer_choose == player_choose:
        print("Tie !")

    elif computer_choose == "paper":
        if player_choose == "rock":
            print("Ha ha Computer Won")
            computer_score +=1
        else:
            print("Ha ha Player Won")
            player_choose +=1
    elif computer_choose == "rock":
        if player_choose == "scissors":
            print("Waow Computer Won")
            computer_score +=1
        else:
            print("Yes,Player Won")
            player_score +=1
    elif computer_choose == "scissors":
        if player_choose == "paper":
            print("OMG Computer Won")
            computer_score +=1
        else:
            print("OMG Player Won")
            player_score +=1


    if round_counter == int(total_raund):
        break


    if computer_score == player_score :
        print("There is no winner,tie.", computer_score , ":" , player_score)
    elif computer_score > player_score :
        print("The Winner is Computer", computer_score , ":" , player_score)
    elif player_score > computer_score :
        print("The Winner is Player", player_score, ":" , computer_score)