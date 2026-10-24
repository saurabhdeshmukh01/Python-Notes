
# Node Class for Linked List based Stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack Class

class stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node  # Fixes 'top = new_node' shown on slide to bind to self.top

    def pop(self):
        if self.isempty():
            print("Stack is empty.")
            return None
        else:
            temp = self.top
            print("Popped item:", temp.data)
            #popped_node = self.top
            self.top = self.top.next
            temp = None
            #return popped_node.data

    def peek(self):
        if self.isempty():
            return None
        return self.top.data

    def print(self):
        print("Stack contains...")
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        temp =  self.top
        while temp:
            st1.push(Node(temp.data))
            temp =  temp.next
        


s = stack()
st1 = stack()
s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.push(Node(50))
s.reverse()

st1.print()

#print(f"\nPopped item: {s.pop()}")

#print("\nAfter popping:")
#s.print()