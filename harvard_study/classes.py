class Point():
#All functions that operate on objects themselves are going to take the first argument called 
# "self", and this argument "self" represents the object in question, helps to store then inside 
# of there selfs.
    def __init__(self, x, y):
#Recall the "self" representing the point itself, and if we want to store data inside of that point
#and allow that point to store its own x and y values, then we need to store that data inside of
# the "self".           
        self.x = x
        self.y = y

# If I want to create a new point call p:
p = Point(2, 8)
print(p.x)
print(p.y)