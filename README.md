# Employee Contact List Manager

The **Employee Contact List Manager** is a Python-based application that allows users to manage a list of employee contacts. This system provides essential functionalities like adding, viewing, searching, updating, and deleting contact details. All contact information is stored in a `contacts.txt` file for persistence.

## Features

- **Add Contact**: Create a new contact with a name, phone number, and email address.
- **View All Contacts**: Display a list of all saved contacts.
- **Search Contacts**: Search for contacts by name using keywords.
- **Update Contact**: Modify the details (name, phone, or email) of an existing contact.
- **Delete Contact**: Remove a contact by name.
- **Persistent Storage**: Automatically saves all contacts in a `contacts.txt` file.

## Prerequisites

- Python 3.x installed on your system.
- Basic understanding of Python.

## How to Run the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/rshah2001/Employee-Contact-list-manager.git
   cd Employee-Contact-list-manager
   ```

2. Run the application:
   ```bash
   python contact_management_system.py
   ```

3. Follow the on-screen menu to manage your contact list.

## Usage

### Main Menu
When you run the application, you'll see the following options:
1. **Add Contact**: Enter details for a new contact.
2. **View All Contacts**: Lists all stored contacts.
3. **Search Contact**: Search for contacts containing specific keywords in their name.
4. **Delete Contact**: Remove a contact by providing their name.
5. **Update Contact**: Modify details of a specific contact.
6. **Exit**: Quit the program.

### Storage
- All contacts are stored in a file named `contacts.txt`. 
- If the file does not exist, it will be created automatically.

## Example

### Adding a Contact
```plaintext
Enter contact name: John Doe
Enter contact phone: 123-456-7890
Enter contact email: john.doe@example.com
Contact 'John Doe' added successfully!
```

### Viewing All Contacts
```plaintext
All Contacts:
Name: John Doe, Phone: 123-456-7890, Email: john.doe@example.com
```

### Searching for a Contact
```plaintext
Enter a keyword to search: John
Search Results:
Name: John Doe, Phone: 123-456-7890, Email: john.doe@example.com
```

## File Structure
```
Employee-Contact-list-manager/
├── final.py  # Main application file
├── contacts.txt                  # Automatically generated file for storing contacts
└── README.md                     # Documentation file
```

## Contributing

Feel free to submit a pull request if you'd like to improve or extend the functionality of the application. For major changes, please open an issue to discuss your proposed changes first.

