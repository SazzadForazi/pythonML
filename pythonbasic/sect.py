x = ("apple", "banana", "cherry")
# y = list(x)
# y[1]="xxx"
# x=tuple(y)
# # print(y)
# print(x)


y=list(x)
y.append('orrange')
print(tuple(y)*2)
x=y.count("banana")
print(x)