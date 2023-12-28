numbers={"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
file=open("day1.txt","r")
sum=0

for i in file:
    num=[]
    for key in numbers:
        i=i.replace(key, str(key[0]+str(numbers[key])+key[-1]))

    for x in i:
        if(x.isdigit()):
            num.append(x)
        print(num)
    sum+=int(num[0])*10+int(num[-1])
file.close()
print(sum)