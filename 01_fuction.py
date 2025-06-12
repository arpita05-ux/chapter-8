# a = int(input("enter your number: "))
# b = int(input("enter your number: "))
# c = int(input("enter your number: "))


# average  = (a + b + c)/3

# print(average)


# x = int(input("enter your number: "))
# y = int(input("enter your number: "))
# z = int(input("enter your number: "))


# average  = (a + b + c)/3

# print(average)
# if i have to do 50 times them it has to many line in program so we use fuction.

# Fuction 
def avg():
    a = int(input("enter your number: "))
    b = int(input("enter your number: "))
    c = int(input("enter your number: "))

    average  = (a + b + c)/3
    print(average)
    return average   # becase i want actual avg. number .if i use double quote it give string not number.

a = avg()      # Fuction call
print("saved value:", a)
print("Thanks")   
avg()   # now each time i write avg() we can enter no. that time


