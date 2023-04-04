# leap year checker

def leap_year(year):
    if year %4 == 0:

        if year %100 == 0:

            if year %400 == 0:
                print("Leap Year")
            else:
                print("Not Leap Year")

        else:
            print('Leap Year')

    else:
        print("Not Leap Year")

def main():
    year = int(input("Enter Year: "))
    leap_year(year)

if __name__ == '__main__':
    main()