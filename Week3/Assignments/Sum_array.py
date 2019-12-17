def sum_of_numbers(nums):
    sums = 0
    for n in nums:
        sums += n
    return sums
# Alternatively return sum(nums)


numbers = list(map(int, input("Enter the numbers (series) : ").split()))
print("Sum of numbers is ", sum_of_numbers(numbers))