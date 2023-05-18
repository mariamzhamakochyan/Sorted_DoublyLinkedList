class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.greater = None
        self.smaller = None

class Sortedlist:
    def __init__(self):
        self.head =  None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        elif data <= self.head.data:
            node.next = self.head
            self.head.prev = node
            self.head.smaller = node
            node.greater = self.head
            self.head = node
        elif data >= self.tail.data:
            node.prev = self.tail
            self.tail.next = node
            self.tail.greater = node
            node.smaller = self.tail
            self.tail = node
        else:
            cur = self.head
            while cur.next and cur.next.data <= data:
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node
            node.greater = cur.next
            node.smaller = cur
            cur.next.smaller = node
            cur.next.greater.prev = node
        self.size += 1
               
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end = " ")
            cur = cur.next
        print()

myList = Sortedlist()
myList.append(21)
myList.append(1)
myList.append(5)
myList.append(7)
myList.append(3)
myList.print_list()
print(f'Size: {myList.size}')