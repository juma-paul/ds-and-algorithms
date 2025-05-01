import pytest
from src.group_anagrams import group_anagrams_brute, group_anagrams_optim

test_cases = [
    (['act','pots','tops','cat','stop','hat'], [['hat'],['act', 'cat'],['stop', 'pots', 'tops']]),
    (['x'], [['x']]),
    ([''], [['']]),
]

def sorted_groups(groups):
    return sorted([sorted(group) for group in groups])

@pytest.mark.parametrize('strs, expected', test_cases)
def test_group_anagrams(strs, expected):
    assert sorted_groups(group_anagrams_brute(strs)) == sorted_groups(expected)
    assert sorted_groups(group_anagrams_optim(strs)) == sorted_groups(expected)