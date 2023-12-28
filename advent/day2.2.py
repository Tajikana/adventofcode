puzzle_input= open("day2.txt","r")
from collections import defaultdict

ans=0
for line in puzzle_input:
    ok= True
    id, line=line.split(":")
    V=defaultdict(int)
    for event in line.split(";"):
        for balls in event.split(","):
            n,color=balls.split()
            V[color]=max(V[color],int(n))
            print(n,color)
            if int(n)>{"red":12, "green":13, "blue":14}.get(color,0):
                ok=False
    score=1
    for v in V.values():
        score*=v
    ans+=score
    if ok:
        pass
        # ans+=int(id.split()[-1])
#         print(event)
#     print(line)
#     print(id)
print(ans)