from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 

iris = load_iris() 
X_train,X_test,y_train,y_test = train_test_split(iris.data, iris.target,test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier 
from sklearn import metrics 


for i in range(1,30):
    num_neigh = i
    knn = KNeighborsClassifier(n_neighbors = num_neigh) 
    knn.fit(X_train, y_train) 
    y_pred = knn.predict(X_test) 
    scores = metrics.accuracy_score(y_test, y_pred)
    if ((i == 1) or (i == 3) or (i == 5) or (i == 10) or (i == 20) or (i == 30)):
        print('n_neighbors가 {0:d}일때 정확도: {1:.3f}'.format(num_neigh, scores))
    else:
        pass
    