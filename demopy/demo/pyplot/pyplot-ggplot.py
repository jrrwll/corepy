from matplotlib import pyplot
from sklearn import datasets
from sklearn import linear_model

pyplot.style.use('ggplot')

# load data
boston = datasets.load_boston()
yb = boston.target.reshape(-1, 1)
xb = boston['data'][:, 5].reshape(-1, 1)
# plot data
pyplot.scatter(xb, yb)
pyplot.ylabel('value of house /1000 ($)')
pyplot.xlabel('number of rooms')

# create linear regression object
regr = linear_model.LinearRegression()
# train the model using the training sets
regr.fit(xb, yb)
# Plot outputs
pyplot.scatter(xb, yb, color='black')
pyplot.plot(xb, regr.predict(xb), color='blue',
            linewidth=3)
pyplot.show()
