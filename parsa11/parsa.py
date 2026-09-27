def l_saz(num:int):
    data=[]
    while len(data)<num:
        name=input("esme:")
        if len (name)<=2:
            raise NameError("esmet khayli kotah shode.")
        if len (data)==0:
            data.append(name)
        else:
            h_e=input("1.hazf ya 2.ezafe:")
            if h_e=="1":
                try:
                    data.remove(name)
                except:
                    print("in dar list sabt nami ma nist.")
                else:
                    print(":)))")
                finally:
                    print("tamam")
            else:
                data.append(name)
    return data
with open("text.txt","w+") as text:
    print(text.writable())
    text.write("salam\n")
    text.writelines(("man khobam\nto khotory\nemroz1405/6/30"))

adad=1
def f_saz(data:list,name:str):
    with open(f"{name}.txt","w+") as a:
        global adad
        for i in data:
            a.write(f"{adad}*{i}\n")
            adad+=1
    return f"{name}.text"


def add(file1):
    with open (file1,"a+") as a:
        Q1=input("yek khat mikhahi ezafe beshe ya hazf ya chanta?")
        if Q1=="yek":
            new=input("che ra mikhahid ezafe shavad:")
            a.write(f"{new}\n")
        else:
            n_list=[]
            while True:
                new=input("matn khode ra vard khonid:")
                if new!="0":
                    n_list.append(f"{new}\n")
                else:
                    break
            global adad
            for i in n_list:
                a.write(f"{adad}*{i}")
                adad+=1
    return file1
l_1=l_saz(3)
l_2=f_saz(l_1,"text")
l_3=add("text.txt")