import pandas as pd

data = pd.read_csv("/Users/ajitk/Desktop/ML basics/melb_data.csv")
y = data.Price
# print(y)
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = data[features]

# print(X.head())

from sklearn.tree import DecisionTreeRegressor


# model.fit(X,y)
# print("Making predictions for the first 5 rows: ")
# print(X.head())
# print("The prediction of the price is ")
# prediction = model.predict(X)

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

train_X,val_X, train_y , val_y = train_test_split(X,y,random_state = 0)


# model.fit(train_X,train_y)
# val_prediction = model.predict(val_X)
# error = mean_absolute_error(val_y,val_prediction)
# print(train_X.shape, train_y.shape)
# print(val_prediction)
# print(error)

# def get_mae(max_leaf_nodes, train_X, train_y , val_X, val_y):
#     home_model = DecisionTreeRegressor(max_leaf_nodes= max_leaf_nodes)
#     home_model.fit(train_X, train_y)
#     pred_val = home_model.predict(val_X)
#     mae = mean_absolute_error(val_y,pred_val)
#     return mae

# for max_leaf_nodes in [5,50,500,5000]:
#     mae = get_mae(max_leaf_nodes, train_X, train_y , val_X, val_y)
#     print("The max_leaf_nodes are:" , max_leaf_nodes ,"Mean_absolute_error is:" , mae)

'we use this model to reduce the chances of overfitting and underfitting. It checks mae for different leaves/ nodes and then find the right amount of leaves to use'
'randomtreeregressor is better as it makes multiple descision trees and averages things out which tends to give better result than decisiontreeregressor'
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(random_state=1)

model.fit(train_X, train_y)

prediction = model.predict(val_X)
mae = mean_absolute_error(val_y, prediction)
print(f"The prediction is: {prediction} and the mean_absolute_error is : {mae}")
"This gave a better result 18100 vs 22900"