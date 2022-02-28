i = 1
numbers = []

while i <= 5 :
    addtolist = int(input(f"Please Enter 5 numbers, Your {i}. entry: "))
    i+=1
    numbers.append(addtolist)
largest = numbers[0]

for number in numbers:
    
    if number > largest:
        largest = number
   

print(f""" Largest number: {largest} 
    out of all your entries""")