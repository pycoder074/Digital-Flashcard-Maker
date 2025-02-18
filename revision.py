from utils import type_effect
from csv_handler import *
import os 
class Revision_Controller():
    def __init__(self):
        pass  # Initialize the class if necessary

    def study(self, filename):
        data = read(filename)
        flashcards_reviewed = 0  # Track number of flashcards reviewed
        for row in data:
            term, definition = row  # Assuming CSV format is term, definition
            type_effect(f"What is a {term}", speed=0.05)  # Display the term with default speed

            # Wait for user input to show definition
            user_input = input('Press Enter to reveal the answer or type "quit" to quit study mode... ')

            if user_input.lower() == 'quit':  # Check if user types "quit"
                type_effect("Exiting the revision... \n", speed=0.05)  # Exit message with speed
                return  # Exit the study session and return to the main menu

            type_effect(definition, speed=0.05)  # Display the definition with default speed
            input('Press Enter to continue to the next flashcard...')  # More clear message
            flashcards_reviewed += 1

        type_effect(f"You've reviewed {flashcards_reviewed} flashcards.\n", speed=0.05)  # Display flashcards reviewed summary

    def start_revision(self):
        topics = find_csv_files()
        if topics:
            type_effect('Which topic would you like to study? \n', speed=0.05)
            for i, topic in enumerate(topics):
                type_effect(f'{i + 1}. {topic}\n', speed=0.05)

            while True:
                choice = input('>>> ')
                try:
                    choice_index = int(choice) - 1  # Convert input to index
                    if 0 <= choice_index < len(topics):
                        self.study(topics[choice_index])
                        break  # Return to main menu after study session
                    else:
                        type_effect("Invalid selection. Please choose a valid topic number. \n", speed=0.05)
                except ValueError:
                    type_effect("Invalid input. Please enter a number corresponding to a topic. \n", speed=0.05)
        else:
            type_effect('No topics available to study. \n', speed=0.05)
        
    def add_new_topic(self):
        type_effect('Enter the name of the new topic: \n', speed=0.05)
        new_topic = input('>>> ')
        
        if new_topic:
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{new_topic}.csv")
            file = open(file_path, "w")
            type_effect(f'{new_topic} has been created. \n', speed=0.05)

            type_effect("Would you like to add flashcards to this topic? \n", speed=0.05)
            answer = input('>>> ')

            if answer.lower() == 'yes':
                flashcards = []
                while True:
                    term = input('Term: ')
                    definition = input('Definition: ')
                    if term.lower() == "quit" or definition.lower() == "quit":
                        break  # Exit loop if quit is typed
                    elif not term or not definition:
                        type_effect("Both term and definition are required. \n", speed=0.05)
                    else:
                        flashcards.append([term, definition])

                if flashcards:
                    write(file, flashcards)  # Write flashcards to file
                    type_effect(f'{len(flashcards)} flashcards have been added to {new_topic}. \n', speed=0.05)
                else:
                    type_effect("No flashcards were added. \n", speed=0.05)
            else:
                type_effect(f'No flashcards added. File {new_topic}.csv has been created. \n', speed=0.05)
            
            file.close()  # Close the file if it was opened
        else:
            type_effect('No name entered. Please type in a name. \n', speed=0.05)

    

    def delete_topic(self):
        topics = find_csv_files()
        if topics:
            type_effect('Which topic would you like to delete? \n', speed=0.05)
            for i in topics:
                type_effect(i + '\n', speed=0.05)

            file_to_delete = input('>>> ')
            if file_to_delete in topics:
                os.remove(file_to_delete)
                type_effect(f'{file_to_delete} has been deleted. \n', speed=0.05)
            else:
                type_effect(f"{file_to_delete} not found. \n", speed=0.05)
        else:
            type_effect('No topics available to delete. \n', speed=0.05)
