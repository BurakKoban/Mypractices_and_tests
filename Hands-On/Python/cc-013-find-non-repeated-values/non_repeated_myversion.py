products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]

singlebooks = []


for  i in range(len(products)):
    books = products
    book = books[i]
    books.pop(i)
    if book in books:
        pass
    else:
        singlebooks.append(book) 
        
    books.insert(i,book)
for singlebook in singlebooks:
    print(singlebook)

