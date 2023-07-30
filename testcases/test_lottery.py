from src.lottery import get_last_n_digits, is_match_last_n_digits, get_max_matched_digits, get_price_name, get_winning_price, get_winning_price_from_winning_numbers, get_price_name_from_winning_numbers

def test_get_last_3_digits():
    assert get_last_n_digits("94899145", 3) == "145"

def test_get_last_4_digits():
    assert get_last_n_digits("94899145", 4) == "9145"

def test_get_last_5_digits():
    assert get_last_n_digits("94899145", 5) == "99145"

def test_get_last_6_digits():
    assert get_last_n_digits("94899145", 6) == "899145"

def test_get_last_7_digits():
    assert get_last_n_digits("94899145", 7) == "4899145"

def test_get_last_8_digits():
    assert get_last_n_digits("94899145", 8) == "94899145"

def test_not_match_last_3_digits():
    assert is_match_last_n_digits("94899145", "71143793", 3) == False

def test_match_last_3_digits():
    assert is_match_last_n_digits("94899145", "71143145", 3) == True

def test_get_price_lose_name():
    assert get_price_name("94899145", "71143793") == "沒有中獎"

def test_get_first_prirce_name():
    assert get_price_name("94899145", "94899145") == "頭獎"

def test_get_second_prirce_name():
    assert get_price_name("94899145", "84899145") == "二獎"

def test_get_lose_price():
    assert get_winning_price("94899145", "71143793") == 0

def test_get_sixth_price():
    assert get_winning_price("94899145", "71143145") == 200

def test_get_winning_price_from_winning_numbers():
    winning_numbers = ["94899145", "71143793"]
    number = "71145793"
    assert get_winning_price_from_winning_numbers(winning_numbers, number) == 200

def test_get_price_name_from_winning_numbers():
    winning_numbers = ["94899145", "71143793"]
    number = "71145793"
    assert get_price_name_from_winning_numbers(winning_numbers, number) == "六獎"