#Welcome to the Fibonacci Calculator

print("#Welcome to the Fibonacci Calculator App\n")

#Getting user input
num_digits = int(input("how many digits of the Fibonacci sequence would you like to compute? "))

#Calculating the printing the Fibonacci sequence
print(f"\nThe first {num_digits} numbers of the Fibonacci sequence are:")

num1 = 1
num2 = 0
series = []

for i in range(num_digits):
  num = num1 + num2
  print(num)
  series.append(num)
  num1 = num2
  num2 = num

print(f"\nThe golden ratios are: ")
for i in range(1,len(series)):
  ratio = series[i] / series[i-1]
  print(ratio)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi: 1.618 ....")

