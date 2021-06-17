from matplotlib import pyplot

labels = 'frogs', 'hogs', 'dogs', 'logs'
sizes = 15, 20, 45, 10
colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'
explode = 0, 0.1, 0, 0
pyplot.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
pyplot.axis('equal')
pyplot.show()

# show chinese
print(pyplot.rcParams.keys())
pyplot.rcParams['font.sans-serif'] = ['DejaVu Sans']
pyplot.rcParams['axes.unicode_minus'] = False
