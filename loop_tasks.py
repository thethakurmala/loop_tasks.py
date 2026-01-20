# TASK 4: Loops & Iterations Demonstration

print("---- For Loop: Print numbers 1 to 100 ----")
for i in range(1, 101):
    print(i, end=" ")

print("\n\n---- While Loop: Countdown Timer ----")
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("🚀 Countdown Finished!")

print("\n---- Break and Continue Example ----")
for num in range(1, 11):
    if num == 5:
        print("Breaking loop at", num)
        break
    print(num)

print("\nContinue Example (Skip even numbers):")
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)

print("\n---- Iterating Over String ----")
word = "Python"
for char in word:
    print(char)

print("\n---- Multiplication Table ----")
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\n---- Range with Step Value ----")
for i in range(0, 21, 2):
    print(i)

print("\n---- Loop with Condition (Real-world Example) ----")
marks = [45, 78, 88, 32, 90]
for mark in marks:
    if mark >= 40:
        print(mark, "Pass")
    else:
        print(mark, "Fail")
