#29. **Hitta en cykel i en lista:** Kontrollera om en given lista innehåller en cykel (loop).
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def contains_cycle(head):
    if not head or not head.next:
        return False

    slow = head  # Långsam pekare
    fast = head  # Snabb pekare

    while fast and fast.next:
        slow = slow.next          # Rör sig ett steg åt gången
        fast = fast.next.next     # Rör sig två steg åt gången

        if slow == fast:          # Pekarna möts, cykel hittad
            return True

    return False  # Ingen cykel

# Exempelanvändning:
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Skapar en cykel

print(contains_cycle(node1))  # Output: True
