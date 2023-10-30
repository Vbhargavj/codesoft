def main():
    
    a = float(input("Enter the number 1 "))
    b = float(input("Enter the number 2 "))

    print("Choose valid option to perform an action")
    print("1 for addition")
    print("2 for substraction")
    print("3 for multipication")
    print("4 for division")

    op = int(input("Enter a valid operation "))

    res = operation(a,b,op)
    
    if res==False:
        print('Enter valid option')
        main()
    else:
        print(res)
        
        


def operation(a, b, option):
    if option == 1:
        return a + b
    elif option == 2:
        return a - b
    elif option == 3:
        return a * b
    elif option == 4:
        return a / b
    else :
        return False

if __name__ == "__main__":
    print("simple calc")
    main()