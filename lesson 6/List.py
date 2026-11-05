users = ("John", "Jane", "Ngunga", )

data = ["Ngunga", 27, True, ]

empty_list = []

print("Ngunga" in empty_list)

print(users[0])
print(users[-2])

print(users.index('Jane'))

print(users[0:2])
print(users[1])
print(users[-3:-1])

print(len(data))

users=['Mike']
print(users)

users  += ['Ngunga']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'John')
print(users)

users[2:2] = ['Karen', 'Mary']
print(users)

users[1:3] = ['Alice', 'Bob']
print(users)

users.remove('Ngunga')
print(users)

users.pop(0)
print(users)

del users[1]
print(users)

#del data
data.clear()
print(data)

users.sort()
print(users)

users[1:2] = ['Ngunga']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [10, 50, 21, 52, 11]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil" , True, ])
print(mylist)

#tuples

mytuple = tuple(('Ngunga', 27, True, ))

another_tuple = (1,6,5,9, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(another_tuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = another_tuple
print(one)
print(two)
print(hey)

print(another_tuple.count(2))
