# Jingbo Wang
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    for i in range(4):
        # input the Celsius temperature from user
        celsius = eval(input("What is the " + str(i+1) +
                              "'s Celsius temperature? "))
    
        # traslate the Celsius temperature into Fahrenheit temperature
        fahrenheit = (9/5) * celsius + 32

        # cout the Fahrenheit temperature
        print("The " + str(i+1) + "'s temperature is ",fahrenheit,
              "'s degrees Fahrenheit.")

main()
