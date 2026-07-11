import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

os.makedirs("output", exist_ok=True)

iris = load_iris()
X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(y, iris.target_names)

print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nStatistics:")
print(df.describe())

plt.figure(figsize=(6,4))
sns.countplot(x="species", data=df)
plt.tight_layout()
plt.savefig("output/class_distribution.png")
plt.close()

sns.pairplot(df, hue="species")
plt.savefig("output/pairplot.png")
plt.close()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

scores = []
for k in range(1, 16):
    m = KNeighborsClassifier(n_neighbors=k)
    m.fit(X_train, y_train)
    scores.append(accuracy_score(y_test, m.predict(X_test)))

best_k = scores.index(max(scores)) + 1
print(f"Best K: {best_k}")

model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, pred))
print("\nClassification Report:\n")
print(classification_report(y_test, pred, target_names=iris.target_names))

cm = confusion_matrix(y_test, pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("output/confusion_matrix.png")
plt.close()

plt.figure(figsize=(6,4))
plt.plot(range(1,16), scores, marker="o")
plt.xlabel("K")
plt.ylabel("Accuracy")
plt.grid(True)
plt.tight_layout()
plt.savefig("output/accuracy_vs_k.png")
plt.close()

joblib.dump({"model":model,"scaler":scaler}, "iris_model.pkl")

print("\nCustom Prediction")
try:
    vals = []
    prompts = ["Sepal length","Sepal width","Petal length","Petal width"]
    for p in prompts:
        vals.append(float(input(f"{p}: ")))
    new = scaler.transform([vals])
    result = model.predict(new)[0]
    print("Predicted Species:", iris.target_names[result])
except Exception:
    print("Skipping custom prediction.")

print("\nDone! Check output folder for graphs.")
