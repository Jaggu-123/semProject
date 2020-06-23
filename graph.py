import matplotlib.pyplot as plt

x = [i for i in range(0, 60)]
list = []
listCar = []
listBus = []
listBike = []
for i in x:
    y = (((((i/2.5) - 1)*13.9)/5.45) + ((((i/0.7118) - 1)*4.52)/6.35) + ((((i/0.5375) - 1)*1.7272)/3.2))/3
    y1 = ((((i/2.5) - 1)*13.9)/5.45)
    y2 = ((((i/0.7118) - 1)*4.52)/6.35)
    y3 = ((((i/0.5375) - 1)*1.7272)/3.2)
    listBike.append(y3)
    listBus.append(y1)
    listCar.append(y2)
    # if y <= 3:
    #     y = 3
    # elif y >= 60:
    #     y = 60
    list.append(y)

plt.plot(x, listBike, label = 'bike')
plt.plot(x, listBus, label='bus')
plt.plot(x, listCar, label='car')
plt.plot(x, list, label = 'average')
plt.legend()
plt.show()