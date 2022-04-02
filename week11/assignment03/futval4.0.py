# Jingbo Wang
#    A program to compute the value of an investment
#    carried nyears into the future

def main():
    print("This program calculates the future value of a"
           +"n-year(which is a user input) investment.")
    
    # get input from user
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the years for the investment: "))

    # print reasult
    print("Year" + "       " + "Value")
    print("----------------------")
    for i in range(year):
        principal = principal * (1 + apr)
        print(" " + str(i) + "         " + str(principal))

main()

