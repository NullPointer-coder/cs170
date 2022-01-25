# Jingbo Wang
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value of a"
           +"15-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(3):
        for j in range(5):
            principal = principal * (1 + apr)
        print ("The value in " + str(i+1) + "'s five years is:", principal)

main()

