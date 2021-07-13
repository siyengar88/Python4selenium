#Python program to interchange first and last elements in list
li=[1,2,3,4,5,6,7,8]
print("{} {}".format("Original List: ",li))
temp=li[-1]         #storing the last element in a temporary variable
li[-1]=li[0]        #Bringing first element to last position
li[0]=temp          #storing last element in first position
print("Exchanging first and last elements in the list.")
print("{} {}".format("List after exchange: ",li))