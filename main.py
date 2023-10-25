def decoder(encoded_password):
    # Initialize an empty string to store the decoded password
    decoded = ''

    # Loop through each character in the encoded password
    for char in encoded_password:
        # Check if the character is a digit
        if char.isdigit():
            # Convert the digit to an integer, subtract 3, take modulo 10 to handle underflow, and add back to the decoded string
            decoded += str((int(char) - 3) % 10)

    return decoded


def encode(number):
    for int in number:
        int += 3
        int = int % 10


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def main():
    select = int(input("Please enter an option: "))

    if select == 1:
        password = int(input("Please enter your password to encode: "))
        encode(password)
        print("Your password has been encoded and stored!")


if __name__ == '__main__':
    main()
