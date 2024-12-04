// Hämta element
const searchInput = document.getElementById('search');
const nameList = document.getElementById('nameList');
const names = nameList.getElementsByTagName('li');

// Lägg till en händelselyssnare för inmatningsfältet
searchInput.addEventListener('input', () => {
    const filter = searchInput.value.toLowerCase(); // Konvertera till små bokstäver för att ignorera case
    Array.from(names).forEach(name => {
        const text = name.textContent.toLowerCase();
        if (text.includes(filter)) {
            name.classList.remove('hidden'); // Visa namnet om det matchar
        } else {
            name.classList.add('hidden'); // Dölj annars
        }
    });
});
