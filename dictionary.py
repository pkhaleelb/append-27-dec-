# DICTIONARY(always in key value format)

# dct={'name':'arjun','age':21}
# print(dct['name'])  only name is print here 
 
# dct={'name':'arjun','age':21}
# for x in dct:
#     print(x,dct[x])  here both name and age will print

# dct={'name':'arjun','age':21}
# for key,value in dct.items():
#     print(key,value)

#  Nested dictionary(in dictionary there is one more dct is called nested)

# dct={'hr':{'name':'raj','age':21},'it':{'name':'rrr','age':25}}
# print(dct['it']['name'])

#code

# lst=[1,2,3,4]
# emp=[]
# for x in lst:
#     emp.append(x**3)
# print(emp)

# one line code

# print([x**3 for x in [1,2,3,4]])

#dictionary in the list of cube,square

# lst=[1,2,3,4]
# print({x: x**3 for x in lst})
# print({x: x**2 for x in lst})

# mutable

# val=[1,2]
# val[0]=[100]
# print(val)

# immutable
# val=[1,2]
# val[0]=[100]
# print(val)
# st=[1,2]
# st[0]=[100]
