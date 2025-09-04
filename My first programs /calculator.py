def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
functions_dictionary = {"+": add,
                        "-": sub,
                        "*": mult,
                        "/": div,

}
def calculator():
    number1 = float(input("What is your first number? "))
    countinue_accumulating = True
    while countinue_accumulating:
        for sym in functions_dictionary:
            print(sym)
        choosen_operation = input("Choose the operation: ")
        number2 = float(input("What is the next number? "))
        outcome = functions_dictionary[choosen_operation](number1, number2)
        print(f"{number1} {choosen_operation} {number2} = {outcome}")
        wants_to_continue = input("Type 'yes' if you want to continue calculating, type 'no' if you want to start a new calculation: ").lower()
        if wants_to_continue == "yes":
            number1 = outcome
        else:
            countinue_accumulating = False
            calculator()

calculator()
