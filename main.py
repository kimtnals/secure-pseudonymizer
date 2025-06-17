from src.client import Client

def main():
    client = Client()

    while True:
        print("=== Pseudonymization CLI ===")
        print("1. Create new session")
        print("2. Select session")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            client.create_new_session()
        elif choice == "2":
            client.select_session()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()