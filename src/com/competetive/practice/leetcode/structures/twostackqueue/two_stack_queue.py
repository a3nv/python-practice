class Queue:

    def __init__(self):
        """
        Allocate two arrays
        """
        self.q1 = []
        self.q2 = []

    def enqueue(self, val):
        """
        On enqueue pt only in the first stack
        :param val:
        :return:
        """
        self.q1.append(val)

    def dequeue(self):
        """
        On dequeue if the second stack is not empty pop from it, otherwise put from the first stack into the reverse
        order and then pop the last element
        Finally return null if both stacks are empty
        :return:
        """
        if self.q2:
            return self.q2.pop()
        if self.q1:
            while self.q1:
                self.q2.append(self.q1.pop())
            return self.q2.pop()
        return None


if __name__ == "__main__":
    """
    Should return 1 2 3
    """
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
