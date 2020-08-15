def is_sorted(words, order):
    """
    Fill this in.
    :param words:
    :param order:
    :return:
    """
    mapping = {char: idx for idx, char in enumerate(order)}
    mapping2 = enumerate(order)
    print(mapping)
    print(list(mapping2))

    last_word = [mapping[c] for c in words[0]]
    print(last_word)

    for word in words[1:]:
        current = [mapping[c] for c in word]
        if last_word > current:
            return False
        last_word = current
    return True


if __name__ == "__main__":
    print(is_sorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))  # False
    print(is_sorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))  # True
