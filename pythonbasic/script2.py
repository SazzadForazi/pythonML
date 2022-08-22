"""
list_order = ['#45421','#1245','#256','#954']
# list_order.sort()
# print(list_order)
print(sorted(list_order,key=len))
"""
list_order = ['#45421', '#1245', '#256', '#954']


def myfun(n):
    return int(n[1:])


y = sorted(list_order, key=myfun)
print("sorted by size", y)
