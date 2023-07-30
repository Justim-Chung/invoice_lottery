winning_numbers = ["94899145", "71143793", "41055355"]

def get_last_n_digits(number, n):
    """Given a number and n, return the last n digit

    Args:
        number (str): the number to get the last n d
        n (int): the number of digits to get from th
    Returns:
        str : the last n digits of the number 
    """
    return number[-n:]

def is_match_last_n_digits(lhs, rhs, n):
    """Given two numbers and n, return True if the last n digits match

    Args:
        lhs (str): the left hand side number
        rhs (str): the right hand side number
        n (int): the number of digits to compare
    Returns:
        bool : True if the last n digits match, False otherwise
    """
    return get_last_n_digits(lhs, n) == get_last_n_digits(rhs, n)

def get_max_matched_digits(lhs, rhs):
    """Given two numbers, return the max number of matched digits

    Args:
        lhs (str): the left hand side number
        rhs (str): the right hand side number
    Returns:
        int : the max number of matched digits
    """
    max_matched_digits = 0
    for i in range(3, 9):
        if is_match_last_n_digits(lhs, rhs, i):
            max_matched_digits = i
    return max_matched_digits
    

def get_price_name(lhs, rhs):
    """Given two numbers, return the price name

    Args:
        lhs (str): the left hand side number
        rhs (str): the right hand side number
    Returns:
        str : the price name
    """
    price_name = ['六獎', '五獎', '四獎', '三獎', '二獎', '頭獎']
    max_matched_digits = get_max_matched_digits(lhs, rhs)
    if max_matched_digits < 3:
        return '沒有中獎'
    else:
        return price_name[max_matched_digits - 3]

def get_winning_price(lhs, rhs):
    """Given two numbers, return the winning price

    Args:
        lhs (str): the left hand side number
        rhs (str): the right hand side number
    Returns:
        int : the winning price
    """
    winning_price = [200, 1000, 4000, 10000, 40000, 200000]
    max_matched_digits = get_max_matched_digits(lhs, rhs)
    if max_matched_digits < 3:
        return 0
    else:
        return winning_price[max_matched_digits - 3]

def get_winning_price_from_winning_numbers(winning_numbers, number):
    """Given a list of winning numbers and a number, return the winning price

    Args:
        winning_numbers (list): a list of winning numbers
        number (str): the number to check
    Returns:
        int : the winning price
    """
    result_p = 0
    for winning_number in winning_numbers:
        result_p += get_winning_price(number, winning_number)
    return result_p

def get_price_name_from_winning_numbers(winning_numbers, number):
    """Given a list of winning numbers and a number, return the price name

    Args:
        winning_numbers (list): a list of winning numbers
        number (str): the number to check
    Returns:
        str : the price name
    """
    result_n = '沒有中獎'
    for winning_number in winning_numbers:
        result_n = get_price_name(number, winning_number)
        if result_n != '沒有中獎':
            break
    return result_n