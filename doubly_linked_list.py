# write a functio to print node values in reverse order in dll
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Case 1: Node to delete is the head
        if temp.data == value:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            temp = None
            return

        # Search for the node to delete
        while temp is not None and temp.data != value:
            temp = temp.next

        # Value not found
        if temp is None:
            print("Value is not present in the list")
            return

        # Case 2: Node is in the middle or end
        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next

        temp = None

    def print(self):
        if self.head is None:
            print("\nList is empty")
            return

        temp = self.head
        print("\nList elements:", end=" ")
        while temp:
            print(temp.data, end=" <-> " if temp.next else "")
            temp = temp.next
        print()

    def cnt_occ(self, num):
        temp = self.head
        cnt = 0 
        while temp:
            if temp.data == num:
                cnt += 1
            temp = temp.next
        print("The occurance: ", cnt)


# Example Usage:
if __name__ == "__main__":
    dll = LinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.print()

    dll.delete(20)
    dll.print()

    dll.delete(50)  # Prints: Value is not present in the list.