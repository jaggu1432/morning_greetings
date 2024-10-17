# message_sender.py
import logging

def send_message(email, message):
    try:
        if not email:
            raise ValueError("Email address is missing.")
        if not message:
            raise ValueError("Message content is missing.")
        
        # Simulate sending a message (replace this with real logic)
        logging.info(f"Sending message to {email}")
        print(f"Sending message to {email}: {message}")
    except ValueError as e:
        logging.error(f"Error sending message: {e}")
