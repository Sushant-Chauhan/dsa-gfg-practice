

def small_largest(arr):
    if not arr:
        return None, None  # Handle empty array

    min_elemenet = float('inf')
    max_elemenet = float('-inf')
    for num in arr:
        if num>max_elemenet:
            max_elemenet  = num
        if num<min_elemenet:
            min_elemenet = num
    return [min_elemenet,max_elemenet]
    

def second_small_largest(arr):
    if not arr:
        return None, None
    smallest = second_smallest =  float('inf')
    largest = second_largest = float('-inf')
    
    for num in arr:
        if num>largest:
            second_largest = largest
            largest=num
        elif num<largest and num>second_largest:
            second_largest=num
            
        if num<smallest:
            second_smallest=smallest
            smallest=num
        elif num>smallest and num<second_smallest:
            second_smallest=num
        
    if second_smallest == float('inf'):
        second_smallest = None
    if second_largest == float('-inf'):
        second_largest = None

    return [second_smallest, second_largest]

def reverse_array(arr): 
    i, j = 0, len(arr)-1
    
    while(i<j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i+=1
        j-=1
    return arr
 

def is_sorted(arr):
    for i in range(len(arr)-1):   
        if arr[i] > arr[i+1]:      
            return False
    return True


def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

#--------------------------------------------------------------------------

def linear_search(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    return -1
            
    
def binary_search(arr, target):    #only for sorted arrays
    low, high = 0, len(arr)-1
    
    while low<=high:
        mid = (low+high)//2
        
        if arr[mid]==target:
            return mid
        elif target > arr[mid]:
            low = mid+1
        else:        #target < arr[mid]:
            high = mid-1
    return -1 

# def bubble_sort(arr):
# def selection_sort(arr):
# def insertion_sort(arr):
# def merge_sort(arr):
# def quick_sort(arr, low, high):

    
def kth_smallest(arr, k):
    #1. sort in ascending order (without using inbuilt sorting function) i.e.  arr.sort()
    #2. return k-1 th element
    n = len(arr)
    for i in range(k):
        minidx = i
        for j in range(i+1,n):
            if arr[j] <  arr[minidx]:
                minidx = j
        arr[i] , arr[minidx] = arr[minidx], arr[i]
    return arr[k-1]


# What is a Heap?
# A heap is a special binary tree that follows a specific ordering property. It is not necessarily a balanced tree, but it ensures that the parent node follows a particular order relative to its children.
# 🔹Min Heap
# Properties:
# The parent node is always smaller than or equal to its children.
# The smallest element is always at the root (heap[0] in Python’s heapq).
# It is a complete binary tree, meaning all levels are completely filled except possibly the last level.

# 🔹 Max Heap
# Properties:
# The parent node is always greater than or equal to its children.
# The largest element is always at the root.
# It is also a complete binary tree.

# 🔹 When to Use Min Heap & Max Heap?
# Find the k-th smallest element	Max Heap of size k
# Find the k-th largest element	Min Heap of size k
# Sort elements in increasing order (Heap Sort)	Min Heap
# Sort elements in decreasing order (Heap Sort)	Max Heap


import heapq
# use Min Heap (by default python has Min Heap)
def kth_largest(arr, k):
    min_heap = []
    
    for num in arr:
        heapq.heappush(min_heap, num)  # Push elements normally
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove smallest element
    
    return heapq.heappop(min_heap)  # The root is the k-th largest


# Use Max Heap (i.e. will place -ve sign before no. becoz by default python has min heap )
def kth_smallest(arr, k):
    max_heap = []
    
    for num in arr:
        heapq.heappush(max_heap, -num)  # Push negative values to simulate Max Heap
        if len(max_heap) > k:
            heapq.heappop(max_heap)  # Remove largest in heap (smallest in actual values)
    
    return -heapq.heappop(max_heap)  # Convert back to positive
 
 

def sort_zeros_ones_twos(arr):
    # arr.sort()
    low, mid, high = 0 , 0 , len(arr)-1
    
    while mid<=high:
        if arr[mid]==0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low+=1
            mid+=1
            
        elif arr[mid]==1:
            mid+=1
            
        else:   # arr[mid] == 2
            arr[mid] , arr[high] = arr[high], arr[mid]
            high -= 1
            
    return arr
    
# [2,2,1,0,1,2,0 , 0, 1, 0, 2]  
#  m                        h
#  l


#  move all negative numbers to the left and positive numbers to the right. three-way partitioning approach can be used.
def segregate_neg_pos(arr):
    low,mid = 0,0
    while mid<len(arr):
        if arr[mid] < 0 :
            arr[mid], arr[low] =  arr[low], arr[mid]
            mid += 1
            low+=1
        else:
            mid += 1
            
    return arr
        
# arr = [-1, -3, -6, 4, 5, 2]
#               l
#                          m


def segregate_even_odd(arr):
    low, mid = 0 , 0
    while mid<len(arr):
        if arr[mid]%2 == 0:  # even at beginning
            arr[low] , arr[mid] = arr[mid], arr[low]
            low+=1     
        mid+=1
    return arr
            
# arr = [2, 4, 6, 1, 5, 3]
#              l
#                       m
        
#--------------------------------------------------------------------------

arr = [1, 2, 3, 4, 5, 6]
print("Segregated:", segregate_even_odd(arr))


# arr = [-1, 2, -3, 4, 5, -6]
# print("Segregated:", segregate_neg_pos(arr))

# arr = [2,2,1,0,1,2,0 , 0, 1, 0, 2]  
# print("Sorted:", sort_zeros_ones_twos(arr))

# arr = [10,9,8,7,6,5,4,3,2,1]
# k=3
# print(f"{k}-th Smallest:", kth_smallest(arr, k))
# k = 2
# print(f"{k}-th Largest:", kth_largest(arr, k))


# print("kth_smallest = ", kth_smallest(arr,6))
# arr.sort()
# print(arr)

# print("binary_search: Element is at index = ",binary_search(arr,45))

# print("linear_search: Element is at index = ",linear_search(arr,6))
    
# print("Sum:", sum_of_array(arr))

# print(is_sorted(arr))

# print(reverse_array(arr))

# a,b = second_small_largest(arr)
# print(f' Smallest_Smallest = {a}, Second_Largest = {b}')

# a,b = small_largest(arr)
# print(f'Smallest = {a} , Largest = {b}')
