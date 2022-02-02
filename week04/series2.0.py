# Jingbo Wang
# This program cloud calculate the factorial number


def main():
    print("This program could calculate",
            " n + (n-1) + (n-2) + ... + 1")
    # input n from user
    n = int(input('Please Enter n value you want:'))

    factorial = 0

    for i in range(1,n+1,1):
        # to calculate the factorial number
        factorial = factorial + i

    # print the final result   
    print(factorial)

main()
