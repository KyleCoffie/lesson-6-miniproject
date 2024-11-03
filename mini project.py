# User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:

contacts = {}
def add_contact():
    name = input("What is the contact's name? ")
    phone_no = input("What is the contact's phone number? ")
    email = input("What is the contact's email? ")
    new_contact={"name":name, "phone":phone_no, "email":email}
    contacts[phone_no]= new_contact
    print("Contact added!")

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

def edit_contact():
    display_contacts()
    choice_phone_no =input("Enter the phone number of the person would you like to edit? ")
    if choice_phone_no in contacts:
        print ("1. Name")
        print ("2. Phone")
        print ("3. Email")
   
        selection = (int(input("Which part of the contact would you like to edit?")))
        if selection == 1:
           updated_name = input( "Please enter updated name")
           contacts[choice_phone_no]["name"] = updated_name
        if selection == 2: 
           updated_phone = input( "Please enter updated phone no.")
           contacts[choice_phone_no]["phone"] = updated_phone
        if selection == 3:
            updated_email = ("Please enter updated email")
            contacts[choice_phone_no]["email"] = updated_email
        print (" Contact has been updated!")
    else:
        print("Contact with that phone number not found")
        
def search_contact(name,contacts):
    for contact in contacts:
        if contact["name"].lower()==name.lower:
            return contact
        return None
    search_name = input("What name are you looking for in your contacts?")
    result = search_contact(search_name, contacts)
    if result:
        print(f"Contact found: {result}")
    else: print ("Contact not found")
        
def display_contacts():
    if contacts == {}:
        print("There are no contacts in your list! Go and make some friends!!!")
    else:
        print("Your contacts are: ")
        for key,data in contacts.items():
            print (f"{key}: Name:{data["name"]} Phone Number: {data["phone"]} Email: {data["email"]}")

def export_contact(name, contacts):
    for contact in contacts:
        if contact["name"].lower()==name.lower:
            return contact
        return None
    export_name = input("Wich contact would you like to export to the text file?")
    result = export_contact(export_name,contacts)
    if result:
        with open('contact_lists.txt', 'w') as file:
            file.write(f'{result}')
            print(f"{result} has been exported to the contact_lists.txt file!")
    else:
        print("Contact not found")        


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
               

        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            export_contact()
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