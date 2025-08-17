import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from imblearn.over_sampling import RandomOverSampler
from sklearn.preprocessing import StandardScaler
import copy
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

dataset_cols = ["bike_count","hour","temp","humidity","wind","visibility","dew_pt_temp","radiation","rain","snow","functional"]

df = pd.read_csv("/Users/ajitk/Desktop/ML basics/freecodecamp/SeoulBikeData_UTF8(new).csv")
df = df.drop(["Date","Holiday","Seasons"],axis = 1)
df.columns = dataset_cols
df["functional"] = (df["functional"] == "Yes").astype(int)
df = df[df["hour"] == 12]
df = df.drop("hour",axis = 1)
for label in df.columns[1:]:
    plt.scatter(df[label],df["bike_count"])
    plt.title(label)
    plt.ylabel("Bike count in noon is")
    plt.xlabel(label)
    # plt.show()

df = df.drop(["wind","visibility","functional"],axis = 1)
from sklearn.model_selection import train_test_split
y = df["bike_count"]
X = df.drop(["bike_count"], axis = 1)
# print(X)
# print(y)
X_temp, X_test , y_temp , y_test = train_test_split(X,y,test_size = 0.2 , random_state = 42)
X_train , X_val , y_train , y_val = train_test_split(X,y,test_size = 0.2, random_state= 42)
reg_model = LinearRegression()
reg_model.fit(X_train , y_train)

preds = reg_model.predict(X_val)
rmse = mean_squared_error(y_val , preds )
print(preds , (rmse)**(0.5))
print(y_val)



