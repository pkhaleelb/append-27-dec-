#TUPLE

# a,*b=10,20,'c'
# print(a)
# print(b)
# print(type(a))
# print('b',type(b))
# c=11,22,33
# print(c)
# print('c',type(c))

# t=(10,20,30,40)
# t.append(99)
# print(t)   # AttributeError: 'tuple' object has no attribute 'append'
#  BEACUSE TUPLE IS IMMUTABLE ,WE CANNOT ADD,MODIFY OR DELETE.

# a=()
# print(type(a))  #<class 'tuple'>
# b=(1)
# print(type(b))  #<class 'int'>
# c=(1,)
# print(type(c))  #<class 'tuple'>

# HETEROGENOUS EXAMPLE

# tup=(10,20.5,True,1+3j,'python')
# tup=(int,float,boolean,complex val,string)

#Tuple inside=(list,tuple,set,dictionary) example

# tup=(10,[20,30,40],[50,60,70],{9,10,11},{1:'x',2:'y'}