class ListNode(object):

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return str(self.val)
        return str(self.val) + ' ' + str(self.next)
