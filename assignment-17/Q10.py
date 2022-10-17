s1 = [eval(e) for e in input("Enter value :").split(',')]
s1 = set(s1)
print(s1)

print("maximum value is {} and minimum value is {}".format(max(s1),min(s1)))