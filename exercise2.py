
######## The following function finds the minimum distance between
#         any pair of equal elements in an array:

#           - Takes an array of integers as an input
#           - Returns: > the minimum distane if there are 
#                           matching pairs in the array
#                      > 0, otherwise

def minimumDistances(array):
    # Create a disctionary that stores array's elements as
    #  keys and the distance to their matching
    #  values, otherwise the index of the element is stored as value 
      
    distances_dictionary = {}
    min_distance = -1
    index = 1
    
    # Iterate over the values in the array to find the matching pairs 
    for e in array:
        if not (e in distances_dictionary):
            # insert element in the dictionary with its
            #  index (converted to negative, to calculate
            #  distance later) as a key
            distances_dictionary[e] = -abs(index) 
        else:
            # matching pair found! update distance
            distances_dictionary[e] += index 
            if(min_distance == -1):
                min_distance = distances_dictionary[e]
            elif(distances_dictionary[e] < min_distance):
                min_distance = distances_dictionary[e]
        index += 1

    print(min_distance)



######## Test exectution: choose a scenario by changing the input of  'open([scenario], "r")'  function

case1 = "assignment02-1.txt"
case2 = "assignment02-2.txt"

input = open(case2, "r")
strings_array = input.readlines()[1].split(" ")
integers_array = [int(s) for s in strings_array]

minimumDistances(integers_array)

# close input file 
input.close()