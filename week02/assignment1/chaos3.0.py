# Jingbo Wang
# A simple program illustrating chaotic behavior
# by two input 

def main():
    print("The program illustrates a chaotic function")
    
    # get input form user from 0 to 1
    x,y = eval(input("Enter two numbers between 0 and 1: "))

    # the number of values to print is determined by the user
    n = eval(input("how many numbers should I print? "))

    # print out the title of table
    # str(): Transform float value into string value
    print("input"+ "  " + str(x) + "        " + str(y))
    print("------------------------")
    
    # calculate the input value for 10 times
    # and print result each times
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        
        # print out the result of the calculation with
        # 6 decimal places
        print("     " + str("{0:.6f}".format(x)) + "   "
               + str("{0:.6f}".format(y)))
        

main()
