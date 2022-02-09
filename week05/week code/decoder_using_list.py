# Jingbo Wang
# A program to convert a sequence of Unicode numbers into
# a string of text.

def main():
    print("This program converts a sequence of unicode number into")
    print("the string of text that it represents.\n")

    # Get the message to encode
    in_string = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicode message
    message = []
    for num_str in in_string.split():
        # convert the (sub)string to a number
        code_num = int(num_str)
        # append character to the list
        message.append(chr(code_num))


    message = "".join(message)
    print("\nThe decoded message is:", message)

main()
