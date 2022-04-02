# Jingbo Wang
# a program modify the list by squaring each value,
#  and return the modified list.

def squareEach(nums):
    # squaring each number
    for i in range(len(nums)):
        nums[i] **= 2
    return  nums

def main():
    # Initialize a nums list
    nums = []
    # ask user how many numbers you want enter
    total = int(input("How many numbers you want enter? "))

    # input and store numbers in the nums list
    for i in range(total):
        num = float(input("Please enter " + str(i+1)+ "'s number: "))
        nums.append(float(num))

    # print the nums list before square
    print("Before square, ", nums)
    # print the nums list after square
    print("After square, ", squareEach(nums))
    
main()   
    
