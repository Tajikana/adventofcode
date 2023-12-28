puzzle_input= open("day2.txt","r")

ans=0
for line in puzzle_input:
    ok= True
    id, line=line.split(":")
    for event in line.split(";"):
        for balls in event.split(","):
            n,color=balls.split()
            if int(n)>{"red":12, "green":13, "blue":14}.get(color,0):
                ok=False
    if ok:
        ans+=int(id.split()[-1])
        print(event)
    print(line)
    print(id)
print(ans)

