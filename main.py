# import the "matplotlib", "pandas" and "seaborn" libraries.
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# We downloaded and read the "iris" dataset, one of the most well-known datasets.
data = pd.read_csv("iris.csv")
print(data.head())

# It is possible to create many kinds of graphics with this library. Let's create a few of them.
# Scatter plot
sns.scatterplot(x='sepal.length', y='sepal.width', data=data)

# Barplot
sns.barplot(x='petal.length', y='petal.width', data = data)

# Histplot
sns.histplot(data["sepal.length"])

# Kdeplot (Density Chart)
sns.kdeplot(data["petal.length"], shade = True)  # It ensures that the area under the chart is filled.

# Boxplot
sns.boxplot(x = "petal.length", y = "petal.width", data = data)

# Violinplot
sns.violinplot(x = "petal.length", y = "petal.width", data = data)

# Pairplot
sns.pairplot(data, hue = "sepal.length")

# Heatmap
sns.heatmap(data.corr(), annot = True, linewidths = 2)      # (annot = make number values invisible, linewidths = space between boxes)

# Pointplot
sns.pointplot(x = "petal.length", y = "petal.width", data = data)
