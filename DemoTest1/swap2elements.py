#python program to swap two elements in a list

li=[22,12,53,6,35,85,32,88,34]
print("{} {}".format("Original List: ",li))
pos1,pos2=3,6
print("{} {} {} {}".format("Exchanging positions at ",pos1," and ",pos2))
temp=li[pos1]
li[pos1]=li[pos2]
li[pos2]=temp
print("{} {}".format("List after exchange: ",li))