# prob1.py

# Importez les modules nécessaires de scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Chargez le jeu de données Iris
iris = load_iris()
X, y = iris.data, iris.target

# Divisez les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialisez le modèle de classification KNeighbors
knn = KNeighborsClassifier(n_neighbors=3)

# Entraînez le modèle sur l'ensemble d'entraînement
knn.fit(X_train, y_train)

# Prédisez les étiquettes pour l'ensemble de test
y_pred = knn.predict(X_test)

# Évaluez l'exactitude du modèle
accuracy = accuracy_score(y_test, y_pred)
print(f"Précision du modèle : {accuracy}")
