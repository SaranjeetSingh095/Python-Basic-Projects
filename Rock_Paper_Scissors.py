"""
rock = 0
papper = 1
scissors = 2
"""

print("Select Your Choice -> Rock/Paper/Scissors")
while True:
    from random import randint

    Ai = randint(0,2)


    DICT = {
        "rock": 0,
        "paper": 1,
        "scissors": 2
    }

    reverseDICT = {
        0: "rock",
        1: "paper",
        2: "scissors"
    }

    user = input("Enter Choice: ").lower()

    if user == Ai:
        print("Draw!!")
    elif user == 0 or Ai == 1:
        print(f"You Lose\nThe Oponent Choose {reverseDICT[Ai]}")
    elif user == 0 or Ai == 2:
        print(f"You Win\nThe Oponent Choose {reverseDICT[Ai]}")
    elif user == 1 or Ai == 0:
        print(f"You Lose\nThe Oponent Choose {reverseDICT[Ai]}")
    elif user == 1 or Ai == 2:
        print(f"You Lose\nThe Oponent Choose {reverseDICT[Ai]}")
    elif user == 2 or Ai == 0:
        print(f"You Lose\nThe Oponent Choose {reverseDICT[Ai]}")
    elif user == 2 or Ai == 1:
        print(f"You Lose\nThe Oponent Choose {reverseDICT[Ai]}")

