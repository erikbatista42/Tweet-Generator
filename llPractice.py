class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node


    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class LinkedList(object):

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
print(myList.get_size())
