#22. Implementera en kö och prioritetskön.

class Queue:
    def __init__(self):
        """Initierar kön som en tom lista."""
        self.queue = []

    def enqueue(self, item):
        """Lägger till ett element längst bak i kön."""
        self.queue.append(item)

    def dequeue(self):
        """Tar bort och returnerar det första elementet i kön."""
        if self.is_empty():
            raise IndexError("Dequeue från en tom kö!")
        return self.queue.pop(0)

    def peek(self):
        """Returnerar det första elementet utan att ta bort det."""
        if self.is_empty():
            raise IndexError("Peek på en tom kö!")
        return self.queue[0]

    def is_empty(self):
        """Kontrollerar om kön är tom."""
        return len(self.queue) == 0

    def size(self):
        """Returnerar antalet element i kön."""
        return len(self.queue)

#####

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(f"Första elementet: {q.peek()}")  # Output: 1
    print(f"Dequeue: {q.dequeue()}")  # Output: 1
    print(f"Köns storlek: {q.size()}")  # Output: 2

#####

import heapq  # Python har en färdig heap-implementation

class PriorityQueue:
    def __init__(self):
        """Initierar prioritetskön som en tom lista."""
        self.priority_queue = []

    def enqueue(self, item, priority):
        """Lägger till ett element med prioritet."""
        heapq.heappush(self.priority_queue, (priority, item))

    def dequeue(self):
        """Tar bort och returnerar elementet med högst prioritet."""
        if self.is_empty():
            raise IndexError("Dequeue från en tom prioritetskön!")
        return heapq.heappop(self.priority_queue)[1]

    def peek(self):
        """Returnerar elementet med högst prioritet utan att ta bort det."""
        if self.is_empty():
            raise IndexError("Peek på en tom prioritetskön!")
        return self.priority_queue[0][1]

    def is_empty(self):
        """Kontrollerar om prioritetskön är tom."""
        return len(self.priority_queue) == 0

    def size(self):
        """Returnerar antalet element i prioritetskön."""
        return len(self.priority_queue)

#####

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Låg prioritet", 3)
    pq.enqueue("Hög prioritet", 1)
    pq.enqueue("Medelhög prioritet", 2)

    print(f"Första elementet: {pq.peek()}")  # Output: Hög prioritet
    print(f"Dequeue: {pq.dequeue()}")  # Output: Hög prioritet
    print(f"Dequeue: {pq.dequeue()}")  # Output: Medelhög prioritet
    print(f"Dequeue: {pq.dequeue()}")  # Output: Låg prioritet
