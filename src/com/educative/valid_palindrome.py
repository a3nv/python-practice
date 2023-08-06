def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


if  __name__ == "__main__":
    print(is_palindrome("kayak"))
    print(is_palindrome("hello"))
    print(is_palindrome("RACEACAR"))
    print(is_palindrome("A"))
    print(is_palindrome("ABCDABCD"))