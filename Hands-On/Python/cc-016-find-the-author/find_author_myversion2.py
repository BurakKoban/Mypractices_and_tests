def txtlenght(text):
    txt1 = open(text)
    # txt2 = open("text2.txt")
    print(f"text is opened")
    # print("text2.txt is opened")
    sentences1 = txt1.read().split(".")
    # sentences2 = txt2.read().split(".")
    i = 0
    leng = 0 
    while i < len(sentences1) :
        leng = leng + len(sentences1[i])
        r1 = leng / len(sentences1)
        i += 1
    txt1.close
    print(f"text is closed")
    print(r1)
    
txtlenght(text='text1.txt')  
txtlenght(text='text2.txt') 
aut1 = "Hemingway"
aut2 = "Charles Dickens"
# if r1 < r2: 
#    print(f'The first text belongs to ', aut1 , ' and the second one belongs to ', aut2)
# else:
#    print(f'The first text belongs to ', aut2 , ' and the second one belongs to ', aut1)



