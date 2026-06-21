class Node:
    def __init__(self, data, next = None):
        self.data = data 
        self.next = next

def print_list(node):
    curr = node 
    while curr.next:
        print(curr.data, end = ' ')
        print("->", end = '')
        curr = curr.next

    print(curr.data)


# using two loops 
# using map 
# using lenght
# using two pointer
def intersectPoint_3(head1, head2):
    c1 = head1 
    c2 = head2 

    while c1 and c2:
        if c1 == c2:
            return c1
        if c1.next is None:
            c1 = head1 
        elif c2.next is None:
            c2 = head2 

        c1 = c1.next
        c2 = c2.next

    return None

# using cycle detection loop
def intersectPoint_4(head1, head2):
    c1 = head1 
    c2 = head2 

    while c1 and c2:
        if c1 == c2:
            return c1
        if c1.next is None:
            c1 = head1 
        elif c2.next is None:
            c2 = head2 

        c1 = c1.next
        c2 = c2.next

    return None



if __name__ == "__main__":

    # creation of first list: 10 -> 15 -> 30
    head1 = Node(10)
    head1.next = Node(15)
    head1.next.next = Node(30)

    print_list(head1)

    

    # creation of second list: 3 -> 6 -> 9 -> 15 -> 30
    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)

    

    # 15 is the intersection point
    head2.next.next.next = head1.next
    print_list(head2)

    intersectionPoint = intersectPoint_1(head1, head2)

    if intersectionPoint is None:
        print("-1")
    else:
        pass
        print(intersectionPoint.data)