def input_numeric_amount():
    """
    Prompts the user to input a numerical amount.
    """
    try:
        amount = float(input("Enter a numeric dollar amount (e.g., 123.45): "))
        return amount
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        return None


def validate_input(amount):
    """
    Validates the numerical input.
    """
    if amount is None or amount <= 0:
        print("Error: The input must be a positive number.")
        return False
    return True


def convert_to_words(amount):
    """
    Converts a numeric amount to words.
    """
    # A simplified example using a library
    from num2words import num2words
    return num2words(amount, to='currency', lang='en', currency='USD')


def format_output(amount_in_words):
    """
    Formats the check output.
    """
    return f"Pay to the order of: __________\nAmount in words: {amount_in_words}\nMemo: __________"


def main():
    """
    Main function that represents the flow of the Check Writer program.
    """
    while True:
        print("\n--- Check Writer Program ---")
        amount = input_numeric_amount()
        
        if validate_input(amount):
            break  # Proceed to the next steps if input is valid

    amount_in_words = convert_to_words(amount)
    check_output = format_output(amount_in_words)
    
    print("\n--- Generated Check ---")
    print(check_output)


if __name__ == "__main__":
    main()
