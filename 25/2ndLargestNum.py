#25. **Hitta andra största talet:** Skriv ett program som hittar det näst största talet i en lista.

def hitta_andra_storsta_talet(lista):
    if len(lista) < 2:
        raise ValueError("Listan måste innehålla minst två unika tal.")
    
    unika_tal = list(set(lista))  # Tar bort dubbletter
    if len(unika_tal) < 2:
        raise ValueError("Listan måste innehålla minst två unika tal.")
    
    unika_tal.sort(reverse=True)  # Sorterar i fallande ordning
    return unika_tal[1]  # Returnerar det näst största talet

# Exempelanvändning
lista = [3, 5, 1, 9, 9, 4]
andra_storsta = hitta_andra_storsta_talet(lista)
print(f"Det näst största talet är: {andra_storsta}")
