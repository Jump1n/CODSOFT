from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

calci_on = True
while calci_on:
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)

    done_calculating = False
    while not done_calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation."
                                f" Type 'q' to quit. : ").lower()

        if should_continue == "y":
            num1 = answer
        elif should_continue == "n":
            done_calculating = True
        elif should_continue == "q":
            print("Turning off!")
            done_calculating = True
            calci_on = False
        else:
            print("Invalid choice!\nRestarting.")
            done_calculating = True


