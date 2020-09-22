# Larah Chesnic Student ID: 001106662
class HashMap:

    def __init__(self):
        self.size = 10
        self.map = [None] * self.size
    # adds the ASCII characters in the key and uses modulo function to determine hash
    # Big O is O(n)
    def __get__hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    # new additions are entered with their key and value pairs, the key is sent to the get hash function to determine
    # the hash. if there is no entry with this key already, the key value pair is added to a list. else, the key's
    # value is updated
    # Big O is O(n)
    def add(self, key, value):
        key_hash = self.__get__hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True
    # retrieves value from hashmap using key. finds the hash with the key and searches through list to find the value
    # that matches the key returning the value
    # Big O is O(n)
    def get(self, key):
        key_hash = self.__get__hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    # uses key to locate the hash, if there is no entry with that key, the function will return false
    # else deletes both the key and value pair from the list
    # Big O is O(n)
    def delete(self, key):
        key_hash = self.__get__hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    # for each item in the hash's list, as long as there is an entry, the item is printed
    # Big O is O(n)
    def print(self):
        print('Hashmap key and value pairs')
        for item in self.map:
            if item is not None:
                print(str(item))
