# -*- coding: utf-8 -*-
"""single layer perceptron.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LA3Vv5Z7-giUOo0km6NMLyh_eK2pHY4V
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.plotting import plot_decision_regions

dataset = pd.read_csv("//content//drive//MyDrive//DL study//placement (1).csv")

dataset.head(3)

plt.figure(figsize=(4,3))
sns.scatterplot(x="cgpa",y="placement_exam_marks",data=dataset,hue="placed")
plt.show()

x=dataset.iloc[:,:-1]
y=dataset["placed"]



from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=20)



from sklearn.linear_model import Perceptron

pr = Perceptron()
pr.fit(x_train,y_train)

"""**Accuracy checking:**"""

pr.score(x_train,y_train)*100, pr.score(x_test,y_test)*100

"""**Checking graph decision**"""

plt.figure(figsize=(4,3))
plot_decision_regions(x_train.to_numpy(),y_train.to_numpy(),clf=pr)
plt.show()

# So this the linitation that perceptron model nver work correctly or separate it.

# to overcome above limitation we use Multi Layer Perceptron Model: