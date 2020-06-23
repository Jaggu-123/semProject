import matplotlib.pyplot as plt

def func(i):
    y = (((((i/2.5) - 1)*13.9)/5.45) + ((((i/0.7118) - 1)*4.52)/6.35) + ((((i/0.5375) - 1)*1.7272)/3.2))/3
    if i == 0:
        y = 0
    elif y <= 3:
        y = 3
    elif y >= 60:
        y = 60
    print((i, int(y)))
    return int(y)

LaneA = [89, 12, 13, 34, 32, 34, 45, 67, 45, 123, 45, 23, 234, 43]
LaneB = [12, 23, 34, 23, 12, 11, 54, 45, 67, 56, 54, 39, 40, 55]
LaneC = [15, 34, 44, 47, 56, 87, 78, 45, 11, 7, 56, 45, 67, 100]
LaneD = [56, 100, 30, 24, 99, 105, 23, 0, 3, 56, 78, 89, 88, 56]

ttl = 172
val = 172
vehcile = []
TimeA = []
TimeB = []
TimeC = []
TimeD = []
AverageVar = []
AvergaeFixed = []
Total = []

for i in range(1, len(LaneA)):
    # Total.append((LaneD[i] + LaneC[i] + LaneB[i] + LaneA[i])/4)
    ttl = ttl - func(LaneA[i-1])
    val = val - LaneA[i-1]
    TimeA.append((val, ttl))
    val = val + LaneA[i]
    ttl = ttl + func(LaneA[i])
    ttl = ttl - func(LaneB[i-1])
    val = val - LaneB[i-1]
    TimeB.append((val, ttl))
    ttl = ttl + func(LaneB[i])
    val = val + LaneB[i]
    ttl = ttl - func(LaneC[i-1])
    val = val - LaneC[i-1]
    TimeC.append((val,ttl))
    ttl = ttl + func(LaneC[i])
    val = val + LaneC[i]
    ttl = ttl - func(LaneD[i-1])
    val = val - LaneD[i-1]
    TimeD.append((val,ttl))
    ttl = ttl + func(LaneD[i])
    val = val + LaneD[i]
    vehcile.append(val/4)
    # AverageVar.append(ttl)

print(TimeA)
print(TimeB)
print(TimeC)
print(TimeD)
print(vehcile)
print(len(vehcile))
print(len(AverageVar))

for i in range(0, len(TimeA)):
    AverageVar.append(((TimeC[i][0] + TimeA[i][0] + TimeB[i][0] + TimeD[i][0])/4,(TimeC[i][1] + TimeA[i][1] + TimeB[i][1] + TimeD[i][1])/4))
    AvergaeFixed.append(180)

# AverageVar.sort()
# AvergaeFixed.sort()

print(len(AvergaeFixed))
for i in range(0, len(AvergaeFixed)):
    vehcile[i] = AverageVar[i][0]
    AverageVar[i] = (AverageVar[i][1])
    AvergaeFixed[i] = (AvergaeFixed[i])

print(vehcile)
print(AvergaeFixed)
print(AverageVar)

plt.scatter(vehcile, AverageVar, label = 'variable')
plt.scatter(vehcile, AvergaeFixed, label = 'fixed')
plt.xlabel('Average number of vehicle')
plt.ylabel('Average waiting time')


plt.legend()

plt.show()