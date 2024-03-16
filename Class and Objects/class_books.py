class book():

    def display(self):
        print('Title : ',self.title)
        print('Author : ',self.author)
        print('Publisher : ',self.publisher)
        print('isbn : ',self.isbn)
        print('total_copies : ',self.total_copies)



    def __init__(self ,title,author,publisher,isbn,total_copies):
       self.title = title
       self.author = author
       self.publisher = publisher
       self.isbn = isbn
       self.total_copies = total_copies


title = input('Enter Title : ')
auth = input('Enter Author Name : ')
pub = input('Enter Publisher Name :')
isbn_no = input('Enter isbn number : ')
total = input('Enter total number of copies : ')

obj = book(title , auth , pub , isbn_no, total)
obj.display()



