# Jingbo Wang
# A program to convert a sequance of Unicode number into
# a string of text.

def main():
    print("This program converts a sequence of Unicode number into")
    print("the string of text that it represents. \n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicode messsage
    message = ""
    for num_str in inString.split():
        # convert the (sub)string to a number
        code_num = int(num_str)
        # append character to message
        message = message + chr(code_num)

    print("\nThe decoded message is:", message)


main()
    
