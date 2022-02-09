# Jingbo Wang
# A program to convert a textual message into a sequence of
# numbers, utlilizing the underlying Unicode encoding.

def main():
    print("This program converts a textual message into a sequence")
    print("of numbers representing the Unicode encoding of the message. \n")

    # Get the massage to encode
    # no eval, input resurns a string value
    # string is stored in message object
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes: ")

    encoded_message = ""

    # iterable something that's loop-able, iterative
    # string is iterable
    # Loop through the message and accumulate the Unicode value
    for ch in message:
        encoded_message = encoded_message + str(ord(ch)) + " "

    # the encoded_message may contain an extra " " at the end
    encoded_message = encoded_message.strip()

    print(encoded_message) # blank line before prompt


main()
