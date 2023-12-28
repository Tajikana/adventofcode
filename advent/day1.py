file=open("day1.txt","r")
sum=0
for i in file:
    num = []
    for x in i:
        if(x.isdigit()):
            num.append(x)
    sum+=int(num[0])*10+int(num[-1])
file.close()
print(sum)

