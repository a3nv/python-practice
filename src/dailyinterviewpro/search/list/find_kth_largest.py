def find_kth_largest(arr, k):
    """
    Fill this in.
    :param arr:
    :param k:
    :return:
    """
    arr.sort()
    return arr[len(arr) - 3]


if __name__ == "__main__":
    print(find_kth_largest([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))
    # 7
