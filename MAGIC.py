import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler

cols = ["fLength","fWitdh","fSize","fConc","fConc1","fAsym","fM3Long","fM3Trans","fAlpha","fDist","class"]
df = pd.read_csv("/Users/ajitk/Desktop/ML basics/freecodecamp/magic+gamma+telescope/magic04.csv", names = cols)

df["class"] = (df["class"]=='g').astype(int)
# print(df.head())
# print(df["class"].unique())
for label in cols[:-1]:
    plt.hist(df[df["class"]== 1][label],color= 'blue',label = 'gamma',alpha = 0.7, density = True)
    plt.hist(df[df["class"]== 0][label],color= 'red',label = 'hadron',alpha = 0.7, density = True)
    plt.title(label)
    plt.ylabel("Probability")
    plt.xlabel(label)
    plt.legend()
    # plt.show()
train , valid , test = np.split(df.sample(frac = 1),[int(0.6*len(df)),int(0.8*len(df))])

def scale_dataset(dataframe,oversample = False):
    X = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    if oversample:
        ros = RandomOverSampler()
        X,y = ros.fit_resample(X,y) 
    data = np.hstack((X,np.reshape(y,(-1,1))))


    return data , X , y

train , X_train , y_train = scale_dataset(train, oversample = True)
valid , X_valid , y_valid = scale_dataset(valid, oversample = False)
test , X_test , y_test = scale_dataset(test, oversample = False)
from sklearn.neighbors import KNeighborsClassifier
knn_model = KNeighborsClassifier(n_neighbors = 3)
knn_model.fit(X_train,y_train)

y_pred = knn_model.predict(X_test)
# print(y_pred)
# print(y_test)
from sklearn.metrics import classification_report

# print(classification_report(y_test,y_pred))

from sklearn.naive_bayes import GaussianNB
nb_model = GaussianNB()
nb_model.fit(X_train,y_train)
y_pred = nb_model.predict(X_test)
# print(classification_report(y_test,y_pred))
from sklearn.linear_model import LogisticRegression
lg_model = LogisticRegression()
lg_model.fit(X_train,y_train)

y_pred = lg_model.predict(X_test)
# print(y_pred)
# print(classification_report(y_test,y_pred))

from sklearn.svm import SVC
svm_model = SVC()
svm_model = svm_model.fit(X_train,y_train)
y_pred = svm_model.predict(X_test)
print(y_pred , classification_report(y_test, y_pred))


