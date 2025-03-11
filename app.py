import logging
import random
import time

hello = ["Hello", "Hi", "Hey", "Hola", "Bonjour", "Ciao", "Namaste", "Konnichiwa", "Guten Tag", "Olá", "Aloha", "Shalom", "Salut", "Hallo", "Hej", "Hei", "Hoi"]
world = ["World", "Earth", "Globe", "Planet", "Universe", "Cosmos", "Orbis", "Terra", "Gaia", "Mundo", "Monde", "Mondo", "Jagat", "Sekai", "Welt", "Verden", "Maailma", "Wereld"]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    while True:
        logging.info(f"{random.choice(hello)}, {random.choice(world)}!")
        time.sleep(5)