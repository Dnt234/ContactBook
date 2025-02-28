import csv
import os

def create_csv_file(filename, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

def update_list(contacts, new_contact):
    contacts.append(new_contact)
    return contacts

def find_contact_book(contact_books, option):
    try:
        index = int(option) - 1
        if 0 <= index < len(contact_books):
            return contact_books[index]
    except ValueError:
        return None

def count_contact_books(directory):
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    return csv_files

def open_contact(contact_books):
    print(f"There are {len(contact_books)} contact books.")
    for i, book in enumerate(contact_books, start=1):
        print(f"{i}. {book}")
    option = input("Enter the number of the contact book you want to open: ")
    selected_book = find_contact_book(contact_books, option)
    if selected_book:
        with open(selected_book, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    else:
        print("Contact book not found.")

def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    contact_books = count_contact_books(directory)
    while True:
        print("1. Create a new contact book")
        print("2. Open an existing contact book")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            filename = input("Enter the name of the contact book (without .csv): ") + '.csv'
            fieldnames = [input("Whats your name:"), input("Whats your phone number:")]
            create_csv_file(filename, fieldnames)
            contact_books.append(filename)
            print(f"Contact book '{filename}' created.")
        elif choice == '2':
            open_contact(contact_books)
            return open_contact
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

main()


