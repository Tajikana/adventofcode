file = open("day4.txt", "r")
count=0
arr=[]
cardzz=0
for card in file:
    cardno,card= card.split(":")
    first,rest = card.split("|")
    print(int(cardno[5:8]))

    first_nums =[int(x) for x in first.split()]
    rest_nums = [int(x) for x in rest.split()]
    num=[]

    for num1 in first_nums:
        for num2 in rest_nums:
            if num1 == num2:
                num.append(num1)
    ans=len(num)
    while(ans>0):
        file.append()
        ans-=1
    print(ans)
count=sum(arr)
print(count)
