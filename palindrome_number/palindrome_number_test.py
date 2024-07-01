from palindrome_number import PalindromeNumber


def test_palindrome_number():
    instance = PalindromeNumber(number=123)

    assert instance.is_palindrome() == False

    assert instance.is_palindrome() == False

    instance = PalindromeNumber(number=222)

    assert instance.is_palindrome() == True

    instance = PalindromeNumber(number=2112)

    assert instance.is_palindrome() == True

    instance = PalindromeNumber(number=21012)

    assert instance.is_palindrome() == True

    instance = PalindromeNumber(number=-21012)

    assert instance.is_palindrome() == True
