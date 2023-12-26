# Simple Contact Directory

## Overview
This Python program provides a basic command-line interface to manage a contact directory, allowing users to add, find, delete, and update contact information stored in a simple database.

### Database Interaction
The program interacts with a database through the `Simpledb` class, which operates on a file named 'directory.txt'.

## Functionality
- **Add Contacts:** Users can add new contacts with their names and phone numbers.
- **Find Contacts:** Allows searching for a contact by name to retrieve their phone number.
- **Delete Contacts:** Contacts can be removed from the directory by name.
- **Update Contacts:** Provides the ability to update the phone number of an existing contact.
- **Quit:** Exit the program.

## Usage
### Running the Program
Upon running the program, users are prompted with options to add, find, delete, update contacts, or quit the program. The user inputs a command to perform the respective action.

### Commands
- **a:** Add a new contact.
- **f:** Find a contact by name.
- **d:** Delete a contact by name.
- **u:** Update an existing contact's phone number.
- **q:** Quit the program.

### Example Interaction
```python
# Example User Interaction
What would you like to do today? (enter a for add, f for find, d for delete, u for update, or q for quit): a
What is the name that you would like to add? John Doe
What is that person's number? 123-456-7890

# Adding more contacts, finding, updating, and deleting them follow a similar interactive pattern.
