import tkinter as tk
from revision import Revision_Controller
from utils import type_effect

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create Revision Controller instance
        self.revision_controller = Revision_Controller()

        # Set the title and size of the window
        self.title("Main Menu")
        self.geometry("400x300")

        # Create labels, buttons, etc. for the GUI menu
        self.create_widgets()

    def create_widgets(self):
        # Start Revision Button
        self.start_button = tk.Button(self, text="Start Revision", command=self.start_revision)
        self.start_button.pack(pady=10)

        # Add New Topic Button
        self.add_button = tk.Button(self, text="Add New Topic", command=self.add_new_topic)
        self.add_button.pack(pady=10)

        # Edit Topic Button
        self.edit_button = tk.Button(self, text="Edit Topic", command=self.edit_topic)
        self.edit_button.pack(pady=10)

        # Delete Topic Button
        self.delete_button = tk.Button(self, text="Delete Topic", command=self.delete_topic)
        self.delete_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=10)

    def start_revision(self):
        self.revision_controller.start_revision()
        self.exit_app()

    def add_new_topic(self):
        self.revision_controller.add_new_topic()
        self.exit_app()

    def edit_topic(self):
        self.revision_controller.edit_topic()
        self.exit_app()

    def delete_topic(self):
        self.revision_controller.delete_topic()
        self.exit_app()

    def exit_app(self):
        type_effect("Goodbye!\n", speed=0.05)
        self.quit()  # Close the tkinter window

# Create and run the MainMenu
if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
