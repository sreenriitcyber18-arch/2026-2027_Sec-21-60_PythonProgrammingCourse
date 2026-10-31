# Apraoch 1 : break statement using a for loop
n = int(input("Enter N (print until N, stop early at 5): "))

for number in range(1, n + 1):
    if number == 5:
        print(f"Breaking for loop at number {number} (N was {n})")
        break
    print(f"for loop number = {number} (up to {n})")
# Approach 2 : break statement using a while loop
n = int(input("Enter N (print until N, stop early at 5): "))

number = 1
while number <= n:
    if number == 5:
        print(f"Breaking while loop at number {number} (N was {n})")
        break
    print(f"while loop number = {number} (up to {n})")
    number = number + 1