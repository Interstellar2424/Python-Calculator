import math

print("calculator")
print("if your operation is square then the 2nd integer will be ignored.")
a = input("set value for a: ")
b = input("set value for b: ")

operation = input("define operation:(+,-,*,/,%,^,square root)")

if operation == "+":
  print(float(a) + float(b))

elif operation == "-":
    print(float(a) - float(b))

elif operation == "*":
    print(float(a) * float(b))
    
elif operation == "/":
    print(float(a) / float(b))
    
elif operation == "%":
    print(float(a) % float(b))

elif operation == "^":
    print(float(a) ** int(b))
    
if operation == "square root":
    print(math.sqrt(float(a)))
    

#end of code :)