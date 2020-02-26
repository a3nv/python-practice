def witnesses(heights):
    """
    There are n people lined up, and each have a height represented as an integer. A murder has happened right in front
    of them, and only people who are taller than everyone in front of them are able to see what has happened.
    How many witnesses are there?

    Example:
    Input: [3, 6, 3, 4, 1]
    Output: 3
    Explanation: Only [6, 4, 1] were able to see in front of them.
     #
     #
     # #
    ####
    ####
    #####
    36341                                 x (murder scene)
    :param heights:
    :return:
    """
    wit = [heights[0]]  # create a list of witnesses and add first witness there
    for n in range(1, len(heights)):
        """
        Iterate over collection of possible witnesses to the end and compare from real list of witnesses from the last
        """
        cur = heights[n]
        for j in range(len(wit), 0, -1):
            last = wit[j - 1]
            if cur > last:  # if the current witness higher then the last one remove the last one
                del wit[j - 1]
            else:  # otherwise break the loop
                break
        wit.append(cur)  # add new witness to the array
    return len(wit)


def witness_improved(heights):
    tallest = 0
    counter = 0
    for h in heights[::-1]:  # reversing array
        if h > tallest:
            counter += 1
            tallest = h
    return counter


if __name__ == "__main__":
    print(witnesses([3, 6, 3, 4, 1]))  # 3
    print(witness_improved([3, 6, 3, 4, 1]))  # 3
