# 1. Linked lists are dynamic, unlike arrays, which are fixed in size.
# 2. Traversing a linked list involves iterating from the head node to the end.
# 3. Edge cases like an empty list or deleting the head node should always be handled.


class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Reference to the next node, initiall2y None

class LinkedList:
    
    def __init__(self):
        self.head = None  # Initialize the linked list with no nodes

    ''' Insert at the End '''
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            #new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node


    ''' Insert at the Beginning '''
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node


    ''' Delete a Node '''
    def delete(self, key):
        current = self.head
        # Case 1: If the list is empty
        if not current:  
            print("List is empty.")
            return
        # Case 2: If the head node is the one to be deleted
        if current.data == key:
            self.head = current.next
            current = None  # Free the memory (optional in Python as it's garbage collected)
            return
        # Case 3: Traverse the list to find the node to delete
        prev = None
        while current:
            if current.data == key:
                prev.next = current.next  # Skip the current node to delete it
                current = None  # Free the memory
                return
            prev = current
            current = current.next
        # Case 4: If the key is not found
        print(f"Key {key} not found in the list.")


    ''' Display the List '''  
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    ''' Get Length of the Linked List '''
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


    ''' Search for an Element '''
    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position  # Return the index if found
            current = current.next
            position += 1
        return -1  # Return -1 if the element is not found


    ''' Insert at a Specific Position '''
    def insert_at_position(self, data, position):
        if position < 0:
            raise ValueError("Position must be a non-negative integer.")

        new_node = Node(data)    #create a new node with self.data= data , self.next=None
        if position == 0:  # Insert at the head
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 1):
            if not current:
                print("Position out of bounds.")   # raise IndexError("Position out of bounds.")
                return 
            current = current.next
        new_node.next = current.next
        current.next = new_node

# pos=3
# _ _ _ __  _ _ _
# 0 1 2 NN  3 4 5
# c c c
#   0 1 

    
    ''' Reverse the Linked List '''
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev to current
            current = next_node  # Move current to next
        self.head = prev  # Update head



    ''' Remove Duplicates '''
    def remove_duplicates(self):
        current = self.head
        seen = set()
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next



    ''' Find the Middle Element '''
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None



    ''' Check if the List Contains a Cycle '''
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



    ''' Rotate a Linked List '''
    def rotate(self, k):
        if not self.head or k == 0:
            return
        
        # Compute the length
        current = self.head
        length = 1
        while current.next:
            current = current.next
            length += 1
        
        k %= length
        if k == 0:
            return
        
        current.next = self.head  # Make it circular
        temp = self.head
        
        # Move to the (length - k)th node
        for _ in range(length - k - 1):
            temp = temp.next
        
        # Update the head and break the circular connection
        self.head = temp.next
        temp.next = None



    '''  Nth Node from the End of the Linked List '''
    # Approach 1 : Two-pointer technique
    def nth_from_end(self, n):
        first = self.head
        second = self.head
        
        # Move first pointer n steps ahead
        for _ in range(n):
            if not first:
                return None
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        return second.data if second else None

    # Approach 2: length-based method
    def nth_from_end_length_based(self, n):
        # S1: Find the length of the linked list
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        # S2: Calculate the (length - n)th position
        target = length - n
        if target < 0:  # If n is greater than the length of the list
            return None
        # S3: Move to the target node
        current = self.head
        for _ in range(target):
            current = current.next
        return current.data if current else None



    ''' Delete Last Occurrence of an Item '''
    def delete_last_occurrence(self, key):
        current = self.head
        last_occurrence = None
        prev = None
        
        # Find last occurrence
        while current:
            if current.data == key:
                last_occurrence = prev
            prev = current
            current = current.next
        
        if not last_occurrence:
            return
        
        # Remove the last occurrence
        if last_occurrence.next:
            last_occurrence.next = last_occurrence.next.next



    '''  Delete Middle of Linked List '''
    def delete_middle(self):
        if not self.head or not self.head.next:
            self.head = None
            return
        
        slow = self.head
        fast = self.head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Remove the middle node
        prev.next = slow.next



    '''  Remove Duplicates from a Sorted Linked List '''
    def remove_duplicates_sorted(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next



    '''  Delete N Nodes After M Nodes '''
    def delete_n_after_m(self, m, n):
        current = self.head
        
        while current:
            # Skip M nodes
            for _ in range(m - 1):
                if not current:
                    return
                current = current.next
            
            # Delete N nodes
            temp = current
            for _ in range(n):
                if not temp or not temp.next:
                    break
                temp.next = temp.next.next
            
            current = temp.next



    '''  Remove Every K-th Node '''
    def remove_kth_node(self, k):
        if k <= 0:
            return
        
        current = self.head
        prev = None
        count = 1
        
        while current:
            if count % k == 0:
                prev.next = current.next
            else:
                prev = current
            current = current.next
            count += 1



    ''' Pairwise Swap of Linked List '''
    def pairwise_swap(self):
        current = self.head
        
        while current and current.next:
            current.data, current.next.data = current.next.data, current.data
            current = current.next.next

    ''' Occurrence of an Integer '''
    def count_occurrences(self, key):
        count = 0
        current = self.head
        
        while current:
            if current.data == key:
                count += 1
            current = current.next
        
        return count



    ''' Sort a Linked List of 0s, 1s, and 2s '''
    def sort_012(self):
        count = [0, 0, 0]
        current = self.head
        
        # Count occurrences
        while current:
            count[current.data] += 1
            current = current.next
        
        current = self.head
        for i in range(3):
            while count[i] > 0:
                current.data = i
                current = current.next
                count[i] -= 1



    ''' Add Two Numbers Represented by Linked Lists - with dummy node as result'''
    def add_two_numbers(self, l1, l2):
        result  = Node(0)   # taking 0 as data - 1st node
        current = result
        carry = 0
        
        while l1 or l2 or carry:
            total = carry
            
            if l1:
                total += l1.data
                l1 = l1.next

            if l2:
                total += l2.data
                l2 = l2.next 
                 
            carry = total // 10
            current.next = Node(total % 10)
            current = current.next
        
        return result.next

    
    ''' Add Two Numbers Represented by Linked Lists - no dummy node '''
    def add_two_numbers2(self, l1, l2):
        add_ll = LinkedList()  # Create an empty linked list as added linkedlist
        carry = 0  
    
        while l1 or l2 or carry:
            total = carry  
    
            if l1:  
                total += l1.data
                l1 = l1.next
    
            if l2:  
                total += l2.data
                l2 = l2.next
    
            carry = total // 10  
            add_ll.append(total % 10)  
    
        return add_ll  

    
    ''' Convert Linked List to Number '''
    def ll_to_number(self):
        current = self.head
        number = 0 
        while current:
            number = number*10 + current.data
            current=current.next
        return number
    
    ''' Multiply Two Numbers Represented by Linked Lists '''
    def multiply_two_numbers(self, l1, l2):
        num1, num2 = 0, 0
        
        while l1:
            num1 = num1 * 10 + l1.data
            l1 = l1.next
        
        while l2:
            num2 = num2 * 10 + l2.data
            l2 = l2.next
        
        product = num1 * num2
        dummy = Node(0)
        current = dummy
        
        for digit in str(product):
            current.next = Node(int(digit))
            current = current.next
        
        return dummy.next



    ''' Merge Two Sorted Linked Lists '''
    def merge_sorted(self, l1, l2):
        dummy = Node(0)
        current = dummy
        
        while l1 and l2:
            if l1.data <= l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        
        return dummy.next


## ------------- Examples  --------------- : 

def test_linked_list():
    print("Testing LinkedList Methods\n")
    
    # Create a linked list and add elements
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print("Initial List:")
    ll.display()

    #-------------------------------
    
    # Test append
    print("\nAppending 6 to the list:")
    ll.append(6)
    ll.display()

    #-------------------------------
    
    # Test prepend
    print("\nPrepending 0 to the list:")
    ll.prepend(0)
    ll.display()
    
    #-------------------------------
    
    # Test delete
    print("\nDeleting node with value 3:")
    ll.delete(3)
    ll.display()

    #-------------------------------
    
    # Test get_length
    print("\nLength of the list:", ll.get_length())

    #-------------------------------
    
    # Test search
    print("\nSearching for node with value 4:", ll.search(4))

    #-------------------------------
    
    # Test insert_at_position
    print("\nInserting 9 at position 3:")
    ll.insert_at_position(9, 3)
    ll.display()

    #-------------------------------
    
    # Test reverse
    print("\nReversing the list:")
    ll.reverse()
    ll.display()

    #-------------------------------
    
    # Test remove_duplicates
    print("\nRemoving duplicates:")
    ll.remove_duplicates()
    ll.display()

    #-------------------------------
    
    # Test find_middle
    print("\nMiddle element of the list:", ll.find_middle())

    #-------------------------------
    
    # Test has_cycle
    print("\nChecking for cycle in the list:", ll.has_cycle())

    #-------------------------------
    
    # Test Rotation
    print("\nRotating the list by 2:")
    ll.rotate(2)
    ll.display()

    #-------------------------------
    
    # Test Nth node from end
    n = 2
    print(f"\n{n}th node from the end:", ll.nth_from_end(n))

    #-------------------------------
    
    # Test delete last occurrence
    ll.append(3)
    print("\nDeleting last occurrence of 3:")
    ll.delete_last_occurrence(3)
    ll.display()

    #-------------------------------
    
    # Test delete middle
    print("\nDeleting middle node:")
    ll.delete_middle()
    ll.display()

    #-------------------------------
    
    # Test removing duplicates in a sorted list
    ll_sorted = LinkedList()
    for val in [1, 1, 2, 2, 3, 3, 4, 5, 5]:
        ll_sorted.append(val)
    print("\nSorted List Before Removing Duplicates:")
    ll_sorted.display()
    ll_sorted.remove_duplicates_sorted()
    print("Sorted List After Removing Duplicates:")
    ll_sorted.display()

    #-------------------------------
    
    # Test delete N nodes after M nodes
    print("\nDeleting 2 nodes after 2 nodes:")
    ll.delete_n_after_m(2, 2)
    ll.display()

    #-------------------------------
    
    # Test remove every k-th node
    print("\nRemoving every 2nd node:")
    ll.remove_kth_node(2)
    ll.display()

    #-------------------------------
    
    # Test pairwise swap
    print("\nPairwise swapping elements:")
    ll.pairwise_swap()
    ll.display()

    #-------------------------------
    
    # Test occurrence count
    key = 2
    print(f"\nOccurrence of {key} in list:", ll.count_occurrences(key))

    #-------------------------------
    
    # Test sort 0s, 1s, and 2s
    ll012 = LinkedList()
    for val in [2, 1, 0, 2, 1, 0, 1, 2, 0]:
        ll012.append(val)
    print("\nUnsorted 0-1-2 List:")
    ll012.display()
    ll012.sort_012()
    print("Sorted 0-1-2 List:")
    ll012.display()

 #-------------------------------
    
    # Test addition of two numbers as linked lists
    l1, l2 = LinkedList(), LinkedList()
    for val in [2, 4, 3]:  # Represents 342      # convert number to linkedlist (given reverse number in List - inorder to add them)  
        l1.append(val)
    for val in [2, 4, 0]:  # Represents 240
        l2.append(val)
    
    print("\nAdding two linked list numbers:")
    result = ll.add_two_numbers(l1.head, l2.head)
    while result:
        print(result.data, end=" -> ")
        result = result.next
    print("None")

#-------------------------------
    # Add 2 Number using linked list
    
    # # Input numbers
    # n1 = int(input("Enter 1st number : "))  
    # n2 = int(input("Enter 2nd number : "))  
    n1 = 342
    n2 = 240
    
    # Create linked lists for both numbers
    ll1 = LinkedList()        #ln1 : LinkedList Number 1
    ll2 = LinkedList()       
    
    while n1:                   # convert number to linkedlist (reverse - inorder to add them)  
        ll1.append(n1 % 10)      # 2->4->3    [342]
        n1 //= 10
    
    while n2:
        ll2.append(n2 % 10)      # 0->4->2    [240]
        n2 //= 10
    
    result_ll = LinkedList()
    result_ll = result_ll.add_two_numbers2(ll1.head, ll2.head)       # Compute sum of 2 linked lists l1, l2
    
    # Print sum in reverse (default)
    print("Sum in reversed order:")
    result_ll.display()

    # Reverse LList - correct order of sum
    result_ll.reverse()

    print("Sum in correct order:")
    result_ll.display()

    #Convert LinkedList to Integer number and print it.
    summ = result_ll.ll_to_number()    # 582 (Total)
    print("sum is = ",summ)
    
    #-------------------------------
    
    # Test multiplication of two numbers as linked lists
    print("\nMultiplying two linked list numbers:")
    result = ll.multiply_two_numbers(l1.head, l2.head)
    while result:
        print(result.data, end=" -> ")
        result = result.next
    print("None")

    
    # Test merging two sorted lists
    l1, l2 = LinkedList(), LinkedList()
    for val in [1, 3, 5]:
        l1.append(val)
    for val in [2, 4, 6]:
        l2.append(val)
    
    print("\nMerging two sorted linked lists:")
    merged_head = ll.merge_sorted(l1.head, l2.head)
    while merged_head:
        print(merged_head.data, end=" -> ")
        merged_head = merged_head.next
    print("None")
    
    print("\nAll tests completed successfully.")

# Run the tests
test_linked_list()
