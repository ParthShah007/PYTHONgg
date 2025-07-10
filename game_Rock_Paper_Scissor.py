# Parth is on a roll...
import random
computer = random.randint(1,3)
print("Welcome to Stone, Paper, Scissor game!")
print("You will be playing against the computer.")
print("Rules: ")
print("Stone beats scissor.")
print("Scissor beats paper.")
print("Paper beats stone.")
print("If both you and the computer choose the same thing, it's a tie.")
print("Enter 1 for Stone, 2 for Paper, and 3 for Scissor.")
print("Let's play!")
you = int(input("Enter a number: "))
dict = {
    1 : "Stone",
    2 : "Paper",
    3 : "scissor",
} 
yournum = dict[you]
comp = dict[computer]
if (you == computer):
    print("You chose: ",yournum)
    print("Computer chose: ",comp)
    print("It's a tie.")
    print("Let's play again!")   
elif (you == 1 and computer == 3) or (you == 2 and computer == 1) or (you == 3 and computer == 2):
    print("You chose: ",yournum)
    print("Computer chose: ",comp)
    print("You win, Woohoo!")
elif (you > 3 or you < 1):
    print("Invalid input. Please enter a number between 1 and 3.")
    print("Let's play again!")
else :
    print ("You chose: ",yournum)
    print ("Computer chose: ",comp)
    print("You lose.. Sed life:(")
    print("Better luck next time!")
print("Thank you for playing!")
