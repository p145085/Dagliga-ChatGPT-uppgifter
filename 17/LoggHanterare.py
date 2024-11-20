#17. Bygg en enkel logghanterare som sparar felmeddelanden till en fil.

import logging

# Konfigurera logghantering
def setup_logger(log_file="application.log"):
    # Skapa logger
    logger = logging.getLogger("Logghanterare")
    logger.setLevel(logging.ERROR)  # Logga endast felmeddelanden

    # Skapa en filhanterare
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.ERROR)

    # Format för loggmeddelanden
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Lägg till hanterare till logger
    logger.addHandler(file_handler)

    return logger

# Exempel på användning
if __name__ == "__main__":
    logger = setup_logger()

    try:
        # Simulerar ett fel
        result = 10 / 0
    except Exception as e:
        logger.error("Ett fel inträffade: %s", e)
