def distance(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))

    if s1[0] == s2[0]:
        return distance(s1[1:], s2[1:])

    return 1 + min(distance(s1[1:], s2),
                   distance(s1, s2[1:]),
                   distance(s1[1:], s2[1:]))


if __name__ == "__main__":
    print(distance("biting", "sitting"))
