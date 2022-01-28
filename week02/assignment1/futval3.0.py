# Jingbo Wang
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value of a "
           +"15-year investment.")
    # get the first year 
    principal = eval(input("Enter the 1's five year team initial principal: "))
    apr = eval(input("Enter the annual 1's five year team interest rate: "))

    # calculate the principal for each 5 year team
    for i in range(1,4,1):

        # calculate 5 years principal
        for j in range(5):
            principal = principal * (1 + apr)
            
        print ("The value in " + str(i) + "'s five years is:", principal)

        # only get input of three times of 5 year terms 
        if i < 3:
            extra_principal = eval(input("Enter the " + str(i + 1)
                                         + "'s five year team extra"
                                         + "initial principal: "))
            apr = eval(input("Enter the annual " + str(i + 1)
                             + "'s five year team interest rate: "))
            principal = extra_principal + principal
main()

