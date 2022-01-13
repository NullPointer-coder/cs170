# Jingbo Wang
# A simple program illustrating chaotic behavior

def main():
    print("The program illustrates a chaotic function")
    
    # get input form user from 0 to 1
    x = eval(input("Enter a number between 0 and 1: "))
    
    # calculate the input value for 10 times
    # and print result each times
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)

main()
