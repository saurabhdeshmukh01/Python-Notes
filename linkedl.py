class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def trav(self):
        curr = self
        while curr != None:
            print(curr.data,end=" --> ")
            curr = curr.next
        print("None")
def inab(head,val):
    newNOde = Node(val)
    newNOde.next = head
    return newNOde
    #head = newNOde
    #print(trav(head))

def inae(head,data):
    newNode = Node(data)

    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newNode
    return head

def inam(head,data,th):
    n = th
    newNode = Node(data)
    curr = head
    for i in range(n-1):
        curr = curr.next
    newNode.next = curr.next
    curr.next = newNode
    return head
def delB(head):
    return head.next
def dele(head):
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head
def delm(head,th):
    n = th
    curr = head
    for i in range(n-1):
        curr = curr.next
    curr.next = curr.next.next
    return head


n1 = Node(6)
n2 = Node(7)
n3 = Node(8)
n4 = Node(4)
head = n1
n1.next = n2
n2.next = n3
n3.next = n4
# head.trav()
head = inab(head,5)
head = inae(head,3)
head = inam(head,9,4)
head = delB(head)
head = dele(head)
head = delm(head,2)
head.trav()
