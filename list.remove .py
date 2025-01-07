#sets

# lst=[10,20,30,40,50]
# print(lst)
# lst[1:4]=99
# print(lst) Error because of sets is incomplete

# lst=[10,20,30,40,50]
# print(lst)
# lst[1:4]=[99]
# print(lst) (this syntax is correct to do sets)

# lst=[10,20,30,40,50]
# print(lst)
# lst[1:4]=[99,88,77]
# print(lst) ( giving multiple values)

# Remove

# lst=[10,20,30,40,50]
# print(lst)
# lst.remove(30)
# print(lst)     ( Removing the values )

#checking the condition true or false

# lst=[10,20,30,40,50,60]
# print(30 in lst)

# lst=[10,20,30,40,50,60]
# print(30 not in lst)

#pop:pop is used to remove the value

# lst=[10,20,30,40,50,60]
# print(lst)
# lst.pop()
# print(lst)

# lst=[10,20,30,40,50,60]
# print(lst)
# lst.pop(3)
# print(lst)

# a=[10,10,20]
# o/p=10-->2,20-->1

# a=[10,10,20]
# for x in a:
#     print(x,'-->',a.count(x))
# print([a.count(x) for x in a])

# #use sets(wont accept duplicates)

# a=[10,10,20]
# for x in set(a):
#     print(x,'-->',a.count(x))
# print([a.count(x) for x in a]

# val='armani'
# op:aa
# using IN operator

# val='armani'
# vowels='aeiou'
# for x in val:
#     if x in vowels:
#         print(x)