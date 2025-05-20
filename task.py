import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("welcome")

chance = [rock,scissors,paper]
computerChoice = random.randint(0,2)
userchoice = int(input("please enter your choice \n0 for Rock\n1 for scissor\n2 for paper\n"))

print(f"computer chooses! ")
print(chance[computerChoice])

print("You chooses!!")
print(chance[userchoice])


if computerChoice == 0 and userchoice == 0 :
    print("Draw")

elif computerChoice == 0 and userchoice == 1 :
    print("you loose")


elif computerChoice == 0 and userchoice == 2 :
    print("you win")



elif computerChoice == 1 and userchoice == 0:
    print("you win")

elif computerChoice == 1 and userchoice == 1:
    print("Draw")


elif computerChoice == 1 and userchoice == 2:
    print("you loose")




elif computerChoice == 2 and userchoice == 0:
    print("you loose")

elif computerChoice == 2 and userchoice == 1:
    print("you win")


elif computerChoice == 2 and userchoice == 2 :
    print("Draw")








