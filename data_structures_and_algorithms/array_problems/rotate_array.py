# Write a function to rotate an array. You are given the array arr,
# n, the size of an array, and d, the number of elements to pivot on
 
 # [1,2,3,4,5,6,7], n = 7, d = 2

 # [3,4,5,6,7,1,2]

def rotate_array(arr, n, d):
    if n == 0:
        return None
    elif n == 1:
        return arr
    return arr[d:] + arr[:d]

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    arr2 = [2,4,6, 8, 10, 12, 14, 16, 18, 20]
    n = 10
    d = 3
    print(rotate_array(arr2, n, d))