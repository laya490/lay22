a=[10,20,50,60,50,30,40,50]
a.append(60)
print(a)
a.insert(1,15)
print(a)
print(15 in a)
print(a.count(50))
a.remove(50)
print(a)

a.pop(2)
print(a)
del a[1]
print(max(a))
print(min(a))
print(sum(a))
a.reverse()
print(a)
print(a.sort())
print(sorted(a))
c=24.5
v=6
h=c//v
print(h)
h=c**v
print(h)
print(2**65+10//3)
print(2**5-3)