from revision import Revision_Controller
from utils import type_effect

def menu():
    revision_controller = Revision_Controller()
    while True:
        print(f'{"-" * 30} Main Menu {"-" * 30}')
        options = ['                                    ',
                   '                           1. Start Revision \n',
                   '                           2. Add a new topic \n',
                   '                           3. Edit a topic \n',
                   '                           4. Delete a topic \n',
                   '                           5. Exit \n']
        for i in options:
            type_effect(i, speed=0.0001)

        choice = input('>>> ')
        if choice == '1':
            revision_controller.start_revision()
        elif choice == '2':
            revision_controller.add_new_topic()
        elif choice == '3':
            revision_controller.edit_topic()
        elif choice == '4':
            revision_controller.delete_topic()
        elif choice == '5':
            type_effect('Goodbye! \n', speed=0.05)
            break  # Exit the loop and end the program
        else:
            type_effect('Invalid choice, please try again. \n', speed=0.05)
