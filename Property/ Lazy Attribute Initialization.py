class Book:
    def __init__ (self,title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self._cached_description = None

    def description(self):
        # Check if the description is already cached
        if self._cached_description is None:
            print("Fetching description...")
            self._cached_description = self.fetch_description()  # Simulate fetching description
        return self._cached_description
    @property
    def fetch_description(self):
        book_details = {
            "name" : f"{self.title}",
            "writer": f"{self.author}",
            "genre": f"{self.genre}"
        }
        return book_details

b1 = Book("a","b","c")
print (b1.description) # This will fetch the description for the first time
print(b1.description)  # This will return the cached description without fetching



