str = input("Please enter a string: ")
vowels = "aeiou"
i = 1
is_vowel = [False]
while i < len(str):
    for vowelletter in vowels:
        if str[i-1] == vowelletter:
            is_vowel.append(True)
            
        else:
            is_vowel.insert(i, False) 
    
    if is_vowel[i-1] and is_vowel[i]:
        print("Positive")
    elif i == len(str): 
        print("Negative")    
              
    i += 1
    
    
            
