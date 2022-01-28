# running product 2
# this program is to calculate the n**k
# Jingbo Wang

def running_product2():
    n = int(input('Enter n: '))
    k = int(input('Enter k: '))

    # n- what to multiply, k-how many times to multiply
    # this program claculate n**k
    product = 1
    # run loop k times
    for _ in range(k):
        product = product * n

    print(n, 'raised to the power', k, 'is', product)

running_product2()
