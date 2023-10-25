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


