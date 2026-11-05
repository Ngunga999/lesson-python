def hello_world():
    print("Hello world!")

hello_world()

def sum(num1 =0 , num2=0):
    if (type(num1) is not int or type(num2) is not int):
       return 0 
    return num1 + num2

total = sum(5, 10)
print(total)

def multiple_items(*args):
    total = 0
    for num in args:
        total += num
    return total

result = multiple_items(1, 2, 3, 4, 5)
print(result)

def multiple_items(*args):
    print(args)
    print(type(args))

    multiple_items("apple", "banana", "cherry")

    def mult_named_items(**kwargs):
        print(kwargs)
        print(type(kwargs))


    mult_named_items (fruit1="apple", fruit2="banana", fruit3="cherry")
