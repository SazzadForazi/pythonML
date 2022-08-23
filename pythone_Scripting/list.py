spam = [["car", "dog", "bat", "ball"], [10, 20, 30, 40]]
print(spam[0][1])
print(spam[0][1:3])  # slice
y = spam[1][2] = 52
print(spam)
print(spam[1][1:])
print(spam[1][:2])
del spam[0][1]
print(spam)

a = [4, 5, 6, 9]
b = [8, 9, 2, 3]
print(a+b)
b = "Hello"
print(list(b))


print(list(range(4)))
print(list(range(0, 100, 4)))


supp = ["car", "dog", "bat", "ball"]
for i in range(len(supp)):
    print("index "+str(i) + " output is " + supp[i])

print(supp.index("dog"))
supp.append("mouse")
supp.insert(1, "chiken")
supp.remove("car")
del supp[1]
print(supp)
