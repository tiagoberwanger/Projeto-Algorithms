def is_palindrome_recursive(word, low, high):
    if word == "":
        return False
    if word[low] != word[high]:
        return False
    if low > high or low == high:
        return True
    if low < high:
        return is_palindrome_recursive(word, low + 1, high - 1)
