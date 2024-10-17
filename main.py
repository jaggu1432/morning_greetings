# main.py

import logging
from contacts_manager import ContactsManager
from message_generator import generate_message
from message_sender import send_message
from logger import log_message

# Set up the logging configuration
logging.basicConfig(filename='morning_greetings.log',
                    level=logging.INFO,  # Set logging level to INFO
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting the message sending process...")

    try:
        # Create a ContactsManager instance
        contacts_manager = ContactsManager()
        
        # Get the list of contacts
        contacts = contacts_manager.get_contacts()

        if not contacts:
            logging.warning("No contacts available to send messages.")
            raise ValueError("No contacts available to send messages.")

        # Loop through each contact
        for contact in contacts:
            try:
                # Generate a personalized message for each contact
                message = generate_message(contact['name'])
                logging.info(f"Generated message for {contact['name']}: {message}")

                if message:
                    # Simulate sending the message
                    send_message(contact['email'], message)
                    logging.info(f"Message sent to {contact['email']}")

                    # Log the message to an external log file
                    log_message(contact, message)
            except Exception as e:
                logging.error(f"Error with contact {contact['name']}: {e}")

    except ValueError as e:
        logging.error(f"Error in main process: {e}")
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")

    logging.info("Message sending process completed.")

if __name__ == "__main__":
    main()
