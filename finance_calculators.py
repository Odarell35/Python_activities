import math
# The program is  an investment calculator and a home loan repayment calculator.
# The user  should be allowed to choose which calculation they want to do


def main():
    print("Choose the calculation you want to perform:")
    print("Bond-    \t to calculatee the amount you have to pay on a home loan")
    print("Investment- \t to calculate the amount of interest you will earn")

    choice = input("Enter your choice (bond/investment): ").strip().lower()

    if choice == "bond":
        print("You have chosen Bond calculation.")
        amount = int(input("Enter value of house: "))
        rate = int(input("Enter interest rate: "))
        years = int(input("Enter number of months they plan to take to repay the bond: "))
        repayment = ((rate / 1200) * amount) / (1 - math.pow((1 + (rate/1200)), (-years*12)))
        print("Repayment amount each month: R ", repayment)
    elif choice == "investment":
        print("You have chosen Investment calculation.")
        amount = int(input("Enter amount to invest: "))
        rate = int(input("Enter interest rate: "))
        years = int(input("Enter number of years they plan on investing for: "))
        interest = input("Enter your choice (simple/compound): ").strip().lower()
        if interest == "simple":
            total = amount * (1 + rate / 100 * years)
            print(total)
        elif interest == "compound":
            total = amount * math.pow((1 + (rate // 100)), years)
            print(total)
        else:
            print("invalid choice")
    else:
        print("Invalid input. Please enter 'bond' or 'investment'.")

if __name__ == "__main__":
    main()
