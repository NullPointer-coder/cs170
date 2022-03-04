# Display final amount with discount by if statement
# Jingbo Wang

def main():
    # input of amount
    amount = int(input("write amount: "))

    # check for the amount
    if amount > 500:
        discount = 0.1
    else:
        discount = 0.05

    # we have to figured out the discount
    final_amount = amount - (discount * amount)
    print(final_amount)

main()
