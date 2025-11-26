def is_list_library(list_library: list) -> bool:
    """_summary_

    Args:
        list_library (list): _description_

    Returns:
        bool: _description_
    """
    if not isinstance(list_library, list):
        return False
    return True
print(is_list_library([1,2,3]))
