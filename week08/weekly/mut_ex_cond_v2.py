# Jingbo Wang
# mut_ex_cond_v2.py
# A program to calculate percentage of grades and give the level

def mut_ex_cond_v2():
    c_1, c_2, c_3, c_4 = input('write the points in 4 courses out of 100 each ').split()
    # let user inputs three grades
    c_1 = int(c_1)
    c_2 = int(c_2)
    c_3 = int(c_3)
    c_4 = int(c_4)

    percentage = (c_1 + c_2 + c_3 + c_4) / 4
    # calculate the percentage of the 4 grades
    print(percentage)

    # multi-way conditions
    # mutually exclusive
    # enhanced way to present nested if
    # out of all the conditions only one is going to be true
    

    if percentage >= 90:
        # if the percentage is bigger and equal to 90 do this
        print('A')
    elif percentage >= 80:
        # if the percentage is bigger and equal to 80 do this
        print('B')
    elif percentafe >= 70:
        # if the percentage is bigger and equal to 70 do this
        print('C')
    elif percentage >= 60:
        # if the percentage is bigger and equal to 60 do this
        print('D')
    else:
        # else do this
        print('Fail')

# end of mut_ex_cond_v2
mut_ex_cond_v2()
