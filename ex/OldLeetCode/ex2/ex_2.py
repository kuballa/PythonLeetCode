# Python code for the above approach
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# recursive function
def addition(temp1, temp2, size1, size2):

    # creating a new Node
    newNode = Node(0)

    # base case
    if temp1 is not None and temp2 is not None and temp1.next is None and temp2.next is None:

        # addition of current nodes which is the last
        # nodes of both linked lists
        newNode.data = (temp1.data + temp2.data)

        # set this current node's link null
        newNode.next = None

        # return the current node
        return newNode

    # creating a node that contains sum of previously
    # added number
    returnedNode = Node(0)

    # if sizes are same then we move in both linked
    # list
    if temp1 is not None and temp2 is not None and size2 == size1:

        # recursively call the function
        # move ahead in both linked list
        returnedNode = addition(temp1.next, temp2.next, size1 - 1, size2 - 1)

        # add the current nodes and append the carry
        newNode.data = (temp1.data + temp2.data) + ((returnedNode.data) // 10)

    # or else we just move in big linked list
    elif temp1 is not None and temp2 is not None:

        # recursively call the function
        # move ahead in big linked list
        returnedNode = addition(temp1, temp2.next, size1, size2 - 1)

        # add the current node and carry
        newNode.data = (temp2.data) + ((returnedNode.data) // 10)

    # this node contains previously added numbers
    # so we need to set only rightmost digit of it
    returnedNode.data = (returnedNode.data) % 10

    # set the returned node to the current node
    newNode.next = returnedNode

    # return the current node
    return newNode

# Function to add two numbers represented by nexted
# list.
def addTwoLists(head1, head2):
    temp1 = head1
    temp2 = head2
    size1 = 0
    size2 = 0

    # calculating the size of first linked list
    while temp1 is not None:
        temp1 = temp1.next
        size1 += 1

    # calculating the size of second linked list
    while temp2 is not None:
        temp2 = temp2.next
        size2 += 1
    returnedNode = Node(0)

    # traverse the bigger linked list
    if size2 > size1:
        returnedNode = addition(head1, head2, size1, size2)
    else:
        returnedNode = addition(head2, head1, size2, size1)

    # creating new node if head node is >10
    if returnedNode.data >= 10:
        ans = Node()
        ans.data = (returnedNode.data) // 10
        returnedNode.data = returnedNode.data % 10
        ans.next = returnedNode
    else:
        ans = returnedNode

    # return the head node of linked list that contains
    # answer
    return ans


def Display(head):
    if head is None:
        return
    while head.next is not None:
        print(str(head.data) + " -> ", end="")
        head = head.next
    print(str(head.data))

# Function that adds element at the end of the Linked
# List
def push(head_ref, d):
    new_node = Node(0)
    new_node.data = d
    new_node.next = None
    if head_ref is None:
        new_node.next = head_ref
        head_ref = new_node
        return head_ref
    last = head_ref
    while last.next is not None and last is not None:
        last = last.next
    last.next = new_node
    return head_ref


# Creating two lists
first = None
second = None
sum = None
first = push(first, 7)
first = push(first, 5)
first = push(first, 9)
first = push(first, 4)
first = push(first, 6)
second = push(second, 8)
second = push(second, 4)
print("First List : ", end="")
Display(first)
print("Second List : ", end="")
Display(second)
sum = addTwoLists(first, second)
print("Sum List : ", end="")
Display(sum)

# This code contributed by Prasad Kandekar(prasad264)