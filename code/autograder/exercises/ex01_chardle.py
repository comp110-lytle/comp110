"""My second python program."""

__author__ = "123456789"

word: str = input("Enter a 5-character word: ")
char: str = input("Enter a single character: ")

output: str = "Searching for " + char + " in " + word
print(output)

count: int = 0
if word[0] == char:
    count += 1
if word[1] == char:
    count += 1
if word[2] == char:
    count += 1
if word[3] == char:
    count += 1
if word[4] == char:
    count += 1

if count == 0:
    print("No instances of " + char + " found in " + word)
elif count == 1:
    print("1 instance of " + char + " found in " + word)
else:
    print(str(count) + " instances of " + char + " found in " + word)
