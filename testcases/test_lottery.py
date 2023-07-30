from src.lottery import get_last_n_digits, is_match_last_n_digits, get_max_matched_digits, get_price_name

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