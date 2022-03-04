# Jingbo Wang
# check_leap.py
# A program to check if it is a leap year

def check_leap():
    # input
    year = int(input('write year '))

    # century year? that is divisible by 100?!
    if year % 100 == 0:
        # if true then year is a century year
        # nested-if, if inside another if
        if year % 400 == 0:
            # if true then the year is divisible by 400
            print('Leap')
        else:
            # the condition was false, the year is not divisible by 400
            print('Non leap')
    else:
        # if here means the condition was false, year is non century
        if year % 4 == 0:
            print('Leap')
        else:
            # the condition was false, meaning the year is not divisible by 4
            print('Non leap')

# end of check_lear()
check_leap()
