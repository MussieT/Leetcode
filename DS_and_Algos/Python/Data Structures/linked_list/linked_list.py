class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # If we just used self.head node, we will be replacing it
        currrent_node = self.head
        while currrent_node.next is not None:
            currrent_node = currrent_node.next
        
        currrent_node.next = new_node
    
    def print_list(self):

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print("mid is: ", slow.data)

    def remove_nth_from_back(self, nth=0):
        fast = self.head
        slow = self.head

        # move the fast in to nth ,position
        # then move the slow until fast finishes, slow will be just in nth element
        for _ in range(nth):
            print("k is k")
            fast = fast.next

        # it came to the beginning of the array
        if fast is None:
            self.head = self.head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        self.print_list()

    def swap_nodes(self):
        slow = self.head
        fast = self.head.next
        temp = Node(slow.data)

        self.head = fast
        slow.next, fast.next = fast.next, slow

        fast = fast.next

        print("slow: ", slow.data)

        # procedures, first move the second to the first, pointing to the first.
        # then, the second element should point to the second element of the second pointer
        # have second pointer as current, the swapped should point to current .. and goes on

        while fast and fast.next:
            slow.next, fast.next = fast.next, slow

            # fast = fast.next
        

            slow = slow.next

            # slow.next = fast

            print("fast: ", temp.data)
            # slow.next.next = fast

            fast = fast.next
          
            
        
        self.print_list()


# merge_sorted_arrays()
# [1, 2] [1, 2, 3]
new_list = LinkedList()
new_list.append(0)
new_list.append(2)
new_list.append(4)
new_list.append(5)
new_list.append(6)
new_list.append(9)
new_list.swap_nodes()
