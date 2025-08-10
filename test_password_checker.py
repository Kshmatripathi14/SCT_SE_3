import pytest
from password_checker import check_password_strength

def test_weak_password():
    assert check_password_strength("abc") == "Weak ❌"

def test_medium_password():
    assert check_password_strength("Abcdef12") == "Medium ⚠️"

def test_strong_password():
    assert check_password_strength("Abcdef12@") == "Strong ✅"
