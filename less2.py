i=5
a=[]
while i >= 1:
    name = input("input num - ")
    a += name
    i -= 1
for e in a:
    if int(e) < 5:
        print(e)
print([e for e in a if int(e) > 5])
