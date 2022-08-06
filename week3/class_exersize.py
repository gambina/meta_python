class MyFirstClass:
    print('Who wrote this?')

    index = "Author-Book"

    def hand_list(self, philosopher: str, book: str):
        self.philosopher = philosopher
        self.book = book
        print(self.philosopher + " wrote the book: " + self.book)


whodunnit = MyFirstClass()
whodunnit.hand_list('Sun Tzu', 'The Art of War')
