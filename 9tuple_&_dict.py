tup = ("hi","Python",8)

print(type(tup))

print(tup[:3:2])

print (tup + tup) 



print("this is : "+ tup[1])



d =  {1:'Jimmy', 2:'Alex', "a":'john', 4:'mike',5:{"i":"AK"}}

print(d)

print(d[5]["i"])
print(d["a"])

print (d.keys())
print (d.values())

d["akash"] = "AKKA"
del d["a"]
print(d)


# d2 = d 
d2 = d.copy()

del d2[1]

print(d)