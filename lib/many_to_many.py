class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        Author.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        book.contracts_list.append(contract)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.contracts_list = []
        Book.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]
class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.members.append(self)



