class Node:
    def __init__(self, stuff):
        self.stuff = stuff
        self.next_one = None

class LinkedList:
    def __init__(self):
        self.first_node = None
    
    def add_stuff(self, stuff):
        new_guy = Node(stuff)
        if self.first_node == None:
            self.first_node = new_guy
        else:
            now_node = self.first_node
            while now_node.next_one != None:
                now_node = now_node.next_one
            now_node.next_one = new_guy
    
    def show_list(self):
        now_node = self.first_node
        while now_node != None:
            print(now_node.stuff, end=" ")
            now_node = now_node.next_one
        print("done")
    
    def delete_nth(self, n):
        if self.first_node == None:
            print("Oops, nothing here!")
            return
        how_many = 0
        temp_node = self.first_node
        while temp_node != None:
            how_many = how_many + 1
            temp_node = temp_node.next_one
        if n < 1 or n > how_many:
            print("Bad number, can’t do that!")
            return
        if n == 1:
            self.first_node = self.first_node.next_one
        else:
            now_node = self.first_node
            steps = 0
            while steps < n - 2:
                now_node = now_node.next_one
                steps = steps + 1
            now_node.next_one = now_node.next_one.next_one

ll = LinkedList()
ll.add_stuff(1)
ll.add_stuff(2)
ll.add_stuff(3)
ll.add_stuff(4)
ll.add_stuff(5)
print("Here’s the list:")
ll.show_list()
ll.delete_nth(3)
print("After deleting 3rd one:")
ll.show_list()