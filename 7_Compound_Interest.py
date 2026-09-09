

P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time in years: "))

Amount = P * (1 + R / 100) ** T
CI = Amount - P

print("Amount =", Amount)
print("Compound Interest =", CI)
