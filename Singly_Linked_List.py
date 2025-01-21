
class Node :
  def __init__(self,data): 
	self.data = data  # store data
	self.next = None  # Reference to the next node, initially None


class LinkedList :
   def __init__(self):
   	self.head = None     # Initialize the linked list with no nodes
   

   
   def append(self,data):      ### Insert at the End:
    	NN = Node(data)
        if self.head == None:  # If the list is empty
		self.head = NN
		return
        current = self.head
        while current.next:  # Traverse to the last node
		current = current.next
	NN.next = current.next
	current.next = NN


  
   def prepend(self,data):  ### Insert at the Beginning
	NN = Node(data)
	NN.next = self.head
	self.head = NN

      

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

Note: Python manages memory automatically through garbage collection, so you don’t need to explicitly delete the node as in C++.



   def display(self):
	current = self.head
	while current:
		print(current.data, end="->")
		current = current.next
	print(None)

	

   def get_length(self):
	count=0
	current = self.head
	while current:
		count += 1
		current = current.next
	return count
 


   def search(self,key):
	position = 0
	current = self.head
	while current:
		if current.data==key:
			return position   # Return the index if found
		current = current.next
		position += 1
	return -1     # Return -1 if the element is not found



   def insert_at_position(self,data,position):
	if position<0:
		print("Position must be a non-negative integer")
		return
	
	# NN -> NewNode
	NN = Node(data)     #create a new node with self.data= data , self.next=None

	if position==0 :     #Insert at the hea
		NN.next = self.head
		self.head == NN
		return 

	current = self.head
	for _ in range(position-1):            // 0 , 1, 2
               if not current:
			print("Position out of bounds")
			return 
		current = current.next
	NN.next = current.next
	current.next = NN
	
			

# pos=3
# _ _ _ __  _ _ _
# 0 1 2 NN  3 4 5
# c c c
#   0 1 


def reverse(self):
def remove_duplicates(self):
def find_middle(self):
def has_cycle(self):
def rotate(self, k):
def nth_from_end(self, n):
def delete_last_occurrence(self, key):
def delete_middle(self):
def remove_duplicates_sorted(self):
def delete_n_after_m(self, m, n):
def remove_kth_node(self, k):
def pairwise_swap(self):
def count_occurrences(self, key):
def sort_012(self):
def add_two_numbers(self, l1, l2):
def multiply_two_numbers(self, l1, l2):
def merge_sorted(self, l1, l2):


	