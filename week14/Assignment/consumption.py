# Jingbo Wang
# consumption.py
# A program to finds out how many of the total days
# were heat consumption days, cold consumption days
# and respectively also accumulates the heat degree and cold degree values

from tkinter.filedialog import askopenfilename

def main():
    # initialize normal, heat, and cold days to 0
    normal = heat = cold = 0

    # initialize heat_sum and cold_sum to 0
    heat_sum = cold_sum = 0

    # ask open file
    infile_name = askopenfilename()
    in_file = open(infile_name, "r")

    # total nums of temperature
    total = in_file.readline()
    for lines in in_file:
        temperature = int(lines)
        # read data line by line
        if temperature < 60:
            # if value is less than 60,
            # it is cold temperature
            heat += 1
            heat_sum += 60 - temperature
        elif temperature > 80:
            # if temperature is greater than 80,
            # it is hot temperature
            cold += 1
            cold_sum += temperature - 80
        else:
            # else is normal
            normal += 1
            
    # print out the result
    print('Heat consumption days are', heat,
          'and the heat degree is', heat_sum)
    print('Cold consumption days are', cold,
          'and the cold degree is', cold_sum)
    print('Normal days are', normal)

main()
