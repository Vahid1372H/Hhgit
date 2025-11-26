from fixtures import library

def add_book(title: str, author:str, year: str) -> list:
    try:
        if isinstance(library or title or author or year, list):
            library.append({"title":title, "author": author, "year":year})
            return library
        else:
            return "Error..."
    except ValueError as v:
        return f"The value is incorrect: str{(v)}"
print(add_book("qc", "ahmad", "2025"))