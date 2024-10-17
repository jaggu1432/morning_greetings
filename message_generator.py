# message_generator.py
import logging
import random

def generate_message(name):
    try:
        if not name:
            raise ValueError("Name is required to generate a message.")
        messages = [
            {f"Good Morning, {name}! Have a great day!"},
            {f"Hey, {name}! Hope your day is filled with positivity!"},
            {f"Hello, {name}! Wishing you a wonderful day ahead!"}
        ]
        #message = f"Good Morning, {name}! Have a great day!"
        message = random.choice(messages)
        logging.info(f"Generated message for {name}")
        return message
    except ValueError as e:
        logging.error(f"Error generating message: {e}")
        return None
