# Pythonic way
#
l=[1,2,3,4,5,6,7,8,9,10]
e=filter(lambda x: x%2==0, l)
print(list(e))

##Another method-
## Lay man method
l_copy = []
for i in l:
  if i%2==0:
    l_copy.append(i)
print(l_copy,'\n')
