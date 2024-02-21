def classify_number(num):
    if num < 0:
        print("The Number is negative.")
    elif num == 0:
        print("The Number is  Zero.")
    elif num > 0:
        print("The Number is positive.")
        
num = int(input("Enter a Number:"))
classify_number(num)
