#8. **Skapa en enkel timer:** Bygg ett program som räknar ner från ett givet antal sekunder och visar tiden på skärmen.

import time

def countdown_timer(seconds):
    """
    Räknar ner från ett givet antal sekunder och visar tiden på skärmen.

    :param seconds: Antalet sekunder att räkna ner från
    """
    try:
        for remaining in range(seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            print(timer_display, end="\r")  # \r skriver över samma rad
            time.sleep(1)  # Väntar en sekund

        print("\nTiden är slut!")
    except KeyboardInterrupt:
        print("\nNedräkning avbruten.")

if __name__ == "__main__":
    try:
        user_input = int(input("Ange antalet sekunder för nedräkningen: "))
        countdown_timer(user_input)
    except ValueError:
        print("Var vänlig och ange ett giltigt heltal.")
