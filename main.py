from fixtures import library

def add_book(title: str, author:str, year: str) -> list:
    """_summary_

    Args:
        title (str): _description_
        author (str): _description_
        year (str): _description_

    Returns:
        list: _description_
    """
    try:
        if isinstance(library or title or author or year, list):
            library.append({"title":title, "author": author, "year":year})
            return library
        else:
            return "Error..."
    except ValueError as v:
        return f"The value is incorrect: str{(v)}"
print(add_book("qc", "ahmad", "2025"))