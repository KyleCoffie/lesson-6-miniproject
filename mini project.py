# User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:

contacts = []

def directory():
    while True:


        print("\nWelcome to the Contact Management System!")
        
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")
        choice = input("Please make a selection: ")

        def delete_contact():
            display_contacts()
            try:
                contacttodelete = int(input("Enter the number next to the name you wish to delete. "))
                if contacttodelete -1 >=0 and contacttodelete -1 <len(contacts):
                    removed_contact = contacts.pop(contacttodelete -1)
                    print(f"{removed_contact} has been deleted!")
                else:
                    print(f"{contacttodelete} was not found")
            except ValueError:
                print("Invaid input! Please try again")
                
        def edit_contact(contacts, index, new_name=None, new_no=None, new_email=None):
            if index < 0 or index >= len(contacts):
                print("Invaild contact index")
                return
            if new_name:
                contacts[index+1].name = new_name
            elif new_no:
                contacts[index+2].phone_no = new_no
            elif new_email:
                contacts[index+3].email = new_email
            else:
                print(contacts)
                choice =(int(input("Which Contact would you like to edit? ")))
                for index,contact in enumerate(contacts):
                    pass
                    

                
                
        
        
        def display_contacts():
            if contacts == []:
                print("There are no contacts in your list! Go and make some friends!!!")
            else:
                print("Your contacts are: ")
                for index,contact in enumerate (contacts):
                    print (f"{index+1}: Name:{contact[0]} Phone Number: {contact[1]} Email: {contact[2]}")

        if choice == "1":
            name = input("What is the contact's name? ")
            phone_no = input("What is the contact's phone number? ")
            email = input("What is the contact's email? ")
            new_contact=[name, phone_no, email]
            contacts.append(new_contact)
            print("Contact added!")
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            pass
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            print("Thank for using the contact management system.")
            break
    
    else: False
    
directory()
# Contact Data Storage:
# Use nested dictionaries as the main data structure for storing contact information.
# Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
# Store contact details within the inner dictionary, including:
# Name
# Phone number
# Email address
# Additional information (e.g., address, notes).
# Menu Actions:
# Implement the following actions in response to menu selections:
# Adding a new contact.
# Editing an existing contact's information (name, phone number, email, etc.).
# Deleting a contact.
# Searching for a contact and displaying their details.
# Displaying a list of all contacts.
# Exporting contacts to a text file in a structured format.
# Importing contacts from a text file and adding them to the system. * BONUS
# User Interaction:
# Utilize input() to enable users to select menu options and provide contact details.
# Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.
# Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.
# GitHub Repository:
# Create a GitHub repository for your project.
# Create a clean and interactive README.md file in your GitHub repository.
# Include clear instructions on how to run the application and explanations of its features.