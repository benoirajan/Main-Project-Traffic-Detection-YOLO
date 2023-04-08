from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

actual = [1,1,1,1,1,1,1,1,1,1,1,1,1,0]
predicted=[0,1,1,1,0,1,1,1,1,0,1,1,1,1]

cm = confusion_matrix(actual,predicted)
print(cm)

cm = [
    [.95, .2],
    [.05, .8]
]

sns.heatmap(cm,annot=True,cmap='Blues')
plt.savefig("./plots/plot.png")
plt.show()