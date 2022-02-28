import random
is_valid = True
while is_valid:
    fullname = input("Please enter your full name: ")
    i = 1
    s = 1
    password = ""
    
    while i < 4:
        random_number = random.randint(0, len(fullname))
        password = password + fullname[random_number - 1]
        i = i + 1
        
    while s < 5:
        random_number = random.randint(0, 9)
        password = password + str(random_number)
        s = s + 1
        if s == 5:
            print(f"Your password is {password}")
        
        