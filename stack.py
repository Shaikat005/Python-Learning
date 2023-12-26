'''The working procedure for stack is:
LIFO- Last in first out.'''
books=[]
books.append("I am shaikat.")
books.append("I am a student.")
books.append("I'm 22 years old")
print(books)

books.pop()
print(books)

books.pop()
print("Now the top book is:",books[-1])


