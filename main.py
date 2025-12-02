from fixtures import library

# def add_book(title: str, author:str, year: str) -> list:
#     """we want to get list of library and characteristics and then
#     add the name, title and year of book that we should be add it.

#     Args:
#         title (str): class of title is str
#         author (str): class of author is str
#         year (str): class of year is str

#     Returns:
#         list: our output is list that we add to main list in fixtures
#     """
#     try:
#         if isinstance(library or title or author or year, list):
#             library.append({"title":title, "author": author, "year":year})
#             return library
#         else:
#             return "Error..."
#     except ValueError as v:
#         return f"The value is incorrect: str{(v)}"
# print(add_book("qc", "ahmad", "2025"))


def search_book(library: list) -> list:
        """Created list for show title and author of book that we want to show it

        Args:
            library (list): list of name of book and name of author

        Returns:
            list: The output is just list of name and author
        """
        results = []
        for book in library:
                results.append((book, "ai"))
                results.append((book, "Vahid"))
        return results
print(search_book(["title","author"]))  


