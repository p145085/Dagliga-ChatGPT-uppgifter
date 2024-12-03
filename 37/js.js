// Sätt slutdatum och tid
const endDate = new Date("2024-12-31T23:59:59").getTime();

function updateTimer() {
  const now = new Date().getTime();
  const timeLeft = endDate - now;

  // Beräkna dagar, timmar, minuter och sekunder
  const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

  // Visa nedräkningen
  document.getElementById("timer").innerHTML = 
    `${days}d ${hours}h ${minutes}m ${seconds}s`;

  // Stoppa timern om tiden är slut
  if (timeLeft < 0) {
    clearInterval(timerInterval);
    document.getElementById("timer").innerHTML = "Tiden är ute!";
  }
}

// Uppdatera timern varje sekund
const timerInterval = setInterval(updateTimer, 1000);
updateTimer(); // Kör direkt för att undvika fördröjning
