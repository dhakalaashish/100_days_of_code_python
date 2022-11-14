print('Welcome to the tip calculator.')

total_bill = float(input('What was the total bill? $'))

split_among = int(input('How many people to split the bill? '))

tip_percent = float(input('What percentage tip would you like to give? 10, 12, or 15? '))

cost_per_person = (total_bill*(tip_percent/100) + total_bill) / split_among

print('Each person should pay: ${:.2f}'.format(cost_per_person))