def merge_strings(word1, word2):
    index = 0
    stop = max(len(word1), len(word2))
    answer = ''
    while index <= stop:
        answer = answer + ''.join(valid_chars(word1, word2, index))
        index += 1
    return answer


def char_at(word, index):
    if len(word) >= index + 1:
        return word[index]
    return None


def not_null(o):
    if o is not None:
        return True
    return False


def valid_chars(word1, word2, index):
    return list(
        filter(not_null, [char_at(word1, index), char_at(word2, index)])
    )
