from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

corpus = [
    "This burger is very tasty and affordable",
    "This burger is not tasty and is affordable",
    "This burger is very very delicious",
]
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names()
print("features names : ", feature_names)
matrix = vectors.todense()
list_dense = matrix.tolist()
df = pd.DataFrame(list_dense, columns=feature_names)
print(df)
