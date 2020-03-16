def dist(s1, s2):
    x = len(s1) + 1
    y = len(s2) + 1

    A = [[-1 for i in range(x)] for j in range(y)]

    for i in range(0, y):
        for j in range(0, x):
            if i == 0:
                A[i][j] = j
            elif j == 0:
                A[i][j] = i
            elif s1[j - 1] == s2[i - 1]:
                A[i][j] = A[i - 1][j - 1]
            else:
                A[i][j] = 1 + min(
                    A[i - 1][j],
                    A[i][j - 1],
                    A[i - 1][j - 1])
    return A[y - 1][x - 1]


if __name__ == "__main__":
    print(dist("biting", "sitting"))
