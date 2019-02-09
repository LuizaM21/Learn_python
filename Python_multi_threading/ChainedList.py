

class Node:
    def __init__(self, value, next_pointer=None):
        self.value = value
        self.next_pointer = next_pointer


n1 = Node(101, None)
n2 = Node(102, None)
n3 = Node(103, None)
n4 = Node(104, None)

n1.next_pointer = n2
n2.next_pointer = n3
n3.next_pointer = n4


def list_p(start_pointer):
    """Simple chained list"""
    current_pointer = start_pointer

    while current_pointer is not None:
        print(current_pointer.value, end=" ")
        current_pointer = current_pointer.next_pointer


def insert_poz_0(start_pointer, new_pointer):
    """Return a new start pointer but with new_pointer in the first position"""
    new_pointer.next_pointer = start_pointer
    return new_pointer


print(list_p(n1))

new_p = Node("new_n", None)
new_p1 = Node('new_n1', None)

print(insert_poz_0(list_p, new_p1))


