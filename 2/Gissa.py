#**Gissa ett tal:** Bygg ett spel där användaren gissar ett slumpmässigt genererat tal.

import random

def gissa_ett_tal():
    # Generera ett slumpmässigt tal mellan 1 och 100
    tal = random.randint(1, 100)
    försök = 0
    
    print("Välkommen till Gissa ett tal-spelet!")
    print("Jag har valt ett tal mellan 1 och 100. Försök att gissa det!")
    
    while True:
        försök += 1
        gissning = input("Gissa ett tal: ")
        
        # Kontrollera att användaren skriver in ett tal
        if not gissning.isdigit():
            print("Det var inte ett giltigt tal. Försök igen.")
            continue
        
        gissning = int(gissning)
        
        if gissning < tal:
            print("För lågt! Försök igen.")
        elif gissning > tal:
            print("För högt! Försök igen.")
        else:
            print(f"Grattis! Du gissade rätt på {försök} försök!")
            break

gissa_ett_tal()
