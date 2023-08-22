print("Determine whether an input\nnumber is even or odd\n")

def determine_odd_even(input_number):
    return "Even" if input_number % 2 == 0 else "Odd"


while True:
    input_number = input("Enter a number: ")

    if not input_number.replace("-","").isdigit():
        print("Invalid input, please enter a number!")
    else:
        input_number = int(input_number)
        print("\nThe number", input_number, "is an", determine_odd_even(input_number))
        break

print("\nThank you for using our program")


