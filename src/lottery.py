price_numbers = ["94899145", "71143793", "41055355"]

def get_last_n_digits(number, n):
    """Given a number and n, return the last n digit

    Args:
        number (str): the number to get the last n d
        n (int): the number of digits to get from th
    Returns:
        str : the last n digits of the number 
    """
    return number[-n:]