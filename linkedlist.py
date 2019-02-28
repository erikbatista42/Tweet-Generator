#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None # O(1) because it's only doing one thing

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Because we have to iterate through all things. specifically through all the nodes."""
        # TODO: Loop through all nodes and count one for each
        return len(self.items())

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) because we only change the tail (last node)"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) - becuase we just check through the first node and and never loops through all nodes"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if items is near the head of the list
        Worst case running time: O(n) if item is near the tail of the list or not present and we need to loop through all n nodes in the list."""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node is not None:
            if quality(node.data):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""

        current_node = self.head
        previous_node = None


        if self.head == item and self.length() == 1:
            self.head = None
            self.tail = None
        # if the head is the node we want to delete
        if current_node and current_node.data == item:
            self.head = current_node.next
            current_node = None
            return

        if self.tail.data == item:
            while current_node is not self.tail:
                current_node = current_node.next
                if current_node.next.data == self.tail.data:
                    previous_node = current_node
                    self.tail = previous_node
                    previous_node.next = None

        # pre_node.next = curre_node.next

        # while current_node and current_node.data not None

        # if current_node != None:

        # TODO: Loop through all nodes to find one whose data matches given item
        # while current_node is not None:
        #     if current_node.data == item:

        #     # TODO: Update previous node to skip around node with matching data
        #     else:
        #         # Otherwise raise error to tell user that delete has failed
        #         raise ValueError('Item not found: {}'.format(item))





def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
