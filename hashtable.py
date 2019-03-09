#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) Because it iterates over the whole dictionary"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) Because it iterates over the whole dictionary"""
        values = list()
        # Loop through all buckets
        for bucket in self.buckets:
            for key, value in bucket.items():
                values.append(value)
        # Collect all values in each bucket
        return values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) Why and under what conditions?"""
        count = 0
        # Loop through all buckets
        for bucket in self.buckets: # b iterations
            # Count number of key-value entries in each bucket
            count += bucket.length() # O(l)
        return count
        # Overall O(b + l) --> O(n)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(1) or O(n)
        Best case: O(1) - if key is in bucket 0 head
        Worst case: O(n) - if last item is in the ll of the last bucket"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket
        # check out the entry that was returned - is it None?
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is None:
            return False
        else: # entry is not None
            return True

        # shorter version
        # return (entry is not None)

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(n) Why and under what conditions?"""
        # Find bucket where given key belongs
        # Check if key-value entry exists in bucket
        index = self._bucket_index(key) # 0(1) to calculate index
        bucket = self.buckets[index] # 0(1) to index an array

        def key_matcher(key_value):
            return (key_value[0] == key)


        # entry = bucket.find(lambda key_value: key_value[0] == key)

        # If found, return value associated with given key
        entry = bucket.find(key_matcher) # O(1) with l = bucket.length()

        if entry is not None: # found
            return entry[1] # get the value only at index 1
        # Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(l) Why and under what conditions? Best case O(1) item is located near head of list. Otherwise O(l) (find) + O(l) (delete) = O(2*l) simplifies to O(l) if item is near tail of list"""
        # Find bucket where given key belongs
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index] # O(1)
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key) # O(1)
        # If found, update value associated with given key
        if entry is not None:
            bucket.delete(entry) # O(l) worst case
        # Otherwise, insert given key-value entry into bucket
        entry = (key, value) # O(1)
        bucket.append(entry) # O(1)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(l) Overall O(3 + 2L) --> O(l)"""
        # Find bucket where given key belongs
        index = self._bucket_index(key) # O(l)
        bucket = self.buckets[index] # O(l)
        bucket_entry = bucket.find(lambda key_value: key_value[0] == key) # O(l)
        # Check if key-value entry exists in bucket
        if bucket_entry is not None: # O(1)
            # If found, delete entry associated with given key
            bucket.delete(bucket_entry) # O(l)
        # Otherwise, raise error to tell user delete failed
        else:
            # raise err
            raise KeyError('Key not found: {}'.format(key)) # O(1)


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
