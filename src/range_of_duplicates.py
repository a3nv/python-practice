def binary_search(arr, x):
    """
    Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a
    target element, x. Return -1 if the target is not found.

    Example:
    Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
    Output: [6,8]

    Input: A = [100, 150, 150, 153], target = 150
    Output: [1,2]

    Input: A = [1,2,3,4,5,6,10], target = 9
    Output: [-1, -1]

    :param arr:
    :param x:
    :return:
    """
    left = 0
    right = len(arr)

    matched_index = -1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            matched_index = mid
            break

        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    if matched_index == -1:
        return [-1, -1]
    else:
        left_index = matched_index
        right_index = matched_index
        val = arr[matched_index]
        res = [matched_index, matched_index]
        while left_index != -1 or right_index != -1:
            if left_index != -1:
                if arr[left_index - 1] == val:
                    left_index -= 1
                else:
                    res[0] = left_index
                    left_index = -1
            if right_index != -1:
                if arr[right_index + 1] == val:
                    right_index += 1
                else:
                    res[1] = right_index
                    right_index = -1
        else:
            return res


if __name__ == "__main__":
    arr = [2, 3, 3, 3, 3, 4, 10, 40]
    x = 3

    print(binary_search(arr, x))

    arr = [2, 3, 4, 10, 10, 10, 40]
    x = 10

    print(binary_search(arr, x))
