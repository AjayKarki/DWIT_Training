
"""
This is another method for input of series
user_input = ''
numbers = []
while True:
    val = input("Enter a number (Enter anything else to quit)")
    if val.isdigit():
        numbers.append(int(val))
    else:
        break
"""

numbers = list(map(int, input("\nEnter the numbers (series) : ").split()))
even_count = odd_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count += 1
print("No. of Even numbers ",even_count,"\nNo. of Odd numbers ", len(numbers)-even_count)