# import numpy as np   

# arr1 = np.array([12,2,23,21,4,233,45,765,23])
# secLar = arr1[0]
# secLar1 = arr1[0]
# for i in arr1:
#     if i > secLar:
#         secLar = i    
# for i in arr1:
#     if i < secLar and i > secLar1:
#         secLar1 = i  
# print(secLar1)

def find_second_largest(arr):
    # Check if the array has at least two elements
    if len(arr) < 2:
        return "Array must have at least two elements."
    
    # Initialize the largest and second largest elements
    largest = second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            # Update second largest before updating largest
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            # Update second largest only if it's not equal to largest
            second_largest = num
    
    return second_largest if second_largest != float('-inf') else "No second largest element exists."

# Example usage
array = [12, 35, 1, 10, 34, 1]
result = find_second_largest(array)
print(f"The second largest element is: {result}")
