#2. **Implementera en rekursiv funktion för att lösa Tower of Hanoi-problemet.**
def tower_of_hanoi(n, från, till, mellan):
    """
    Löser Tower of Hanoi-problemet rekursivt.
    
    :param n: Antal skivor
    :param från: Namn på startpinnen
    :param till: Namn på slutpinnen
    :param mellan: Namn på mellanpinnen
    """
    if n == 1:
        print(f"Flytta skiva 1 från {från} till {till}")
        return
    
    # Flytta n-1 skivor från "från" till "mellan" med hjälp av "till"
    tower_of_hanoi(n-1, från, mellan, till)
    
    # Flytta den största skivan från "från" till "till"
    print(f"Flytta skiva {n} från {från} till {till}")
    
    # Flytta n-1 skivor från "mellan" till "till" med hjälp av "från"
    tower_of_hanoi(n-1, mellan, till, från)

# Exempelanvändning
n = 3  # Antal skivor
tower_of_hanoi(n, "A", "C", "B")
