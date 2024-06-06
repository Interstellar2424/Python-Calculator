#Calculator: A Project by Lakshya;

print("Calculator: A Project by Lakshya")

#Input the first and second int.
a = input("Input the First integer: ")
b = input("Input the Second integer: ")

#Defining the operations (+,-,*,/,%);
operation = input("Define the Operation: ")

#conditioning and calculating with first and second Integer by Implementing the the 5 Operations (+,-,*,/,%);
if operation == "+":
    print(int(a) + int(b))

elif operation == "-":
    print(int(a) - int(b))

elif operation == "*":
    print(int(a) * int(b))

elif operation == "/":
    print(int(a) / int(b))

elif operation == "%":
    print(int(a) / int(b))

else:
    print("The Calculation is Undefined")


# End of the Code; :)