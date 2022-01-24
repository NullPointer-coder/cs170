# Jingbo Wang
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    # input the Celsius temperature from user
    celsius = eval(input("What is the Celsius temperature? "))
    
    # traslate the Celsius temperature into Fahrenheit temperature
    fahrenheit = (9/5) * celsius + 32

    # cout the Fahrenheit temperature
    print("The temperature is ",fahrenheit," degrees Fahrenheit.")

main()
