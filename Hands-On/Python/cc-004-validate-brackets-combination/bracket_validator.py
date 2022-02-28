str1 = input("Please enter a string by using brackets : ")
letter = ""
bracket_output = False
def bracket_validator():
    i = len(str1)
    n = 0
    while 0 != i:
        i = i - 1
        letter = str1[n]
        n = n + 1
        if letter == "(":
           letter_par = str1(n)
           if letter_par == ")":
               bracket_output = True
        elif letter == "[":
            letter_braket = str1(n)
            if letter_braket == "]":
                bracket_output = True
        elif letter == "{":
            letter_curly = str1(n)
            if letter_curly == "}":
                bracket_output = True

print(f"Your input is {str1} --- Output is {bracket_output}")


    
    


        

        
            

