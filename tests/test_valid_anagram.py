import pytest
from src.valid_anagram import valid_anagram_brute, valid_anagram_optim

test_cases = [
    ('anagram', 'nagaram', True),
    ('rat', 'car', False),
    ('listen', 'silent', True),
]

@pytest.mark.parametrize('s, t, expected', test_cases)
def test_valid_anagram(s, t, expected):
    assert valid_anagram_brute(s, t) == expected
    assert valid_anagram_optim(s, t) == expected