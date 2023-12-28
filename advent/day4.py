file = open("day4.txt", "r")
count=0
arr=[]
for card in file:
    card= card.split(":")
    first,rest = card[1].split("|")

    first_nums =[int(x) for x in first.split()]
    rest_nums = [int(x) for x in rest.split()]
    num=[]

    for num1 in first_nums:
        for num2 in rest_nums:
            if num1 == num2:
                num.append(num1)
    ans=len(num)
    if(ans!=0):
        ans=2**(ans-1)
        arr.append(ans)
count=sum(arr)
print(count)


