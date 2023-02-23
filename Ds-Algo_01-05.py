# 1. Find the minimum and maximum element in an array.

#arr = [45, 78, 90, 32, 67, 89, 33, 54, 78, 34]

''' arr.sort()   # O(nlogn) time complexity

 print("Minimum = ", arr[0], "Maximum = ", arr[len(arr) - 1])'''

'''maximum_element = arr[0]
minimum_element = arr[0]

for i in range(len(arr)):
    # maximum_element = max(maximum_element, arr[i])
    # minimum_element = min(minimum_element, arr[i])
    if arr[i] > maximum_element:
        maximum_element = arr[i]
    if arr[i] < minimum_element:
        minimum_element = arr[i]

print("Minimum = ", minimum_element, "Maximum = ", maximum_element)'''


# 2. Cyclically rotate an array by one.

#arr = [1, 2, 3, 4, 5]

'''x = arr[len(arr) - 1] # 95

for i in range(len(arr) -1, 0, -1):
    # start=4, stop=0, step=-1
    arr[i] = arr[i-1]

#[1, 1, 2, 3, 4]
arr[0] = x

print(arr)'''

'''arr = arr[-1:] + arr[:-1]
print (arr)'''


# 3. Find the largest sum of contiguous subarray/ Kadane's Algorithm

'''arr = [-2, -3, 4, -1, -2,  1, 5, -3]

result = arr[0]
sum = 0
start = 0 
end = 0 

for i in range(len(arr)):
    sum = sum + arr[i]
    if result < sum:
        result = sum
        end = i
    if sum < 0:
        sum = 0
        start = i + 1

print(arr[start: end + 1])
print(result)'''

# 4. Find if an array is subset of another array

'''arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]

temp = set(arr1 + arr2)

if len(temp) == len(arr1):
    print("Is a Subset")
else:
    print("Is not a Subset")'''

# 5.Rotate a matrix by 90 degree

matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9]
         ]

print(matrix)

for row in range(len(matrix)):
    for col in range(0, row):
        matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

print(matrix)

'''n = len(matrix)
for row in range(n):
    for col in range(n // 2):
        matrix[row][col], matrix[row][n-1-col] = matrix[row][n-1-col], matrix[row][col]
'''
for row in matrix:
    row = row.reverse()
print(matrix)

























