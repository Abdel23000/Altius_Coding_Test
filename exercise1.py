
######## This function runs the test:
#           - Takes as input the path of the dataset 
#           - Writes the result in an output file "output.txt" 

def run_test(input_path):
    # Open input file that contains the dataset and the output file to write execution results into it
    input = open(input_path, "r")
    output = open("output.txt", "w")

    # Store the number of tests in the variable nb_tests
    nb_tests = int(input.readline())

    for test in range(nb_tests):
        # For each test retrieve the heads of the lists to compare
        node1 = read_linked_list(input)
        node2 = read_linked_list(input)

        # Print comparison's result
        # in the output file
        #  (each comparison in a separate line)
        output.write(str(compare_lists(node1, node2)) + "\n")

    # Close files    
    input.close()
    output.close()  

######## The following function compares two linked-lists:
#           - Takes as input two linked-lists l1,
#                l2 with heads node1 and node2 respectively
#           - Returns: 
#                      > (1) if l1 and l2 have the same size and equal data nodes in order
#                      > (0) otherwise 
#           - Two data nodes are equal if they have equal data attributes


def compare_lists(node1, node2):
    while(node1 != None and node2 != None):
        if int(node1.data) != int(node2.data):
            return 0
            
        else:
            node1 = node1.next 
            node2 = node2.next
    if node1 == None and node2 == None:
        return 1
    else:
        return 0

######## The following function reads and generates
#            a linked-list from the input text file:
#           - Cursor should be pointed to the line that contains the size of the linked-list
#           - It returns the head of the linked-list


def read_linked_list(input):
    size = int(input.readline())
    if size == 0:
        return None
    else:
        head = Node(input.readline())
        node = head
        for i in range(size - 1):
            node.next = Node(input.readline())
            node = node.next
        return head

######## This is the structure of linked-list node:
#           - 'data' is the value stored in the node (data attribute)
#           - 'next' is a reference to the next node in the list, equals to none if the current node is the last


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



######## Test execution: choose a scenario by changing the input of  'run_test([scenario])'  function

case1 = "assignment01-1.txt"
case2 = "assignment01-2.txt"
run_test(case1)





    

