user = str(input("Enter Your Paragraph: "))


ignore_spaces = user.replace(" ", "")
Word = str(len(user))
character_count = len(ignore_spaces.strip())


print(f"Character Count -> {character_count}")

#--------------------------------------------------------------------------------------

word_split = user.split()
word_count = len(word_split)
print(f"Word Count -> {word_count}")

#--------------------------------------------------------------------------------------

line_split = user.splitlines()
line_count = len(line_split)
print(f"Line Count -> {line_count}")

#--------------------------------------------------------------------------------------

a1 = user.count(".")
a2 = user.count("?")
a3 = user.count("!")


sentence_count = a1+a2+a3
print(f"Sentance Count -> {sentence_count}")


