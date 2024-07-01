from merge_strings2 import merge_strings


def test_merge_strings():
    assert merge_strings('abc', 'def') == 'adbecf'
    assert merge_strings('abcZZZZ', 'def') == 'adbecfZZZZ'
    assert merge_strings('abc', 'defZZZZ') == 'adbecfZZZZ'
