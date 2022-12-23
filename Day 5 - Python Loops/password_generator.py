import random
print("Welcome to the PyPassword Generator!")

num_alphabets = int(input("How many alphabets would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

choose_letter = ['alphabet', 'number', 'symbol']
choose_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
choose_number = ['0','1','2','3','4','5','6','7','8','9']
choose_symbol = ['!','@','#','$','%','^','&','*']

total_letters = num_alphabets + num_symbols +num_numbers

password = ''

for i in range(total_letters):
    if (num_alphabets == 0) and ('alphabet' in choose_letter):
        choose_letter.remove('alphabet')
    if (num_numbers == 0) and ('number' in choose_letter):
        choose_letter.remove('number')
    if (num_symbols == 0) and ('symbol' in choose_letter):
        choose_letter.remove('symbol')
    
    choice = random.choice(choose_letter)

    if choice == 'alphabet':
        letter = random.choice(choose_alphabet)
        if random.randint(0,1) == 1:
            letter = letter.upper()
        password = password + letter
        num_alphabets = num_alphabets - 1
    elif choice == 'number':
        letter = random.choice(choose_number)
        password = password + letter
        num_numbers = num_numbers - 1
    else:
        letter = random.choice(choose_symbol)
        password = password + letter
        num_symbols = num_symbols - 1

print(f'Here is your password: {password}')


