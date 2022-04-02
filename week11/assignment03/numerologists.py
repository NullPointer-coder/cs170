# Jingbo Wang
# To calculates the numeric value of a single name provided
# as input by the user

def main():
    name = input("Please input you name: ")
    name = name.split()
    sum = 0
    for index in range(len(name)):
        part = name[index]
        for i in range(len(part)):
            sum += ord(part[i])
    print("The numeric value of a single name provided is", sum) 
    
main()
