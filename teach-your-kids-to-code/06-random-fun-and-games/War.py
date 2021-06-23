import random

suits = ['clubs', 'diamonds', 'hearts', 'spades']
faces = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']

hands = 0
my_score = 0
your_score = 0
tie_count = 0

keep_going = True
while keep_going and (hands < 26):
    hands += 1
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)

    print()
    print("I have the", my_face, "of", my_suit)
    print("You have the", your_face, "of", your_suit)

    if faces.index(my_face) > faces.index(your_face):
        print("I win this round!")
        my_score += 1 + tie_count
        tie_count = 0
    elif faces.index(my_face) < faces.index(your_face):
        print("You win this round!")
        your_score += 1 + tie_count
        tie_count = 0
    else:
        print("It's a tie!")
        tie_count += 1

    answer = input("\nHit [Enter] to keep going, any key to exit: ")
    keep_going = (answer == "")

print("\nGame Over")
print(f"\nThe final score is: you have {your_score}, and I have {my_score}")

if my_score > your_score:
    print ("I win the game!")
elif your_score > my_score:
    print ("You win the game!")
else:
    print ("It was a tie game!")
