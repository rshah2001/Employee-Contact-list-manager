import os

# File path for storing contacts
FILE_PATH = "contacts.txt"


class Contact:
    """Domain Layer: Represents a Contact."""

    def __init__(self, name: str, phone: str, email: str):
        """
        Constructor for the Contact class.
        param name: Name of the contact.
        param phone: Phone number of the contact.
        param email: Email address of the contact.
        """
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        """
        Convert a contact object to a string format for file storage.
        return: A string in the format "name,phone,email".
        """
        return f"{self.name},{self.phone},{self.email}"

    @staticmethod
    def from_string(data: str):
        """
        Convert a string from the file back into a Contact object.
        param data: A string in the format "name,phone,email".
        return: A Contact object created from the string.
        """
        name, phone, email = data.strip().split(",")
        return Contact(name, phone, email)


class ContactManager:
    """Handles all operations related to managing contacts."""

    def __init__(self):
        """
        Constructor for the ContactManager class.
        Ensures the file exists and loads contacts from the file into memory.
        """
        self.ensure_file_exists()
        self.contacts = self.load_contacts()

    def ensure_file_exists(self):
        """
        Ensure the contact file exists before any operations.
        If the file does not exist, create an empty file.
        """
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, "w") as file:
                pass  # Create an empty file

    def save_contact(self, contact: Contact):
        """
        Save a single contact to the file.
        param contact: The Contact object to save.
        """
        with open(FILE_PATH, "a") as file:
            file.write(str(contact) + "\n")
        print(f"Contact '{contact.name}' added successfully!")

    def load_contacts(self):
        """
        Load all contacts from the file into memory.
        return: A list of Contact objects loaded from the file.
        """
        with open(FILE_PATH, "r") as file:
            lines = file.readlines()
        return [Contact.from_string(line) for line in lines]

    def add_contact(self, name: str, phone: str, email: str):
        """
        Add a new contact to the file and memory.
        param name: Name of the new contact.
        param phone: Phone number of the new contact.
        param email: Email address of the new contact.
        """
        contact = Contact(name, phone, email)
        self.save_contact(contact)
        self.contacts.append(contact)

    def display_all_contacts(self):
        """
        Display all contacts currently loaded in memory.
        """
        if self.contacts:
            print("\nAll Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print("\nNo contacts found!")

    def search_contact(self, keyword: str):
        """
        Search for contacts that contain the keyword in their name.
        param keyword: The keyword to search for.
        """
        results = [contact for contact in self.contacts if keyword.lower() in contact.name.lower()]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print(f"\nNo contacts found with keyword: {keyword}")

    def delete_contact(self, name: str):
        """
        Delete a contact by name.
        param name: Name of the contact to delete.
        """
        original_count = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        if len(self.contacts) < original_count:
            # Save the updated contact list back to the file
            with open(FILE_PATH, "w") as file:
                for contact in self.contacts:
                    file.write(str(contact) + "\n")
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found!")

    def update_contact(self, name: str):
        """
        Update the details of a contact by name.
        param name: Name of the contact to update.
        """
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                while True:
                    print("\nWhat would you like to update?")
                    print("1. Name")
                    print("2. Phone Number")
                    print("3. Email")
                    print("0. Finish Updating")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        new_name = input("Enter the new name: ")
                        contact.name = new_name
                        print(f"Contact name updated to '{new_name}'.")
                    elif choice == "2":
                        new_phone = input("Enter the new phone number: ")
                        contact.phone = new_phone
                        print(f"Contact phone updated to '{new_phone}'.")
                    elif choice == "3":
                        new_email = input("Enter the new email address: ")
                        contact.email = new_email
                        print(f"Contact email updated to '{new_email}'.")
                    elif choice == "0":
                        # Save the updated contact list back to the file
                        with open(FILE_PATH, "w") as file:
                            for c in self.contacts:
                                file.write(str(c) + "\n")
                        print(f"Contact '{name}' updated successfully!")
                        return
                    else:
                        print("Invalid choice. Please try again.")
        else:
            print(f"Contact '{name}' not found!")


def main_menu():
    """
    Presentation Layer: Main menu for user interaction with the Contact Management System.
    """
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            manager.add_contact(name, phone, email)

        elif choice == "2":
            manager.display_all_contacts()

        elif choice == "3":
            keyword = input("Enter a keyword to search: ")
            manager.search_contact(keyword)

        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == "5":
            name = input("Enter the name of the contact to update: ")
            manager.update_contact(name)

        elif choice == "0":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
