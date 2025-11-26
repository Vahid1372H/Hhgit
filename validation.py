def is_list_library(list_library: list) -> bool:
    if not isinstance(list_library, list):
        return False
    return True
print(is_list_library([1,2,3]))
