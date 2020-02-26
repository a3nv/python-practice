class MaxStack:
    """
    Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of
    max() which returns the maximum element in the stack (return None if the stack is empty).
    Each method should run in constant time.
    """

    def __init__(self):
        """

        """

    def push(self, val):
        """

        :param val:
        :return:
        """

    def pop(self):
        """

        :return:
        """

    def max(self):
        """

        :return:
        """


# Fill this in.

if __name__ == "__main__":
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    print(s.max())
    # 3
    s.pop()
    s.pop()
    print(s.max())
    # 2
