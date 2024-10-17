# logger.py
import datetime
import logging

def log_message(contact, message):
    try:
        if not contact or not message:
            raise ValueError("Contact and message are required for logging.")

        with open("message_log.txt", "a") as log_file:
            log_entry = f"{datetime.datetime.now()} - Sent to {contact['name']}: {message}\n"
            log_file.write(log_entry)
            logging.info(f"Logged message for {contact['name']}")
    except (OSError, ValueError) as e:
        logging.error(f"Error logging message: {e}")
