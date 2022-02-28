class person:
    def __init__(self,name,pnumber): 
        self.name = name
        self.pnumber = pnumber
    

pbook = []
isvalid = True


while isvalid:
  
    entry = input("""Welcome to the phonebook application
1. Find phone number
2. Insert a phone number
3. Delete a person from the phonebook
4. Terminate
Select operation on Phonebook App (1/2/3) :""")
    if entry.isnumeric:  
        if int(entry) == 2:
            p1 = person
            p1.name  = input("Insert name of the person : ")
            p1.pnumber = input("Insert phone number of the person: ")
            if p1.pnumber.isnumeric():
                pbook.append([p1.name,p1.pnumber])
                print(f"Phone number of {p1.name} is inserted into the phonebook")
                
            else:
                print("Invalid input format, cancelling operation ...")
                
        elif int(entry) == 1:
            person_rec = input("Find the phone number of :")
            s = 0
            for rec in pbook:
                if rec[0] == person_rec:
                    print(pbook[s][0]," = ", pbook[s][1])
                    s = s+1                  
                else:
                    print(f"Couldn't find phone number of {person_rec}")
                    
                    
        elif int(entry) == 3:
            del_rec = input("Whom to delete from phonebook : ")
            for drec in pbook:
                if drec[0] == del_rec:
                    pbook.pop()
                    print(f"{del_rec} is deleted from the phonebook")
                else:
                    print(f"No record under {del_rec}")
                    
        elif int(entry) == 4:
            print("Exiting Phonebook")
            isvalid = False
    else:
        print("Your entry is not valid")
        break
       
                    
                    
                
                
            
                
    