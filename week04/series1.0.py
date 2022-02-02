# Jingbo Wang
# This program can calculate the factorial number 

def main():
    print("This program could calculate",
            "1/2 + 2/3 + 3/4 + ... + n/n+1")
    # input n from user
    n = int(input('Please Enter n value you want:'))

    factorial = 0
    
    for i in range(1,n+1,1):
        # to calculate the factorial number
        factorial = factorial + i/(i+1)

    # print the final result 
    print(factorial)

main()
