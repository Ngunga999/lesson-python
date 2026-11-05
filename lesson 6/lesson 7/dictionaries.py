# Dictionaries
band = {
    "vocals": "plant" ,
   "guitar": "Page", 
}
band2 = dict(vocals="Plant", guitar="Page")


print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))


# list all keys
print(band.keys())

# list all values
print(band.values())

# list all items
print(band.items())

# list of key/value pairs as tuples
print(band.items())

#verify if key exists
print("guitar" in band)
print("triangle" in band)

#change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

print(band.pop("bass"))
print(band)

band ["drums"] = "Bonham"
print(band)

print(band.popitem())      #tuple
print(band)

#delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

#copy dictionaries

# band2 = band # creates a reference to the original dictionary
# print("bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Ngunga"
# print(band)

band2 = band.copy() 
band2["drums"] = "Ngunga"
print("good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("good copy!")
print(band3)

# Nested dictionaries

member1 = {
    
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    
    "name": "Jimmy Page",
    "instrument": "guitar"
}
band = {
    
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# sets

nums = {1, 2, 3, 4, 5}

nums2 = set([1, 2, 3, 4,])

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed
nums  = {1, 2, 2, 3, }
print(nums)

# True is a dupe of 1, false is a dupe of 0

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#check if value is in set

print(2 in nums)

# But you cannot refer to an element in the set with an index position or key 

# add a new element to the set

nums.add(8)
print(nums)

#Add elements from one set to another
more_nums = {9, 10, 11}
nums.update(more_nums)
print(nums)

# You can use update with lists, tuples, and dictionaries as well

#Merge two to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1, 2, 3}
two = {5, 6, 1}

one.intersection_update(two)
print(one)

# Keep everything excepts the duplicates
one = {1, 2, 3}
two = {5, 6, 1}

one.symmetric_difference_update(two)
print(one)