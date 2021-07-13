#This program is for variables

a =1 #integer
b= 1.56 #float
c=3+4j #complex
d="Srting" #string


print(type(c))

print("{} {}".format("Data Type of variable a is ",type(a)))
print("{} {}".format("Data Type of variable b is ",type(b)))
print("{} {}".format("Data Type of variable c is ",type(c)))
print("{} {}".format("Data Type of variable d is ",type(d)))

e=(1,2,3,4)

print(e)
print("{} {}".format("Data Type of variable e is ",type(e)))

f=[1,2,3,4,5]

print(f)
print("{} {}".format("Data Type of variable f is ",type(f)))

g={1:"A",2:"B",3:"C"}
print("{} {}".format("Data Type of variable g is ",type(g)))

f.append("bero")
f.insert(4,"karma")
print(f)

f.remove(4)

print(f)