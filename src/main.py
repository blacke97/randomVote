import random as rd

# 例如，班级共30人，对选举班级内优秀班干部投票，班干部共7人，优秀班干部名额5人
# 则投票总人数30人
# 被投票人数7人
# 每个人可以投的票数为5

voter = int (input("请输入投票总人数："))
tickets = int (input("请输入每个人可以投的票数："))
voted = int (input("请输入被投票人数："))

res = [0] * voted
for i in range(voter):
    person = rd.sample(range(0, voted), tickets)
    for j in person:
        res[j]+=1

print(res)