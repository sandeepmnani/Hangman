# Read user input
income = int(input())
percent = 0
# Income tax calculation
if income in range(0, 15527):
    percent = 0
elif income in range(15528, 42708):
    percent = 15
elif income in range(42708, 132407):
    percent = 25
elif income >= 132407:
    percent = 28
try:
    calculated_tax = tax = (income / 100) * percent
except ZeroDivisionError:
    calculated_tax = 0

print(f'The tax for {income} is {percent}%. That is {calculated_tax:.0f} dollars!')
