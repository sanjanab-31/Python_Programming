from array import array as a
mc=[1,2,34,4,5]
print(mc)
print(type(mc))
mc[2]='ss'
print(mc)
nc=a("i",)
print(nc)
print(type(mc))
nc.append(20)
print(nc)
nc.insert(1,33)
print(nc)
nc.append("sanju")
print(nc)