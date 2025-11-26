def is_list_library(list_library: list) -> bool:
    """This function is validation of our list


    Args:
        list_library (list): The class of list_library is list

    Returns:
        bool: If our prompt is not list, The output is False and otherwise
        if the type of our list_library is list, the output is True
    """
    if not isinstance(list_library, list):
        return False
    return True
print(is_list_library([1,2,3]))
