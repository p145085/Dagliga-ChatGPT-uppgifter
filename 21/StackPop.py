#21. Implementera en stack med push- och pop-funktioner.
class Stack:
    def __init__(self):
        # Initialisera stacken som en tom lista
        self.stack = []

    def push(self, item):
        """Lägger till ett element högst upp på stacken."""
        self.stack.append(item)

    def pop(self):
        """Tar bort och returnerar det översta elementet från stacken."""
        if self.is_empty():
            raise IndexError("Pop från en tom stack!")
        return self.stack.pop()

    def peek(self):
        """Returnerar det översta elementet utan att ta bort det."""
        if self.is_empty():
            raise IndexError("Peek på en tom stack!")
        return self.stack[-1]

    def is_empty(self):
        """Kontrollerar om stacken är tom."""
        return len(self.stack) == 0

    def size(self):
        """Returnerar antalet element i stacken."""
        return len(self.stack)


##############

if __name__ == "__main__":
    # Skapa en ny stack
    my_stack = Stack()

    # Lägg till element i stacken
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print(f"Stackens storlek: {my_stack.size()}")  # Output: 3
    print(f"Översta elementet: {my_stack.peek()}")  # Output: 30

    # Ta bort element från stacken
    print(f"Pop: {my_stack.pop()}")  # Output: 30
    print(f"Pop: {my_stack.pop()}")  # Output: 20

    print(f"Stackens storlek: {my_stack.size()}")  # Output: 1
