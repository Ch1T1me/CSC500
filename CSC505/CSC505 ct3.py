class ShoppingListApp:
    def __init__(self):
        self.screens = []  # To store screen names and descriptions

    def get_screens(self):
        print("Welcome to the Shopping List App Prototype Program!")
        print("Let's define the key screens in your app.")

        # Prompt user for the number of screens
        try:
            num_screens = int(input("How many screens does your app have? "))
            for i in range(num_screens):
                print(f"\nScreen {i + 1}:")
                screen_name = input("Enter the name of the screen: ").strip()
                screen_description = input(f"Enter a brief description for '{screen_name}': ").strip()
                # Store screen details as a dictionary
                self.screens.append({"name": screen_name, "description": screen_description})
        except ValueError:
            print("Invalid input. Please enter a valid number for the number of screens.")

    def display_prototype(self):
        print("\n--- Shopping List App Prototype ---")
        if not self.screens:
            print("No screens to display. Please input screens first.")
            return

        # Display the details of each screen
        for i, screen in enumerate(self.screens, start=1):
            print(f"\nScreen {i}:")
            print(f"  Name: {screen['name']}")
            print(f"  Description: {screen['description']}")

        # Display the flow of screens
        screen_names = [screen['name'] for screen in self.screens]
        print("\nSequence of Screens: " + " -> ".join(screen_names))

if __name__ == "__main__":
    app = ShoppingListApp()
    app.get_screens()
    app.display_prototype()
