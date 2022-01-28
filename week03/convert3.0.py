# Jingbo
# A program to convert Celsius temps to Fahrenheit
# from 0 to 100 every 10 temps

def main():
    print("This program to convert Celsius temps to Fahrenheit",
          "from 0 to 100 every 10 temps")
    print()

    # print out table name
    print("       " + "Celsius temps" + "        " + "Fahrenheit")
    print("---------------------------------------")

    for i in range(0,101,10):

        # celsius is the value of i in the range
        celsius = i

        # traslate the Celsius temperature
        # into Fahrenheit temperature
        fahrenheit = (9/5) * celsius + 32
        print("           " + str(celsius)
              + "                  " 
              + str(fahrenheit))


main()
        
