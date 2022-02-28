# Jingbo Wang
# the program to figure out the date of Easter

def main():
    year = int(input("Please enter the year (Like: 1987): "))

    # Get Center
    C = year // 100

   # figure out the date of Easter
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30

    print(epact)


main()
