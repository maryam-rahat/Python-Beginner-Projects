# currency conversion
# (usage of lambda function)

def main():
    print("This program converts USD to INR according to exchange rate on 03/25/2023")
    print('')

    dollars = eval(input("Input amount in dollars ($): "))
    inr = convert_to_inr(dollars)

    print("That is", inr, "INR")

convert_to_inr = lambda dollars: dollars * 82.35

main()
