from random import randint

secrate = randint(1,100)

print("Guess Number Between 1-100")
user = int(input("Enter Number > "))

attempt = "1"

while user != secrate:

    attempt += 1

    if secrate == user:
        print("🎉 You Win!")
    

    elif secrate > user:
        print("Too Low! ")
    elif secrate < user:
        print("Too High!")

    user = int(input("Try Again: "))

print("🎉 Congratulations! You Guessed The Correct Number.")
print(f"You Guessed It In {attempt} Attempts.")
