# Jingbo Wang
# testing functions

def sum(a, b):
    return a + b

# running product
def power(base, exponent):
    result = 1;
    for index in range(exponent):
        result = result * base
        
    return result

# this function returns both sum and product of 2 numbers
def sum_n_product(a, b):
    sum = a + b
    product = a * b
    return sum, product

def main():
    sum_1, product_1 = sum_n_product(5, 10)
    print(sum_1,product_1)

main()
