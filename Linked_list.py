# Node blueprint: Each node stores one data value and points to next
class Node:
    def __init__(self, data_value):
        self.data_value = data_value
        self.next_node = None


# Singly Linear Linked List (sll)
class SinglyLinkedList:
    def __init__(self):
        # 1. Create Linked List: list starts completely empty
        self.head_node = None

    # Helper method to add items to the end easily
    def append_node(self, new_value):
        new_node = Node(new_value)
        if self.head_node is None:
            self.head_node = new_node
            return

        current_node = self.head_node
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = new_node

    # 2. Traverse and print the node values
    def traverse_and_print(self):
        if self.head_node is None:
            print("List is empty!")
            return

        current_node = self.head_node
        print("Linked List: ", end="")
        while current_node is not None:
            print(current_node.data_value, end=" -> ")
            current_node = current_node.next_node
        print("None")

    # 3. Insert node at a specific position (1-based index)
    def insert_at_position(self, new_value, target_position):
        new_node = Node(new_value)

        # If user wants to insert at the very beginning (position 1)
        if target_position == 1:
            new_node.next_node = self.head_node
            self.head_node = new_node
            return

        current_node = self.head_node
        current_step = 1

        # Walk until we reach just before target position
        while current_node is not None and current_step < target_position - 1:
            current_node = current_node.next_node
            current_step += 1

        # If position is invalid (beyond list length + 1)
        if current_node is None:
            print("Invalid position! Out of range.")
            return

        # Insert the new node in between
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    # 4. Find Middle node and print its value (using slow and fast pointers)
    def find_middle_node(self):
        if self.head_node is None:
            print("List is empty! No middle node.")
            return

        slow_pointer = self.head_node
        fast_pointer = self.head_node

        # fast moves 2 steps, slow moves 1 step
        while fast_pointer is not None and fast_pointer.next_node is not None:
            slow_pointer = slow_pointer.next_node
            fast_pointer = fast_pointer.next_node.next_node

        print(f"Middle node value is: {slow_pointer.data_value}")

    # 5. Delete node by matching value
    def delete_node_by_value(self, target_value):
        if self.head_node is None:
            print("List is empty! Nothing to delete.")
            return

        # If the head node itself has the target value
        if self.head_node.data_value == target_value:
            self.head_node = self.head_node.next_node
            print(f"Deleted node with value {target_value}.")
            return

        current_node = self.head_node
        previous_node = None

        while current_node is not None and current_node.data_value != target_value:
            previous_node = current_node
            current_node = current_node.next_node

        # Target value not found
        if current_node is None:
            print(f"Value {target_value} not found in the list.")
            return

        # Unlink the node from the chain
        previous_node.next_node = current_node.next_node
        print(f"Deleted node with value {target_value}.")

    # 6. Reverse list
    def reverse_list(self):
        previous_node = None
        current_node = self.head_node

        while current_node is not None:
            next_temp_node = current_node.next_node  # Save next node
            current_node.next_node = previous_node    # Flip arrow backwards
            previous_node = current_node             # Shift previous forward
            current_node = next_temp_node            # Shift current forward

        self.head_node = previous_node
        print("List has been reversed.")

    # 7. Calculate sum of every two consecutive node values
    def sum_of_consecutive_nodes(self):
        if self.head_node is None or self.head_node.next_node is None:
            print("Need at least 2 nodes to calculate consecutive sum.")
            return

        current_node = self.head_node
        pair_number = 1

        print("Consecutive Pair Sums:")
        while current_node.next_node is not None:
            first_val = current_node.data_value
            second_val = current_node.next_node.data_value
            pair_sum = first_val + second_val
            print(f"Pair {pair_number} ({first_val} + {second_val}) = {pair_sum}")
            
            current_node = current_node.next_node
            pair_number += 1


# Driver code / Testing all 7 operations
# 1. Create Linked List
my_sll = SinglyLinkedList()

# Add starting numbers: 10 -> 20 -> 30 -> 40
my_sll.append_node(10)
my_sll.append_node(20)
my_sll.append_node(30)
my_sll.append_node(40)

# 2. Traverse and print
print("2. Traverse & Print")
my_sll.traverse_and_print()

# 3. Insert at specific position (insert 25 at position 3)
print("\n3. Insert at Position")
my_sll.insert_at_position(25, 3)
my_sll.traverse_and_print()

# 4. Find Middle node
print("\n4. Find Middle Node")
my_sll.find_middle_node()

# 5. Delete node (delete 20)
print("\n5. Delete Node")
my_sll.delete_node_by_value(20)
my_sll.traverse_and_print()

# 6. Reverse list
print("\n6. Reverse List")
my_sll.reverse_list()
my_sll.traverse_and_print()

# 7. Consecutive sum
print("\n7. Consecutive Pair Sums")
my_sll.sum_of_consecutive_nodes()