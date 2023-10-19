n=input("enter the number of the list")
tab=[]
t=[]
m=[]
for i in range(n):
    tab.append(int(input("enter the element number",i,"of the first list")))
    t.append(int(input("enter the element number",i,"of the second list)")))
    m.append(tab[i]+t[i])
print(m)
             