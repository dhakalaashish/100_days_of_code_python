your_name = input('What is your name?\n').upper()
crush_name = input('What is your crush\'s name? \n').upper()

combined_name = your_name + crush_name

true_digit = str(sum([1 if letter == "T" or letter == "R" or letter == "U" or letter == "E" else 0 for letter in combined_name]))
love_digit = str(sum([1 if letter == "L" or letter == "O" or letter == "V" or letter == "E" else 0 for letter in combined_name]))

love_compatibility = float(true_digit + love_digit)

if love_compatibility >= 80:
    print(f"You guys are meant to be together as penut butter and break, your compatibility {love_compatibility}")
elif love_compatibility >= 60 and love_compatibility < 80:
    print(f"Maybe you guys can work it out, who knows! Your compatability is {love_compatibility}")
else:
    print(f"You are not meant to be together. Forget about your crush! {love_compatibility}")