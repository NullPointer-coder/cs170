# Jingbo Wang
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value of a"
           +"n-year(which is a user input) investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the years for the investment: "))

    for i in range(year):
        principal = principal * (1 + apr)

    print ("The value in " + str(year) + " years is:", principal)

main()

