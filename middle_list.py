class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # create Node and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printMiddle(self):
        temp = self.head
        count = 0

        while(self.head.next):


            count += 1
            self.head=self.head.next

        while count==0:

             temp=self.head
             count=count-1
        print(temp.data)



llist = LinkedList()
llist.push(1)
llist.push(20)
llist.push(100)
llist.push(15)
llist.push(35)
llist.push(44)
llist.printMiddle()