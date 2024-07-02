#Calculator: A Project by Lakshya;

import math
print("Python Calculator: -- A Project by Lakshya")
print("if your operation is sqrt then the second value will be ignored.")

#Input the first and second int.
a = input("Input the First integer: ")
b = input("Input the Second integer: ")

#Defining the operations (+,-,*,/,%);
operation = input("Define the Operation(+,-,*,/,%,^,sqrt:")

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
    print(int(a) % int(b))

elif operation == "^":
    print(int(a) ^ int(b))

elif operation == "sqrt":
    print(math.sqrt(int(a)))

else:
    print("The Calculation is Undefined")


# End of the Code; :)
