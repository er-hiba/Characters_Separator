word = input("Enter a word: ")
row1 = ""
row2 = ""

for i in range(len(word)):
    if i % 2 == 0:
        row1 += word[i] + " "
    else:
        row2 += word[i] + " "

print("Characters at Odd positions:", row1)
print("Characters at Even positions:", row2)
