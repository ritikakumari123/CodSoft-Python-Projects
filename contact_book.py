# Contact Book Application

contacts = {}

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":

        name = input("Enter Name: ")

        # Phone Validation
        phone = input("Enter Phone Number: ")

        if not phone.isdigit():
            print("Invalid phone number! Only digits are allowed.")
            continue

        # Email Validation
        email = input("Enter Email: ")

        if "@" not in email or "." not in email:
            print("Invalid email format!")
            continue

        address = input("Enter Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact added successfully!")

    # View Contacts
    elif choice == "2":

        if not contacts:
            print("No contacts found.")

        else:
            print("\n===== CONTACT LIST =====")

            for name, details in contacts.items():

                print(f"\nName: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")

    # Search Contact
    elif choice == "3":

        search = input("Enter contact name to search: ")

        if search in contacts:

            print("\n===== CONTACT FOUND =====")
            print(f"Name: {search}")
            print(f"Phone: {contacts[search]['Phone']}")
            print(f"Email: {contacts[search]['Email']}")
            print(f"Address: {contacts[search]['Address']}")

        else:
            print("Contact not found.")

    # Update Contact
    elif choice == "4":

        update_name = input("Enter contact name to update: ")

        if update_name in contacts:

            phone = input("Enter new phone number: ")

            if not phone.isdigit():
                print("Invalid phone number! Only digits are allowed.")
                continue

            email = input("Enter new email: ")

            if "@" not in email or "." not in email:
                print("Invalid email format!")
                continue

            address = input("Enter new address: ")

            contacts[update_name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }

            print("Contact updated successfully!")

        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == "5":

        delete_name = input("Enter contact name to delete: ")

        if delete_name in contacts:

            del contacts[delete_name]
            print("Contact deleted successfully!")

        else:
            print("Contact not found.")

    # Exit
    elif choice == "6":

        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice. Please try again.")
