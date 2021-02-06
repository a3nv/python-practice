def findPythagoreanTriplets(nums):
    """
    Given a list of numbers, find if there exists a pythagorean triplet in that list.
    A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

    Example:
        Input: [3, 5, 12, 5, 13]
        Output: True
    Here, 5^2 + 12^2 = 13^2.
    :param nums: array of numbers
    :return: true - if there is a triplet, otherwise - false
    """

    """
    A brute force solution would require 3 nested for loops to test every combination with 3 variables. 
    However upon closer inspection, we can see that by creating a set of squares of all nums, we can search combinations 
    for just 2 numbers (a and b) instead and see if the sum exists.
    
    The time complexity for this problem is O(n^2), since we have a loop nested in another loop, where each iterates 
    through the list.

    The space complexity would also be O(n), since a set needs to be created to search if the sum of squares exists. 
    """
    squares = set([c ** 2 for c in nums])

    for a in squares:
        for b in squares:
            if a + b in squares:
                return True
    return False


if __name__ == "__main__":
    print(findPythagoreanTriplets([3, 12, 5, 13]))  # True
    print(findPythagoreanTriplets([20, 99, 101]))  # True
    print(findPythagoreanTriplets([60, 91, 109]))  # True
    print(findPythagoreanTriplets([15, 112, 113]))  # True
    print(findPythagoreanTriplets([44, 117, 125]))  # True
    print(findPythagoreanTriplets([88, 105, 137]))  # True
    print(findPythagoreanTriplets([17, 144, 145]))  # True
    print(findPythagoreanTriplets([24, 143, 145]))  # True
    print(findPythagoreanTriplets([51, 140, 149]))  # True
    print(findPythagoreanTriplets([85, 132, 157]))  # True
    print(findPythagoreanTriplets([119, 120, 169]))  # True
    print(findPythagoreanTriplets([52, 165, 173]))  # True
    print(findPythagoreanTriplets([19, 180, 181]))  # True
    print(findPythagoreanTriplets([57, 176, 185]))  # True
    print(findPythagoreanTriplets([104, 153, 185]))  # True
    print(findPythagoreanTriplets([95, 168, 193]))  # True
    print(findPythagoreanTriplets([28, 195, 197]))  # True
    print(findPythagoreanTriplets([84, 187, 205]))  # True
    print(findPythagoreanTriplets([133, 156, 205]))  # True
    print(findPythagoreanTriplets([21, 220, 221]))  # True
    print(findPythagoreanTriplets([140, 171, 221]))  # True
    print(findPythagoreanTriplets([60, 221, 229]))  # True
    print(findPythagoreanTriplets([105, 208, 233]))  # True
    print(findPythagoreanTriplets([120, 209, 241]))  # True
    print(findPythagoreanTriplets([32, 255, 257]))  # True
    print(findPythagoreanTriplets([23, 264, 265]))  # True
    print(findPythagoreanTriplets([96, 247, 265]))  # True
    print(findPythagoreanTriplets([69, 260, 269]))  # True
    print(findPythagoreanTriplets([115, 252, 277]))  # True
    print(findPythagoreanTriplets([160, 231, 281]))  # True
    print(findPythagoreanTriplets([161, 240, 289]))  # True
    print(findPythagoreanTriplets([68, 285, 293]))  # True

    print(findPythagoreanTriplets([68, 285, 111]))  # False
    print(findPythagoreanTriplets([68, 285, 5202]))  # False
