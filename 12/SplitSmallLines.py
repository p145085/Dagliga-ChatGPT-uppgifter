#12. **Implementera ett program som delar upp en stor textfil i mindre filer baserat på antal rader.**
def dela_upp_fil(filnamn, rader_per_fil):
    try:
        with open(filnamn, 'r', encoding='utf-8') as stor_fil:
            filräknare = 1
            radräknare = 0
            ny_fil = open(f"{filnamn}_del_{filräknare}.txt", 'w', encoding='utf-8')

            for rad in stor_fil:
                ny_fil.write(rad)
                radräknare += 1

                if radräknare >= rader_per_fil:
                    ny_fil.close()
                    filräknare += 1
                    radräknare = 0
                    ny_fil = open(f"{filnamn}_del_{filräknare}.txt", 'w', encoding='utf-8')

            ny_fil.close()
        print(f"Filen '{filnamn}' har delats upp i {filräknare} mindre filer.")
    except FileNotFoundError:
        print(f"Filen '{filnamn}' hittades inte.")
    except Exception as e:
        print(f"Ett fel inträffade: {e}")

# Exempel på användning
filnamn = "stor_textfil.txt"  # Filen som ska delas upp
rader_per_fil = 1000         # Antal rader per mindre fil
dela_upp_fil(filnamn, rader_per_fil)
