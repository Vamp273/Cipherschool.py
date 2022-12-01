a = 1
while a<10:
    print(a)
    a+=1

b = "jatin"
print(type(b))
for c in b:
    print(c)
    print(type(c))

for i in range(5):
    print(i)
    if i ==3:
        break

for i in range(5):
    print(i)
    if i ==3:
        continue

for i in range(5):
    print(i)
    i = 100
    print(i)

for i in range(5):
    print(i)
    del i

for i in [0,1,2,3,4,5]: #i=0 # i = 2
    print(i) #i=0  # i = 2
    i = 100 # i =100 # i = 1100
    print(i)  #i = 100 # i = 100

if True:
    pass
    "sfgvghnbloiooh"
print("rest of the code")

# we use pass to create empty blocks in python.

for i in range(5):
    print(i)
else:
    print("something")

for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("something")