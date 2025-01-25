
# ----- Min Heap methods (how they are implemented internally ) --- ---  Note :  In  reality these are implemented using c language but in same way with same logic


class MinHeap:
    def __init__(self):
        self.heap = [] 
    
    def heappush(self,val):
        self.heap.append(val)
        self._bubble_up(len(self.heap)-1)
 
    def heapop(self):
        if not self.heap:
            return
        if len(self.heap)==1:
            return self.heap.pop()      
        
        root = self.heap[0]
        self.heap[0]=self.heap.pop()     #replace root with last element
        self._bubble_down(0)
        return root
        
    def peak(self):
        return self.heap[0] if self.heap else None
        
    def _bubble_up(self,index):
        parent = (index-1) // 2
        if index>0  and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)
    
    def _bubble_down(self,index):
        smallest = index
        left = 2*index + 1
        right = 2*index + 2
        
        if left < len(sef.heap) and self.heap[left]<self.heap[smallest]:
            smalles=left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index :
            self.heap[index], self.heap[smallest] = self.heapp[smallest], self.heapp[index]
            self._bubble_down(smallest)
            
            
         
    def heapreplace(self, val):     ##  Replace  root with the given value & restore the heap property.(heapify)
    
        if not self.heap:
            return None
        
        root =  self.heap[0]
        self.heap[0] = val 
        self._bubble_down(0)   # Restor heap property starting from the root.
        return root
        
    
    
    def heapify(self):    #convert list into valid min-heap
        n = len(self.heap)
        for i in range(n//2 - 1 , -1 , -1) : 
            self._bubble_down(i)
    
            
 # Usage
heap = MinHeap()
heap.heappush(10)
heap.heappush(5)
heap.heappush(15)
print(heap.heappop())  # Output: 5
print(heap.peek())     # Output: 10



    
#####################################################

class CustomList:
    def __init__(self):
        self.data = []
        self.size = 0  # Tracks the number of elements


    def append(self, val):
                                          # If the internal array is "full," create a new array with more capacity
        if self.size == len(self.data):  # Simulating dynamic resizing
            self._resize()

        self.data[self.size] = val         # Add the new value at the end
        self.size += 1


    def _resize(self):
        new_capacity = max(1, len(self.data) * 2)    # Create a new array with double the capacity
        new_data = [None] * new_capacity

        for i in range(self.size):            # Copy existing elements into the new arra
            new_data[i] = self.data[i]

        self.data = new_data               # Replace old array with the new one


    def __str__(self):
        return str(self.data[:self.size])       # Display only the elements in the current lis
        
        
custom_list = CustomList()
custom_list.append(1)
custom_list.append(2)
custom_list.append(3)
print(custom_list)  # Output: [1, 2, 3]









