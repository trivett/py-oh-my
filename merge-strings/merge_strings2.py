def merge_strings(word1, word2):
    index = 0
    stop = min(len(word1), len(word2))
    remainder = word1[stop:] + word2[stop:]
    prefix = ''
    while index < stop:
        prefix = prefix + word1[index] + word2[index]
        index += 1
    return prefix + remainder
