from src.lottery import get_last_n_digits

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