# value = 1
# while value < 10:
#   print(value)
#   if value == 5:
#        break
#   value += 1


names = ["John", "Paul", "George", "Ringo"]

# for X in names:
#   if X == "George":
#       break
#    print(X)

#   for X in names:
#        if X == "George":
#        continue
#   print(X)

#for X in range(4):
#   print(X)
    
    
#for X in range(2, 4):
#    print(X)

#for X in range(0, 100, 5):
#    print(X)

for X in range(5, 101, 5):
    print(X)
else:
    print("Glad that/s over!")

    names = ["John", "Paul", "George", "Ringo"]
    actions = ["sing", "play guitar", "play bass", "play drums"]

# for name in names:
#  for action in actions:
#       print(f"{name} can {action}")

for action in actions:
    for name in names:
        print(f"{name} can {action}")

        