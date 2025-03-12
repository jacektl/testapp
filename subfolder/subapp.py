import logging
import random
import time

zen_messages = [
    "Does the moon follow the car?",
    "The Zen master is the traffic light.",
    "What is the sound of one tire skidding?",
    "The journey of a thousand miles begins with a single gear.",
    "Honk if you understand recursion.",
    "There is no road, only the car.",
    "The road is the destination.",
    "The car is the driver.",
    "The driver is the road.",
    "The road is the road.",
    "The car is the car.",
    "The driver is the driver.",
    "The road is the car.",
    "The car is the road.",
    "The driver is the road.",
    "The road is the driver.",
    "The car is the driver.",
    "The driver is the car.",
    "The road is the road."]

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    while True:
        logging.info(f"{random.choice(zen_messages)}!")
        time.sleep(5)