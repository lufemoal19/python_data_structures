class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
class my_list:
    def __init__(self):
        self.head = None
        pass
    
    def __str__(self):
        if self.is_empty():
            return "EMPTY LIST"
        iter_node = self.head
        while iter_node:
            print(iter_node, end="\n")
            iter_node = iter_node.next
        else:
            return "END LIST"

    def is_empty(self):
        return True if self.head is None else False
    
    def add(self, data):
        new_node = node(data)
        if self.is_empty(): 
            self.head = new_node
            return True
        iter_node = self.head
        while iter_node.next:
            iter_node = iter_node.next
        iter_node.next = new_node
        return True
    
    def search(self, data):
        if self.is_empty():
            return False
        iter_node = self.head
        while iter_node:
            if iter_node.data is data:
                return True
            iter_node = iter_node.next
        return False
    
class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        pass
    
    def __str__(self):
        return f"User: {self.username} password: {self.password}"

if __name__ == '__main__':
    test = my_list()

    user0 = user("Felipe", "1234")
    user1 = user("Maria", "1234")
    user2 = user("Michelle", "1234")
    user3 = user("Fernando", "1234")
    user4 = user("Saul", "1234")

    test.add(user0)
    test.add(user1)
    test.add(user2)
    test.add(user3)
    test.add(user4)
    

    print(f'Search node data: {test.search(user2)}')

    print(test)