a = input("enter a\n")
b = input("enter b\n")
# cast a and b to int
a = int(a)
b = int(b)
# take the small and the big variable
if (a > b):
    # m is the small variable
    m = b
    # M is the big variable
    M = a
else:
    m = a
    M = b
# seperate the result output
print("integers between", a, "and", b, "are:")
# initialize a sum variable with 0
s = 0
# start the loop
for i in range(m + 1, M, 1):
    print(i)
    s += i
mean = float(s)/(M - m - 1)
print("their sum is:", s)
print("their mean is:", mean)
