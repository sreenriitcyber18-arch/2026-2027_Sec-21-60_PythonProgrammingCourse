# pass statement using a for loop
n = int(input("Enter N (use pass for multiples of 3): "))

for number in range(1, n + 1):
    if number % 3 == 0:
        # placeholder: no action for multiples of 3
        pass
        print(f"Used pass for multiple of 3: {number} (N is {n})")
    else:
        print(f"for loop number = {number} (up to {n})")
# continue statement using a while loop
n = int(input("Enter N (print 1 to N, skip even numbers): "))

number = 1
while number <= n:
    if number % 2 == 0:
        print(f"Skipping even number {number} with continue (N is {n})")
        number = number + 1
        continue
    print(f"while loop odd number = {number} (up to {n})")
    number = number + 1
