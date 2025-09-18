import seaborn as sns
from matplotlib import pyplot as plt

titanic = sns.load_dataset("titanic")
plt.figure(figsize=(15,12))

plt.subplot(2,3,1)
sns.boxplot(x="survived", y="age", data=titanic)
plt.title("Age Distribution By Survival Status")
plt.xlabel("Survived(0: No, 1: Yes)")
plt.ylabel("Age")

plt.subplot(2,3,2)
sns.boxplot(x="sex", y="age", data=titanic)
plt.title("Age Distribution By Gender")
plt.xlabel("Gender")
plt.ylabel("Age")

plt.subplot(2,3,3)
sns.boxplot(x="class", y="fare", data=titanic)
plt.title("Fare Distribution By Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")

plt.subplot(2,3,4)
sns.boxplot(x="survived", y="fare", data=titanic)
plt.title("Fare Distribution By Survival Status")
plt.xlabel("Survived(0: No, 1: Yes)")
plt.ylabel("Fare")

plt.subplot(2,3,5)
sns.boxplot(x="sex", y="age",hue="survived", data=titanic ,palette="rocket")
plt.title("Age by Gender and Survival")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.legend(title="Survived", labels=["no", "Yes"])

plt.show()