# lst=[1,2,4]
# sum=0
# for x in lst:
#     sum+=x
# print(sum)

# type casting(converting the datatype from string to int)

# lst=['100','222','88']
# for x in lst:
#     prd=1
#     for y in x:
#         prd*=int(y)
#     print(prd)

lst=[100,222,88]
for x in lst:
    prd=1
    for y in str(x):
        prd*=int(y)
    print(prd)
