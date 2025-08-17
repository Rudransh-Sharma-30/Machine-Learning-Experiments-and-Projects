import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
cols = ["area","perimeter","compactness","length","width","asymmetry","groove","class"]
df = pd.read_csv("/Users/ajitk/Desktop/ML basics/freecodecamp/seeds_dataset.csv", names = cols , sep = "\s+") #this treats more than one preceeding spaces
for i in range(len(cols)-1):
    for j in range(i+1 , len(cols)-1):
        x_label = cols[i]
        y_label = cols[j]
        sns.scatterplot(x = x_label , y = y_label, data = df , hue = "class")
        plt.show()

print(df.head())