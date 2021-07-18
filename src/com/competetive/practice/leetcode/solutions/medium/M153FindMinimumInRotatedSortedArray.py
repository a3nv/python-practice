from typing import List


def binary_search(nums: List[int]) -> int:
    """
    153. Find minimum in rotate array
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
    :param nums:  input array
    :return: minimum element from the array
    """
    r = len(nums) - 1
    if r == 1:
        return nums[0]
    if nums[0] < nums[r]:
        return nums[0]
    l = 0
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] > nums[m + 1]:
            return nums[m + 1]
        if nums[m - 1] > nums[m]:
            return nums[m]
        if nums[m] > nums[0]:
            l = m + 1
        else:
            r = m - 1


if __name__ == "__main__":
    print(binary_search([3, 4, 5, 1, 2]))
    print(binary_search([4, 5, 6, 7, 0, 1, 2]))
    print(binary_search([11, 13, 15, 17]))
