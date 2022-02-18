# Jingbo Wang
# This program could let string value phrase
# to generate an acronym

def main():
    print("This program asks the user to input any phrase,"
           + "and uses this input phrase to generate an acronym")
    
    string = input("Please enter a string you want: ")

    # separate the string value by spaces
    string = string.split()
    

    result = ""

    for char in string:
        # capitalize the first character of each part string,
        # and put them into result
        #char[0] is the first character of each part string
        result += char[0].capitalize() 

    print("The acronym of the string you input is:", result)



main()
