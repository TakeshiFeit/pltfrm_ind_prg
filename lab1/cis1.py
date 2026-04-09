from datetime import datetime


# main program
def main():
    # checking what year it is
    # then convert result into int format
    year = int(datetime.now().strftime("%Y"))

    # input block
    print(f"****************************************\n*           Personal business card            *\n****************************************")
    name = input("Enter Your name: ")
    surname = input("Enter Your surname: ")
    dateOfBirth = int(input("Enter Your year of birth: "))
    height = int(input("Enter your height (cm): "))

    # print block
    print(f"****************************************\n*           Your business card            *\n****************************************")
    print(f"* Your name: {name} *")
    print(f"* Your surname: {surname} *")
    print(f"* Your date of birth: {dateOfBirth} *")
    print(f"* Your age: {year - dateOfBirth} *")
    print(f"* Your height: {height}(cm) *")
    print(f"****************************************")

if __name__ == "__main__":
    main()
    input(f"\nPress Enter for exit...")
