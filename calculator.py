#simple python program for calculator that performs basic arthimetic operations
#prompts the user to enter two input values and displays the result
def add(x,y):
    return x + y 

def subtract(x,y):
    return x - y 

def multiply(x,y):
    return x * y 

def divide(x,y):
    if y != 0:
        return x / y 
    else:
        return "Error: Division by zero is not allowed"

def calculator():
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("Enter choice from 1,2,3,4: ")

        if choice in ['1','2','3','4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input.Enter correct values")
                continue
            
            if choice == '1':
                print("{} + {} = {}".format((num1),(num2),(add(num1,num2))))
            elif choice == '2':
                print("{} - {} = {}".format((num1),(num2),(subtract(num1,num2))))
            elif choice == '3':
                print("{} * {} = {}".format((num1),(num2),(multiply(num1,num2))))
            elif choice == '4':
                print("{} / {} = {}".format((num1),(num2),(divide(num1,num2))))

            #asking the user for next calculation
            next_calculation = input("perform another arthimetic operation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid input. Select valid operation")

if __name__ == "__main__":
    calculator()
