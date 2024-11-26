#27. Implementera en enkel länkad lista.
class Node:
    """En nod i den länkade listan."""
    def __init__(self, data):
        self.data = data  # Innehållet i noden
        self.next = None  # Pekare till nästa nod

class LinkedList:
    """En enkel länkad lista."""
    def __init__(self):
        self.head = None  # Första noden i listan

    def append(self, data):
        """Lägger till ett nytt element i slutet av listan."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # Om listan är tom, gör detta till huvudet
            return
        last = self.head
        while last.next:  # Gå till slutet av listan
            last = last.next
        last.next = new_node  # Lägg till noden i slutet

    def display(self):
        """Skriver ut innehållet i listan."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove(self, key):
        """Tar bort den första noden som innehåller 'key'."""
        current = self.head

        # Om det är huvudet som ska tas bort
        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return

        # Leta efter noden som ska tas bort
        prev = None
        while current is not None and current.data != key:
            prev = current
            current = current.next

        # Om nyckeln inte hittades
        if current is None:
            print(f"Värdet {key} finns inte i listan.")
            return

        # Hoppa över noden
        prev.next = current.next
        current = None

# Exempel på användning
if __name__ == "__main__":
    llista = LinkedList()
    llista.append(10)
    llista.append(20)
    llista.append(30)
    
    print("Innehållet i listan:")
    llista.display()
    
    print("\nTar bort 20 från listan:")
    llista.remove(20)
    llista.display()
    
    print("\nFörsöker ta bort 40 (finns ej):")
    llista.remove(40)
    llista.display()
