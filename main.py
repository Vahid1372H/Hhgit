from fixtures import library


def add_book(library, title, author, year):
    library.append({"title": title, "author": author, "year": year})
print(add_book((library, "Deep Learning", "Goodfellow", 2016)
))