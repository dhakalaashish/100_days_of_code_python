#This program should print each number form 1 to 100 in turn
# When the number is divisible by 3, the instead of printing the number it should print 'Fizz".
# When the number is divisible by 5, the instead of printing the number it should print 'Buzz".
# When the number is divisible by both 3 and 5, the instead of printing the number it should print 'FizzBuzz".
# Each print should be on a different line, and we should also include the number 100.

for i in range(1,101):
    if i%3 == 0 and i%5 != 0:
        print("Fizz\n")
    elif i%5 == 0 and i%3 != 0:
        print("Buzz\n")
    elif i%5 ==0 and i%3==0:
        print("FizzBuzz\n")
    else:
        print(f"{i}\n")
        



