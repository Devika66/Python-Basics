def sumlist(list1, list2):
    total_sum = 0
    for i, j in zip(list1, list2):  # Use zip to iterate over both lists simultaneously
        total_sum += i + j          # Add both elements to the sum
    return total_sum


n = int(input("Enter the range: "))
l1 = []
l2 = []

print("Enter the numbers for list 1:")
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    l1.append(num)

print("Enter the numbers for list 2:")
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    l2.append(num)

result = sumlist(l1, l2)
print("Sum of l1 and l2 =", result)
