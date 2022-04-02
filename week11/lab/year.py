# Jingbo
# year.py
# A program to calculates the corresponding day number

def main():
    date = input("Please enter data(month/day/year): ")

    # split the input date by /
    time = date.split("/")
    
    done = "false";
    while (done == "false"):
        # checks three numbers is valid date or not
        if (len(time) == 3
            and time[0].isdigit()
            and time[1].isdigit()
            and time[2].isdigit()):
        
            month = int(time[0])
            day = int(time[1])
            year = int(time[2])
            
            # get each number in array
            dayNum = 31 * (month - 1) + day

            # calculate the days
            if (month > 2):
                
                # after February subtract (4(month) + 23)//10
                dayNum -= ((4 * month) + 23) // 10
                
                if ((year % 4 == 0 and (year % 100 == 0)) or
                    ((year % 4 ==0) and (year % 100 != 0))):
                    # leap year and after February 29, add 1
                    dayNum += 1
            print("the days is", dayNum)
            done = "true"
        else:
            print("It's not a valid date! try again!")
            date = input("Please enter data(month/day/year): ")
            time = date.split("/")

main()
