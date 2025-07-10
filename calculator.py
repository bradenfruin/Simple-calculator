num_1 = int(input("Enter First Number: "))
num_2 = int(input("Enter Second Number: "))
print("Choose calculation to perform: \n","1. Add\n","2. Subtract\n","3. Multiply\n","4. Devide\n")
cal = input().strip().lower()
if cal == "add":
    ans = num_1 + num_2
elif cal == "subtract":
    ans = num_1 - num_2
elif cal == "multiply":
    ans = num_1 * num_2
elif cal == "devide":
    if num_2 == 0:
        print("Error!!!! Can't Devide by 0")
        ans = None
    else:
        ans = num_1 / num_2
else:
    print("Invalid Operation")
    ans = None
    
if ans is not None:
    print(f"The answer is:",ans,"")