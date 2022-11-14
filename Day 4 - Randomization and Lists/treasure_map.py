row1 = ["🟨", "⬛️", "🟥"]
row2 = ["🟧", "⬜️", "🟫"]
row3 = ["🟪", "🟦", "🟩"]
map = [row1,row2,row3]
print(f'{map[0]}\n\n{map[1]}\n\n{map[2]}')

incorrect_input = True

while incorrect_input:
    try:
        user_input = input("Which block has the treasure?\nEnter the column number followed by the row number.\nFor example enter '13' for the red one!\n")
        col = int(user_input[0])
        row = int(user_input[1])
        incorrect_input = False
    except:
        incorrect_input = True

map[col-1][row-1] = "❌"

print(f"{map[0]}\n\n{map[1]}\n\n{map[2]}")