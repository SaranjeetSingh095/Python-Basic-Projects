from random import randint

# Character Sets
symbols = "!@#$%^&*()_-+=<>?"
numbers = "0123456789"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Allowed Characters
characters = lowercase + uppercase

# User Input
q1 = input("Include Symbols? (y/n): ").lower()
q2 = input("Include Numbers? (y/n): ").lower()

length = int(input("Enter Password Length: "))

# Add Optional Characters
if q1 == "y":
    characters += symbols

if q2 == "y":
    characters += numbers

# Generate Password
password = ""

for _ in range(length):
    index = randint(0, len(characters) - 1)
    password += characters[index]

print("\nGenerated Password:", password)
