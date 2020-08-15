def h_index(publications):
    n = len(publications)
    citations = [0] * (n + 1)

    for pub in publications:
        if pub < n:
            citations[pub] += 1
        else:
            citations[n] += 1

    total = 0
    i = n
    while i >= 0:
        total += citations[i]
        if total >= i:
            return i
        i -= 1

    return i


if __name__ == "__main__":
    print(h_index([5, 3, 3, 1, 0]))  # 3
