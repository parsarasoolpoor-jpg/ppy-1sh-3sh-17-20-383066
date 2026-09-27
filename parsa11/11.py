"""with open("parsa.txt","w+")as a:
    a.write("salam\n")
    a.writelines(("man khobam\nto khotory\nemroz1405/6/30"))"""


"""with open("parsa.txt",("r+")) as a:
    a.seek(0)
    res=a.readline()
    print(res)
    print(a.tell())"""

with open("parsa.txt","r+") as m:
    res=m.readlines()
    print(res)

res.insert(5,"!!!!\n")
print(res)

with open("parsa.txt","w+") as m:
    m.writelines(res)
