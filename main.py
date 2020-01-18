from view.view_book import*
from view.input_book import*
from core.baseapp import BaseApp


class MainApp(BaseApp):
    def __init__(self):
        self.books = []

    def list_book(self):
         ViewBook.list(self)

    def add_book(self):
         InputBook.input(self)

         #InputBook.search(self)
        #SearchHelper.search.title(self)

if __name__ == "__main__":
    app = MainApp()
    app.run()

