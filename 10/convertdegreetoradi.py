#10. **Konvertera grader till radianer:** Skriv ett program som konverterar grader till radianer och vice versa.

import math

def grader_till_radianer(grader):
    return grader * (math.pi / 180)

def radianer_till_grader(radianer):
    return radianer * (180 / math.pi)

def huvudmeny():
    print("Välkommen till grader och radianer konverteringsprogram!")
    while True:
        print("\nVad vill du göra?")
        print("1. Konvertera grader till radianer")
        print("2. Konvertera radianer till grader")
        print("3. Avsluta")

        val = input("Välj ett alternativ (1/2/3): ")

        if val == "1":
            grader = float(input("Ange grader: "))
            radianer = grader_till_radianer(grader)
            print(f"{grader} grader är {radianer:.4f} radianer.")
        elif val == "2":
            radianer = float(input("Ange radianer: "))
            grader = radianer_till_grader(radianer)
            print(f"{radianer} radianer är {grader:.4f} grader.")
        elif val == "3":
            print("Avslutar programmet. Hej då!")
            break
        else:
            print("Ogiltigt val. Försök igen!")

if __name__ == "__main__":
    huvudmeny()