from typing import List


def search(numbers: List[int], key_value: int) -> int:
    head, tail = 0, len(numbers) - 1
    while head <= tail:
        mid = (head + tail) // 2
        if numbers[mid] == key_value:
            return mid
        if numbers[mid] > key_value:
            tail = mid - 1
        else:
            head = mid + 1
    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 0
    print(search(nums, target))
    target = 2
    print(search(nums, target))

