# Given an array arr, convert it into a doubly linked list and return the head of the list.


class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data 
        self.next = next 


def array2ll(data):
    head = ListNode(data[0])
    curr = head
    for i in data[1:]:
        new_node = ListNode(i)
        curr.next = new_node
        curr = new_node

    return head

def printll(head):
    curr = head 
    while curr.next is not None:
        print(curr.data, end = '')
        print(" -> ", end = '')
        curr = curr.next

    print(curr.data)





data = [2,3,1,4,5]
head = array2ll(data)
printll(head)
