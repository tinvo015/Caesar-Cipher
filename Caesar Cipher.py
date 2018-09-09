# This program decodes a Caesar Cipher.
# If the user knows the rot number, then the program will rot the
# message by that number. Otherwise, the program will output all possible
# rotations. The inputted text cannot contain a new line character or program
# will read that as the user pressing enter.


def break_encryption(text, rotate_number):
    if rotate_number > 26:
        rotate_number = rotate_number % 26  # keeps rotation between 0 and 25
    text = shift(text, rotate_number)
    print("Rot ", rotate_number, ":", sep="")
    print(text)

def brute_force_encryption(text):
    for j in range(1, 26) :
        results = shift(text, j)
        print("Rot ", j, ":", sep="")
        print(results)
        print("")

def shift (text, rotate) :
    results = ""
    for i in range(len(text)):
        value = ord(text[i])
        if value >= 65 and value <= 90:  # shifts capital letters
            value = ord(text[i]) + rotate
            if value > 90:
                value = value - 26

        elif value >= 97 and value <= 122:  # shifts lowercase letters
            value = ord(text[i]) + rotate
            if value > 122:
                value = value - 26

        results = results + chr(value)
    return results

def appropriate_input(brute_force):
    if brute_force == 'y' or brute_force == 'Y' or brute_force == 'N' or brute_force == "n":
        return True
    else:
        return False


if __name__ == "__main__":
    print("This program cracks a Caesar Cipher encryption.")
    brute_force = input("Do you know the rotation number of your encryption (Y/N)? ")
    while not appropriate_input(brute_force) :
        brute_force = input("Do you know the rotation number of your encryption? Enter \"Y\" for yes and \"N\" for no. ")
    print("Enter your text below and press enter when finished. Do not enter in new line characters. :")
    text = input()
    if brute_force == "y" or brute_force == "Y":
        rotate_number = int(input("Enter rotation/shift number:"))
        while rotate_number < 0:
            rotate_number = int(input("Enter a positive rotation number:"))
        break_encryption(text, rotate_number)
    else:
        brute_force_encryption(text)
