# collect principal amount, interest on it, years
# calculate the monthly payment

def main():
    print("this is a monthly interest calculator")
    print('')

    principal  = float(input('Input the loan amount: '))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Years: "))


    monthly_interest = apr / 1200
    months = years * 12
    monthly_payment = principal * monthly_interest / (1 - (1 + monthly_interest) ** (-months))

    print("The monthly payment is: {:.2f}".format(monthly_payment))

if __name__ == "__main__":
    main()