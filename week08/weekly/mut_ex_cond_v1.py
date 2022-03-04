# Jingbo Wang
# mut_ex_cond_v1.py
# A program to calculate percentage of grades and give the level

def mut_ex_cond_v1():
    c_1, c_2, c_3, c_4 = input('write the points in 4 courses out of 100 each ').split()
    # let user inputs three grades
    c_1 = int(c_1)
    c_2 = int(c_2)
    c_3 = int(c_3)
    c_4 = int(c_4)

    percentage = (c_1 + c_2 + c_3 + c_4) / 4
    # calculate the percentage of the 4 grades
    print(percentage)

    if percentage >= 90:
        # if the percentage is bigger and equal to 90 do this
        print('A')
    else:
        if percentage >= 80:
            # if the percentage is bigger and equal to 80 do this
            print('B')
        else:
            if percentafe >= 70:
                # if the percentage is bigger and equal to 70 do this
                print('C')
            else:
                if percentage >= 60:
                    # if the percentage is bigger and equal to 60 do this
                    print('D')
                else:
                    # else do this
                    print('Fail')

# end of mut_ex_cond_v1
mut_ex_cond_v1()
