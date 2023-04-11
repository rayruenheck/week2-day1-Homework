# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop

# Question 1  Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop
for num in range(0,1000):
    num  = num**3
    if num > 1000:
        break
    print(num)

# Question 2 Get first prime numbers up to 100
for num in range(0, 100):
    for i in range(2, num):
        my_mod = num % i
        if my_mod == 0:
            break
    else:
        print(num)
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
user_age = int(input('what is your age?'))
if user_age < 18:
    print('kids')
elif user_age > 65:
    print('senior')
else:
    print('adult')



